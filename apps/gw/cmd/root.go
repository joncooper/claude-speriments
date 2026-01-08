package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "gw",
	Short: "Gmail and Google Calendar CLI",
	Long: `gw is a command-line interface for Gmail and Google Calendar.

It provides fast access to your email and calendar from the terminal,
designed to work seamlessly with Claude Code and other CLI tools.

First time setup:
  gw auth login    # Authenticate with Google

Gmail commands:
  gw mail list     # List recent emails
  gw mail read ID  # Read a specific email
  gw mail send     # Send an email
  gw mail search   # Search emails

Calendar commands:
  gw cal list      # List upcoming events
  gw cal create    # Create an event
  gw cal delete    # Delete an event`,
}

func Execute() error {
	return rootCmd.Execute()
}

func init() {
	rootCmd.CompletionOptions.DisableDefaultCmd = true
}

// Helper to print errors and exit
func exitError(msg string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, "Error: "+msg+"\n", args...)
	os.Exit(1)
}
