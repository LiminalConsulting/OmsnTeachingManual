#!/usr/bin/env python3
"""
Analyze where Portuguese and English PDFs diverge in pagination
to identify optimal locations for strategic page breaks.
"""

import subprocess
import re

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def get_page_breaks(pdf_path):
    """Extract text for each page to identify content boundaries"""
    try:
        # Get number of pages
        result = subprocess.run(
            ['pdfinfo', pdf_path],
            capture_output=True,
            text=True,
            check=True
        )
        pages_match = re.search(r'Pages:\s+(\d+)', result.stdout)
        if not pages_match:
            return None

        num_pages = int(pages_match.group(1))

        # Extract text from each page
        pages = []
        for i in range(1, num_pages + 1):
            result = subprocess.run(
                ['pdftotext', '-f', str(i), '-l', str(i), '-layout', pdf_path, '-'],
                capture_output=True,
                text=True
            )
            text = result.stdout.strip()
            # Get first non-empty line as page identifier
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            if lines:
                first_line = lines[0][:80]  # First 80 chars
                pages.append((i, first_line, len(text)))
            else:
                pages.append((i, "[Empty page]", 0))

        return pages
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

def find_section_headers(md_path):
    """Extract major section headers from markdown with line numbers"""
    sections = []
    with open(md_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Look for major headers (# or ##)
            if line.startswith('# ') or line.startswith('## '):
                header = line.strip()
                sections.append((line_num, header))
    return sections

def analyze_alignment(pt_pdf, en_pdf, pt_md, en_md):
    """Compare page structure between Portuguese and English versions"""

    print("📊 Analyzing PDF Page Alignment\n")
    print("=" * 80)

    # Get page info
    pt_pages = get_page_breaks(pt_pdf)
    en_pages = get_page_breaks(en_pdf)

    if not pt_pages or not en_pages:
        print("❌ Failed to extract page information")
        return

    print(f"\n📄 Page Counts:")
    print(f"  Portuguese: {len(pt_pages)} pages")
    print(f"  English: {len(en_pages)} pages")
    print(f"  Difference: {abs(len(pt_pages) - len(en_pages))} pages")

    # Get section headers from markdown
    pt_sections = find_section_headers(pt_md)
    en_sections = find_section_headers(en_md)

    print(f"\n📑 Section Headers:")
    print(f"  Portuguese: {len(pt_sections)} major sections")
    print(f"  English: {len(en_sections)} major sections")

    # Show first few pages comparison
    print(f"\n🔍 First 10 Pages Comparison:")
    print("-" * 80)
    max_compare = min(10, len(pt_pages), len(en_pages))

    for i in range(max_compare):
        pt_page, pt_text, pt_len = pt_pages[i]
        en_page, en_text, en_len = en_pages[i]

        print(f"\nPage {i+1}:")
        print(f"  PT: {pt_text[:60]}... ({pt_len} chars)")
        print(f"  EN: {en_text[:60]}... ({en_len} chars)")

        if abs(pt_len - en_len) > 200:
            print(f"  ⚠️  Large difference: {abs(pt_len - en_len)} chars")

    # Identify major sections
    print(f"\n📚 Major Sections (first 10):")
    print("-" * 80)
    for i, (pt_info, en_info) in enumerate(zip(pt_sections[:10], en_sections[:10])):
        pt_line, pt_header = pt_info
        en_line, en_header = en_info
        print(f"\n{i+1}. Line {pt_line} (PT) / Line {en_line} (EN)")
        print(f"   PT: {pt_header}")
        print(f"   EN: {en_header}")

        if abs(pt_line - en_line) > 5:
            print(f"   ⚠️  Line number drift: {abs(pt_line - en_line)} lines")

    print("\n" + "=" * 80)
    print("\n💡 Recommendations:")
    print("  - Major sections should have \\clearpage or \\cleardoublepage")
    print("  - Focus on sections where page count diverges most")
    print("  - Add strategic breaks at section boundaries")

if __name__ == '__main__':
    pt_pdf = 'MANUAL_FINAL_PHYSICS_CHEMISTRY.pdf'
    en_pdf = 'MANUAL_FINAL_PHYSICS_CHEMISTRY_EN.pdf'
    pt_md = 'MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md'
    en_md = 'MANUAL_FINAL_PHYSICS_CHEMISTRY_EN_PRINT.md'

    analyze_alignment(pt_pdf, en_pdf, pt_md, en_md)
