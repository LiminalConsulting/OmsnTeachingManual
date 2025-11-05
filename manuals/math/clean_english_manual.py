#!/usr/bin/env python3
"""
Clean English Mathematics Manual for printing
Removes metadata clutter while preserving core educational content
"""

import re

def clean_manual(input_file, output_file):
    """Remove metadata and clean up the manual for printing"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    cleaned_lines = []
    skip_next = False
    in_metadata_block = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip metadata patterns
        skip_patterns = [
            r'^\*\*Source:\*\*',
            r'^\*\*Grades?:\*\*',
            r'^\*\*Extraction Date:\*\*',
            r'^\*\*Source URL:\*\*',
            r'^\*\*Page Title:\*\*',
            r'^\*\*Author:\*\*',
            r'^\*\*Publication Date:\*\*',
            r'^\*\*Last Modified:\*\*',
            r'^\*\*Website:\*\*',
            r'^\*\*Related Topics:\*\*',
            r'^\*\*Tags:\*\*',
            r'^\*\*Navigation:\*\*',
        ]

        # Check if line matches any skip pattern
        should_skip = False
        for pattern in skip_patterns:
            if re.match(pattern, line.strip()):
                should_skip = True
                break

        if should_skip:
            i += 1
            continue

        # Skip "Available Resources" sections that are empty
        if '## Available Resources' in line or '## Classes and Worksheets' in line:
            # Look ahead to see if there's actual content
            j = i + 1
            has_content = False
            while j < len(lines) and not lines[j].startswith('##'):
                if lines[j].strip() and not lines[j].startswith('**') and '---' not in lines[j]:
                    if 'under construction' not in lines[j].lower() and 'coming soon' not in lines[j].lower():
                        has_content = True
                        break
                j += 1

            if not has_content:
                # Skip until next section
                i = j
                continue

        # Skip standalone dividers (---) between metadata
        if line.strip() == '---':
            # Check if surrounded by metadata or empty lines
            prev_line = lines[i-1].strip() if i > 0 else ''
            next_line = lines[i+1].strip() if i < len(lines)-1 else ''

            if not prev_line or not next_line or any(re.match(p, prev_line) for p in skip_patterns):
                i += 1
                continue

        # Skip "Grade X" headers - we want natural progression
        if re.match(r'^##\s+Grade\s+\d+', line.strip()):
            i += 1
            continue

        # Skip empty "estado do conteúdo" notices
        if 'under construction' in line.lower() or 'coming soon' in line.lower():
            i += 1
            continue

        # Keep the line
        cleaned_lines.append(line)
        i += 1

    # Join lines and clean up multiple blank lines
    cleaned_content = '\n'.join(cleaned_lines)

    # Replace 3+ consecutive newlines with just 2
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    print(f"✅ Cleaned manual written to: {output_file}")

    # Statistics
    original_lines = len(lines)
    cleaned_line_count = len(cleaned_lines)
    removed = original_lines - cleaned_line_count

    print(f"📊 Lines: {original_lines} → {cleaned_line_count} (removed {removed})")

if __name__ == '__main__':
    clean_manual('MANUAL_FINAL_EN.md', 'MANUAL_FINAL_EN_PRINT.md')
