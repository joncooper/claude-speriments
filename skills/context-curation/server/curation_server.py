#!/usr/bin/env python3
"""
Simple HTTP server for the context curation tool.

Serves the curation UI and receives the curated content via POST.
Claude Code polls /status to know when the user is done.
"""

import argparse
import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs

# Global state
_done = False
_output_file = None
_html_file = None


class CurationHandler(BaseHTTPRequestHandler):
    """Handle requests for the curation UI."""

    def log_message(self, format, *args):
        """Suppress default logging."""
        pass

    def _send_json(self, data, status=200):
        """Send a JSON response."""
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, content):
        """Send an HTML response."""
        body = content.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests."""
        global _done, _html_file

        if self.path == '/':
            # Serve the HTML UI
            try:
                with open(_html_file, 'r', encoding='utf-8') as f:
                    self._send_html(f.read())
            except Exception as e:
                self._send_json({'error': str(e)}, 500)

        elif self.path == '/status':
            # Return current status for polling
            self._send_json({'done': _done})

        else:
            self.send_error(404)

    def do_POST(self):
        """Handle POST requests."""
        global _done, _output_file

        if self.path == '/done':
            # Receive the curated content
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(body)

                curated_content = data.get('content', '')

                # Write to output file
                with open(_output_file, 'w', encoding='utf-8') as f:
                    f.write(curated_content)

                _done = True
                self._send_json({'success': True})

            except Exception as e:
                self._send_json({'error': str(e)}, 500)

        else:
            self.send_error(404)

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def main():
    global _output_file, _html_file

    parser = argparse.ArgumentParser(description='Context curation server')
    parser.add_argument('--port', type=int, default=8765, help='Port to listen on')
    parser.add_argument('--html', required=True, help='Path to HTML file to serve')
    parser.add_argument('--output', required=True, help='Path to write curated output')
    args = parser.parse_args()

    _html_file = args.html
    _output_file = args.output

    # Verify HTML file exists
    if not os.path.exists(_html_file):
        print(f"Error: HTML file not found: {_html_file}", file=sys.stderr)
        sys.exit(1)

    # Create output directory if needed
    output_dir = os.path.dirname(_output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    server = HTTPServer(('localhost', args.port), CurationHandler)
    print(f"Server running on http://localhost:{args.port}")
    print(f"Output will be written to: {_output_file}")
    sys.stdout.flush()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
