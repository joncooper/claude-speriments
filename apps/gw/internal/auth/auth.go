package auth

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/joncooper/gw/internal/config"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/calendar/v3"
	"google.golang.org/api/gmail/v1"
)

// Scopes required for Gmail and Calendar access
var Scopes = []string{
	gmail.GmailReadonlyScope,
	gmail.GmailSendScope,
	gmail.GmailModifyScope,
	calendar.CalendarReadonlyScope,
	calendar.CalendarEventsScope,
}

// GetClient returns an authenticated HTTP client
func GetClient(ctx context.Context) (*http.Client, error) {
	cfg, err := getOAuthConfig()
	if err != nil {
		return nil, fmt.Errorf("failed to get OAuth config: %w", err)
	}

	token, err := getToken(ctx, cfg)
	if err != nil {
		return nil, fmt.Errorf("failed to get token: %w", err)
	}

	return cfg.Client(ctx, token), nil
}

// getOAuthConfig returns the OAuth2 configuration
func getOAuthConfig() (*oauth2.Config, error) {
	credBytes, err := config.ReadCredentials()
	if err != nil {
		return nil, fmt.Errorf("unable to read credentials file: %w\n\nRun 'gw auth setup' to configure credentials", err)
	}

	cfg, err := google.ConfigFromJSON(credBytes, Scopes...)
	if err != nil {
		return nil, fmt.Errorf("unable to parse credentials: %w", err)
	}

	return cfg, nil
}

// getToken retrieves a token from cache or initiates OAuth flow
func getToken(ctx context.Context, cfg *oauth2.Config) (*oauth2.Token, error) {
	tokenBytes, err := config.ReadToken()
	if err == nil {
		var token oauth2.Token
		if err := json.Unmarshal(tokenBytes, &token); err == nil {
			// Check if token is still valid or can be refreshed
			if token.Valid() {
				return &token, nil
			}
			// Try to refresh
			tokenSource := cfg.TokenSource(ctx, &token)
			newToken, err := tokenSource.Token()
			if err == nil {
				config.SaveToken(newToken)
				return newToken, nil
			}
		}
	}

	return nil, fmt.Errorf("not authenticated. Run 'gw auth login' to authenticate")
}

// Login performs the OAuth2 login flow
func Login(ctx context.Context) error {
	cfg, err := getOAuthConfig()
	if err != nil {
		return err
	}

	// Start local server for OAuth callback
	codeChan := make(chan string, 1)
	errChan := make(chan error, 1)

	server := &http.Server{Addr: ":8089"}

	http.HandleFunc("/callback", func(w http.ResponseWriter, r *http.Request) {
		code := r.URL.Query().Get("code")
		if code == "" {
			errChan <- fmt.Errorf("no code in callback")
			fmt.Fprintf(w, "<html><body><h1>Error</h1><p>No authorization code received.</p></body></html>")
			return
		}
		codeChan <- code
		fmt.Fprintf(w, "<html><body><h1>Success!</h1><p>You can close this window and return to the terminal.</p></body></html>")
	})

	go func() {
		if err := server.ListenAndServe(); err != http.ErrServerClosed {
			errChan <- err
		}
	}()

	// Generate auth URL
	cfg.RedirectURL = "http://localhost:8089/callback"
	authURL := cfg.AuthCodeURL("state-token", oauth2.AccessTypeOffline, oauth2.ApprovalForce)

	fmt.Println("\n Opening browser for Google authentication...")
	fmt.Println("\nIf the browser doesn't open, visit this URL:")
	fmt.Printf("\n  %s\n\n", authURL)

	// Try to open browser
	openBrowser(authURL)

	// Wait for callback
	var code string
	select {
	case code = <-codeChan:
	case err := <-errChan:
		server.Shutdown(ctx)
		return fmt.Errorf("OAuth callback error: %w", err)
	case <-time.After(5 * time.Minute):
		server.Shutdown(ctx)
		return fmt.Errorf("authentication timeout")
	}

	server.Shutdown(ctx)

	// Exchange code for token
	token, err := cfg.Exchange(ctx, code)
	if err != nil {
		return fmt.Errorf("failed to exchange code: %w", err)
	}

	// Save token
	if err := config.SaveToken(token); err != nil {
		return fmt.Errorf("failed to save token: %w", err)
	}

	fmt.Println("Authentication successful!")
	return nil
}

// Logout removes the cached token
func Logout() error {
	if err := config.DeleteToken(); err != nil && !os.IsNotExist(err) {
		return fmt.Errorf("failed to delete token: %w", err)
	}
	fmt.Println("Logged out successfully")
	return nil
}

// Status prints the current authentication status
func Status() {
	if !config.CredentialsExist() {
		fmt.Println("Status: Not configured")
		fmt.Println("\nRun 'gw auth setup' to configure OAuth credentials")
		return
	}

	if !config.TokenExists() {
		fmt.Println("Status: Credentials configured, not logged in")
		fmt.Println("\nRun 'gw auth login' to authenticate")
		return
	}

	// Try to verify token
	ctx := context.Background()
	client, err := GetClient(ctx)
	if err != nil {
		fmt.Println("Status: Token expired or invalid")
		fmt.Println("\nRun 'gw auth login' to re-authenticate")
		return
	}

	// Quick check with Gmail API
	srv, err := gmail.New(client)
	if err != nil {
		fmt.Println("Status: Error creating Gmail client")
		return
	}

	profile, err := srv.Users.GetProfile("me").Do()
	if err != nil {
		fmt.Println("Status: Token invalid")
		fmt.Println("\nRun 'gw auth login' to re-authenticate")
		return
	}

	fmt.Println("Status: Authenticated")
	fmt.Printf("Email: %s\n", profile.EmailAddress)
}

// openBrowser attempts to open the URL in the default browser
func openBrowser(url string) {
	// Try common browser open commands
	commands := [][]string{
		{"xdg-open", url},
		{"open", url},
		{"cmd", "/c", "start", url},
	}

	for _, cmd := range commands {
		if _, err := os.Stat("/usr/bin/" + cmd[0]); err == nil {
			// Command exists, try to run it
			go func(args []string) {
				// Best effort - ignore errors
				os.StartProcess("/usr/bin/"+args[0], args, &os.ProcAttr{})
			}(cmd)
			return
		}
	}
}
