#!/usr/bin/env python3
"""
Generate paracol bilingual source from PT and EN markdown files.
Usage: python3 make_bilingual.py <pt_file> <en_file> <output_file>

Splits both files on '## ' headings, then interleaves PT and EN sections
using LaTeX paracol syntax for side-by-side bilingual layout.
"""

import sys
import re

def split_on_h2(text):
    """Split text into sections starting with ## headings (or the initial block)."""
    # Split on lines that start with ## (keeping the delimiter)
    parts = re.split(r'\n(?=## )', text)
    return parts

def main():
    if len(sys.argv) != 4:
        print("Usage: make_bilingual.py <pt_file> <en_file> <output_file>")
        sys.exit(1)

    pt_file, en_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(pt_file, 'r', encoding='utf-8') as f:
        pt_text = f.read()
    with open(en_file, 'r', encoding='utf-8') as f:
        en_text = f.read()

    pt_sections = split_on_h2(pt_text)
    en_sections = split_on_h2(en_text)

    # Pad shorter list if unequal
    n = max(len(pt_sections), len(en_sections))
    while len(pt_sections) < n:
        pt_sections.append('')
    while len(en_sections) < n:
        en_sections.append('')

    lines = []
    lines.append(r'\begin{paracol}{2}')
    lines.append('')

    for i, (pt, en) in enumerate(zip(pt_sections, en_sections)):
        pt = pt.strip()
        en = en.strip()
        if not pt and not en:
            continue

        lines.append(pt)
        lines.append('')
        lines.append(r'\switchcolumn')
        lines.append('')
        lines.append(en)
        lines.append('')

        # Use \switchcolumn* (synchronized page break) between major sections
        if i < n - 1:
            lines.append(r'\switchcolumn*')
            lines.append('')

    lines.append(r'\end{paracol}')

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Written {len(pt_sections)} section pairs to {out_file}")

if __name__ == '__main__':
    main()
