#!/usr/bin/env python3
"""
Add page breaks before major sections in both Portuguese and English manuals
This ensures the 5 main sections start on odd (right-hand) pages for alignment
"""

import re

def add_page_breaks(input_file, output_file):
    """Add \\cleardoublepage before major sections"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Major sections to align (all 5 main chapters)
    major_sections = [
        r'^# NUMBERS$',
        r'^# ALGEBRA$',
        r'^# GEOMETRY$',
        r'^# MEASUREMENT$',
        r'^# DATA ORGANIZATION AND TREATMENT$',
        # Portuguese versions
        r'^# NÚMEROS$',
        r'^# ÁLGEBRA$',
        r'^# GEOMETRIA$',
        r'^# MEDIDA$',
        r'^# ORGANIZAÇÃO E TRATAMENTO DE DADOS$',
    ]

    lines = content.split('\n')
    result_lines = []

    for i, line in enumerate(lines):
        # Check if this line is a major section header
        is_major_section = any(re.match(pattern, line.strip()) for pattern in major_sections)

        if is_major_section and i > 0:  # Don't add before first section
            # Add page break before the section
            result_lines.append('')
            result_lines.append('\\cleardoublepage')
            result_lines.append('')

        result_lines.append(line)

    output_content = '\n'.join(result_lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"✅ Added page breaks to: {output_file}")

if __name__ == '__main__':
    # Process both Portuguese and English versions
    print("Adding page breaks for section alignment...")

    add_page_breaks('MANUAL_FINAL_PRINT.md', 'MANUAL_FINAL_PRINT_ALIGNED.md')
    add_page_breaks('MANUAL_FINAL_EN_PRINT.md', 'MANUAL_FINAL_EN_PRINT_ALIGNED.md')

    print("\n✅ Both manuals now have aligned major sections!")
