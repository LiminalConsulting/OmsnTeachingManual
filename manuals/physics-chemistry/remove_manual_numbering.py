#!/usr/bin/env python3
"""
Remove manual numbering from markdown headers to prevent double-numbering
when pandoc's --number-sections is applied.

Transforms:
  # 1. TITLE -> # TITLE
  ## 1.1 Subtitle -> ## Subtitle
  ### 1.1.1 Topic -> ### Topic
"""

import re
import sys

def remove_manual_numbering(content):
    """Remove manual numbering patterns from markdown headers."""

    # Pattern matches: # 1. TITLE or ## 1.1 Title or ### 1.1.1 Topic
    # Captures the header level (#, ##, ###) and the text after the number
    pattern = r'^(#{1,6})\s+\d+(\.\d+)*\.?\s+'

    lines = content.split('\n')
    cleaned_lines = []

    for line in lines:
        # Check if line is a numbered header
        if re.match(pattern, line):
            # Remove the numbering, keep the header level and text
            cleaned_line = re.sub(pattern, r'\1 ', line)
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def main():
    input_file = 'MANUAL_FINAL_PHYSICS_CHEMISTRY.md'
    output_file = 'MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md'

    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Removing manual numbering from headers...")
    cleaned_content = remove_manual_numbering(content)

    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print("✅ Done! Manual numbering removed.")
    print(f"   Input:  {input_file}")
    print(f"   Output: {output_file}")

if __name__ == '__main__':
    main()
