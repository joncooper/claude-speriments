#!/usr/bin/env python3
"""
Generate the curation HTML with source file content embedded.

Usage:
    python generate_html.py --output /tmp/curation.html file1.md file2.txt ...

The script reads the template HTML and injects the source files as a JSON object.
"""

import argparse
import json
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Generate curation HTML')
    parser.add_argument('--output', required=True, help='Output HTML file path')
    parser.add_argument('--template', help='Template HTML file (defaults to curation_ui.html in same dir)')
    parser.add_argument('files', nargs='+', help='Source files to include')
    args = parser.parse_args()

    # Find template
    if args.template:
        template_path = args.template
    else:
        script_dir = Path(__file__).parent
        template_path = script_dir / 'curation_ui.html'

    if not os.path.exists(template_path):
        print(f"Error: Template not found: {template_path}", file=sys.stderr)
        sys.exit(1)

    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Read source files - expects JSON input from stdin
    # Format: {"filename": "content", ...}
    source_files = {}

    # Check if we have stdin input (piped JSON)
    if not sys.stdin.isatty():
        try:
            source_files = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON from stdin: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Read files directly from filesystem (fallback)
        for filepath in args.files:
            if not os.path.exists(filepath):
                print(f"Warning: File not found: {filepath}", file=sys.stderr)
                continue

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Use just the filename as the key
                name = os.path.basename(filepath)
                source_files[name] = content
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)

    if not source_files:
        print("Error: No source files loaded", file=sys.stderr)
        sys.exit(1)

    # Inject into template
    json_data = json.dumps(source_files, ensure_ascii=False)
    html = template.replace('__SOURCE_FILES_PLACEHOLDER__', json_data)

    # Write output
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated: {args.output}")
    print(f"Files included: {len(source_files)}")


if __name__ == '__main__':
    main()
