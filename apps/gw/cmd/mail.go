package cmd

import (
	"bufio"
	"context"
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/joncooper/gw/internal/auth"
	gwgmail "github.com/joncooper/gw/internal/gmail"
	"github.com/spf13/cobra"
)

var mailCmd = &cobra.Command{
	Use:     "mail",
	Aliases: []string{"m", "gmail"},
	Short:   "Gmail commands",
	Long:    `Commands for interacting with Gmail.`,
}

var mailListCmd = &cobra.Command{
	Use:   "list",
	Short: "List recent emails",
	Long: `List recent emails from your inbox.

Examples:
  gw mail list              # List 10 recent emails
  gw mail list -n 25        # List 25 recent emails
  gw mail list --unread     # List only unread emails`,
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		n, _ := cmd.Flags().GetInt64("number")
		unread, _ := cmd.Flags().GetBool("unread")
		query, _ := cmd.Flags().GetString("query")

		var labels []string
		if unread {
			labels = append(labels, "UNREAD")
		}

		messages, err := srv.ListMessages(ctx, n, query, labels)
		if err != nil {
			exitError("%v", err)
		}

		if len(messages) == 0 {
			fmt.Println("No messages found")
			return
		}

		for _, m := range messages {
			unreadMarker := " "
			if m.IsUnread {
				unreadMarker = "*"
			}
			fmt.Printf("%s %s  %-20s  %-40s  %s\n",
				unreadMarker,
				m.ID[:12],
				truncate(m.From, 20),
				truncate(m.Subject, 40),
				formatDate(m.Date))
		}
	},
}

var mailReadCmd = &cobra.Command{
	Use:   "read <message-id>",
	Short: "Read an email",
	Long: `Read the contents of an email.

Examples:
  gw mail read abc123def456     # Read message by ID
  gw mail read abc123 --raw     # Show raw message without formatting`,
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		messageID := args[0]
		raw, _ := cmd.Flags().GetBool("raw")
		markRead, _ := cmd.Flags().GetBool("mark-read")

		msg, err := srv.GetMessage(ctx, messageID, true)
		if err != nil {
			exitError("%v", err)
		}

		if raw {
			fmt.Printf("ID: %s\n", msg.ID)
			fmt.Printf("Thread: %s\n", msg.ThreadID)
			fmt.Printf("Date: %s\n", msg.Date.Format(time.RFC1123))
			fmt.Printf("From: %s\n", msg.From)
			fmt.Printf("To: %s\n", msg.To)
			fmt.Printf("Subject: %s\n", msg.Subject)
			fmt.Printf("Labels: %s\n", strings.Join(msg.Labels, ", "))
			fmt.Println("\n---")
			fmt.Println(msg.Body)
		} else {
			printFormattedMessage(msg)
		}

		if markRead && msg.IsUnread {
			if err := srv.MarkAsRead(ctx, messageID); err != nil {
				fmt.Fprintf(os.Stderr, "Warning: failed to mark as read: %v\n", err)
			}
		}
	},
}

var mailThreadCmd = &cobra.Command{
	Use:   "thread <thread-id>",
	Short: "Read an email thread",
	Long: `Read all messages in a thread.

Examples:
  gw mail thread abc123def456   # Read all messages in thread`,
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		threadID := args[0]
		messages, err := srv.GetThread(ctx, threadID)
		if err != nil {
			exitError("%v", err)
		}

		fmt.Printf("Thread: %s (%d messages)\n", threadID, len(messages))
		fmt.Println(strings.Repeat("=", 60))

		for i, msg := range messages {
			if i > 0 {
				fmt.Println("\n" + strings.Repeat("-", 60) + "\n")
			}
			printFormattedMessage(msg)
		}
	},
}

var mailSearchCmd = &cobra.Command{
	Use:   "search <query>",
	Short: "Search emails",
	Long: `Search emails using Gmail search syntax.

Examples:
  gw mail search "from:boss@company.com"
  gw mail search "subject:urgent is:unread"
  gw mail search "has:attachment larger:5M"
  gw mail search "after:2024/01/01 before:2024/02/01"`,
	Args: cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		query := strings.Join(args, " ")
		n, _ := cmd.Flags().GetInt64("number")

		messages, err := srv.SearchMessages(ctx, query, n)
		if err != nil {
			exitError("%v", err)
		}

		if len(messages) == 0 {
			fmt.Println("No messages found")
			return
		}

		fmt.Printf("Found %d messages matching: %s\n\n", len(messages), query)
		for _, m := range messages {
			unreadMarker := " "
			if m.IsUnread {
				unreadMarker = "*"
			}
			fmt.Printf("%s %s  %-20s  %-40s  %s\n",
				unreadMarker,
				m.ID[:12],
				truncate(m.From, 20),
				truncate(m.Subject, 40),
				formatDate(m.Date))
		}
	},
}

var mailSendCmd = &cobra.Command{
	Use:   "send",
	Short: "Send an email",
	Long: `Send a new email.

Examples:
  gw mail send --to user@example.com --subject "Hello" --body "Hi there"
  gw mail send --to user@example.com --subject "Hello" --body-file message.txt
  echo "Message" | gw mail send --to user@example.com --subject "Hello" --body-stdin`,
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		to, _ := cmd.Flags().GetString("to")
		subject, _ := cmd.Flags().GetString("subject")
		body, _ := cmd.Flags().GetString("body")
		bodyFile, _ := cmd.Flags().GetString("body-file")
		bodyStdin, _ := cmd.Flags().GetBool("body-stdin")
		cc, _ := cmd.Flags().GetStringSlice("cc")
		bcc, _ := cmd.Flags().GetStringSlice("bcc")
		draft, _ := cmd.Flags().GetBool("draft")

		if to == "" {
			exitError("--to is required")
		}
		if subject == "" {
			exitError("--subject is required")
		}

		// Get body from various sources
		if bodyStdin {
			scanner := bufio.NewScanner(os.Stdin)
			var lines []string
			for scanner.Scan() {
				lines = append(lines, scanner.Text())
			}
			body = strings.Join(lines, "\n")
		} else if bodyFile != "" {
			data, err := os.ReadFile(bodyFile)
			if err != nil {
				exitError("failed to read body file: %v", err)
			}
			body = string(data)
		}

		if body == "" {
			exitError("message body is required (--body, --body-file, or --body-stdin)")
		}

		if draft {
			id, err := srv.CreateDraft(ctx, to, subject, body)
			if err != nil {
				exitError("%v", err)
			}
			fmt.Printf("Draft created: %s\n", id)
		} else {
			msg, err := srv.SendMessage(ctx, to, subject, body, cc, bcc)
			if err != nil {
				exitError("%v", err)
			}
			fmt.Printf("Message sent: %s\n", msg.ID)
		}
	},
}

var mailReplyCmd = &cobra.Command{
	Use:   "reply <message-id>",
	Short: "Reply to an email",
	Long: `Reply to an existing email.

Examples:
  gw mail reply abc123 --body "Thanks for your message"
  gw mail reply abc123 --body-file reply.txt`,
	Args: cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		messageID := args[0]
		body, _ := cmd.Flags().GetString("body")
		bodyFile, _ := cmd.Flags().GetString("body-file")
		bodyStdin, _ := cmd.Flags().GetBool("body-stdin")

		// Get body from various sources
		if bodyStdin {
			scanner := bufio.NewScanner(os.Stdin)
			var lines []string
			for scanner.Scan() {
				lines = append(lines, scanner.Text())
			}
			body = strings.Join(lines, "\n")
		} else if bodyFile != "" {
			data, err := os.ReadFile(bodyFile)
			if err != nil {
				exitError("failed to read body file: %v", err)
			}
			body = string(data)
		}

		if body == "" {
			exitError("reply body is required (--body, --body-file, or --body-stdin)")
		}

		msg, err := srv.ReplyToMessage(ctx, messageID, body)
		if err != nil {
			exitError("%v", err)
		}
		fmt.Printf("Reply sent: %s\n", msg.ID)
	},
}

var mailAttachmentCmd = &cobra.Command{
	Use:   "attachment <message-id> [attachment-id]",
	Short: "Download email attachments",
	Long: `Download attachments from an email.

Examples:
  gw mail attachment abc123           # List attachments in message
  gw mail attachment abc123 att456    # Download specific attachment
  gw mail attachment abc123 --all     # Download all attachments`,
	Args: cobra.RangeArgs(1, 2),
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		messageID := args[0]
		outDir, _ := cmd.Flags().GetString("output")
		downloadAll, _ := cmd.Flags().GetBool("all")

		msg, err := srv.GetMessage(ctx, messageID, true)
		if err != nil {
			exitError("%v", err)
		}

		if len(msg.Attachments) == 0 {
			fmt.Println("No attachments in this message")
			return
		}

		// List attachments if no specific one requested
		if len(args) == 1 && !downloadAll {
			fmt.Printf("Attachments in message %s:\n\n", messageID)
			for _, att := range msg.Attachments {
				fmt.Printf("  %s  %-30s  %s  %d bytes\n",
					att.ID[:12],
					att.Filename,
					att.MimeType,
					att.Size)
			}
			fmt.Println("\nUse 'gw mail attachment <message-id> <attachment-id>' to download")
			fmt.Println("Or 'gw mail attachment <message-id> --all' to download all")
			return
		}

		// Download specific attachment or all
		toDownload := msg.Attachments
		if len(args) == 2 {
			attachmentID := args[1]
			toDownload = nil
			for _, att := range msg.Attachments {
				if strings.HasPrefix(att.ID, attachmentID) {
					toDownload = append(toDownload, att)
					break
				}
			}
			if len(toDownload) == 0 {
				exitError("attachment not found: %s", attachmentID)
			}
		}

		for _, att := range toDownload {
			path, err := srv.DownloadAttachment(ctx, messageID, att.ID, att.Filename, outDir)
			if err != nil {
				fmt.Fprintf(os.Stderr, "Failed to download %s: %v\n", att.Filename, err)
				continue
			}
			fmt.Printf("Downloaded: %s\n", path)
		}
	},
}

var mailLabelsCmd = &cobra.Command{
	Use:   "labels",
	Short: "List all labels",
	Run: func(cmd *cobra.Command, args []string) {
		ctx := context.Background()
		client, err := auth.GetClient(ctx)
		if err != nil {
			exitError("%v", err)
		}

		srv, err := gwgmail.NewService(ctx, client)
		if err != nil {
			exitError("%v", err)
		}

		labels, err := srv.GetLabels(ctx)
		if err != nil {
			exitError("%v", err)
		}

		fmt.Println("Labels:")
		for _, l := range labels {
			fmt.Printf("  %s\n", l)
		}
	},
}

func init() {
	rootCmd.AddCommand(mailCmd)

	// List command
	mailCmd.AddCommand(mailListCmd)
	mailListCmd.Flags().Int64P("number", "n", 10, "Number of messages to list")
	mailListCmd.Flags().Bool("unread", false, "Show only unread messages")
	mailListCmd.Flags().StringP("query", "q", "", "Gmail search query")

	// Read command
	mailCmd.AddCommand(mailReadCmd)
	mailReadCmd.Flags().Bool("raw", false, "Show raw output without formatting")
	mailReadCmd.Flags().Bool("mark-read", false, "Mark message as read after viewing")

	// Thread command
	mailCmd.AddCommand(mailThreadCmd)

	// Search command
	mailCmd.AddCommand(mailSearchCmd)
	mailSearchCmd.Flags().Int64P("number", "n", 20, "Maximum number of results")

	// Send command
	mailCmd.AddCommand(mailSendCmd)
	mailSendCmd.Flags().StringP("to", "t", "", "Recipient email address")
	mailSendCmd.Flags().StringP("subject", "s", "", "Email subject")
	mailSendCmd.Flags().StringP("body", "b", "", "Email body text")
	mailSendCmd.Flags().String("body-file", "", "Read body from file")
	mailSendCmd.Flags().Bool("body-stdin", false, "Read body from stdin")
	mailSendCmd.Flags().StringSlice("cc", nil, "CC recipients")
	mailSendCmd.Flags().StringSlice("bcc", nil, "BCC recipients")
	mailSendCmd.Flags().Bool("draft", false, "Create draft instead of sending")

	// Reply command
	mailCmd.AddCommand(mailReplyCmd)
	mailReplyCmd.Flags().StringP("body", "b", "", "Reply body text")
	mailReplyCmd.Flags().String("body-file", "", "Read body from file")
	mailReplyCmd.Flags().Bool("body-stdin", false, "Read body from stdin")

	// Attachment command
	mailCmd.AddCommand(mailAttachmentCmd)
	mailAttachmentCmd.Flags().StringP("output", "o", ".", "Output directory for downloads")
	mailAttachmentCmd.Flags().Bool("all", false, "Download all attachments")

	// Labels command
	mailCmd.AddCommand(mailLabelsCmd)
}

// Helper functions

func truncate(s string, maxLen int) string {
	if len(s) <= maxLen {
		return s
	}
	return s[:maxLen-3] + "..."
}

func formatDate(t time.Time) string {
	now := time.Now()
	if t.Year() == now.Year() && t.YearDay() == now.YearDay() {
		return t.Format("15:04")
	}
	if t.Year() == now.Year() {
		return t.Format("Jan 2")
	}
	return t.Format("Jan 2, 2006")
}

func printFormattedMessage(msg *gwgmail.Message) {
	fmt.Printf("From: %s\n", msg.From)
	fmt.Printf("To: %s\n", msg.To)
	fmt.Printf("Date: %s\n", msg.Date.Format("Mon, Jan 2, 2006 at 3:04 PM"))
	fmt.Printf("Subject: %s\n", msg.Subject)

	if len(msg.Attachments) > 0 {
		fmt.Printf("Attachments: %d\n", len(msg.Attachments))
		for _, att := range msg.Attachments {
			fmt.Printf("  - %s (%s, %d bytes)\n", att.Filename, att.MimeType, att.Size)
		}
	}

	fmt.Println("\n" + strings.Repeat("-", 60) + "\n")
	fmt.Println(msg.Body)
}
