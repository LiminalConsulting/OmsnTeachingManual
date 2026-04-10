#!/usr/bin/env python3
"""
Generate paracol bilingual source from PT and EN markdown files.
Usage: python3 make_bilingual.py <pt_file> <en_file> <output_file>

Splits both files on '## ' headings, then interleaves PT and EN sections
using LaTeX paracol syntax for side-by-side bilingual layout.

The raw LaTeX commands are placed in their own paragraphs separated by blank
lines so pandoc treats them as raw LaTeX blocks while still processing the
markdown content normally.
"""

import sys
import re

def split_on_h2(text):
    """Split text into sections starting with ## headings (or the initial block)."""
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

    n = max(len(pt_sections), len(en_sections))
    while len(pt_sections) < n:
        pt_sections.append('')
    while len(en_sections) < n:
        en_sections.append('')

    lines = []
    # Use a raw LaTeX block (blank-line separated) so pandoc passes it through
    lines.append('```{=latex}')
    lines.append(r'\begin{paracol}{2}')
    lines.append('```')
    lines.append('')

    for i, (pt, en) in enumerate(zip(pt_sections, en_sections)):
        pt = pt.strip()
        en = en.strip()
        if not pt and not en:
            continue

        # PT content (left column) — as regular markdown
        lines.append(pt)
        lines.append('')

        # Switch to right column
        lines.append('```{=latex}')
        lines.append(r'\switchcolumn')
        lines.append('```')
        lines.append('')

        # EN content (right column) — as regular markdown
        lines.append(en)
        lines.append('')

        # Sync columns for next section pair
        if i < n - 1:
            lines.append('```{=latex}')
            lines.append(r'\switchcolumn*')
            lines.append('```')
            lines.append('')

    lines.append('```{=latex}')
    lines.append(r'\end{paracol}')
    lines.append('```')

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Written {len(pt_sections)} section pairs to {out_file}")

if __name__ == '__main__':
    main()
