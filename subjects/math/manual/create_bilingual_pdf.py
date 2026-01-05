#!/usr/bin/env python3
"""
Create a bilingual PDF where each spread shows Portuguese on the left and English on the right.
Uses PyPDF2 to interleave pages from both PDFs.
"""

from PyPDF2 import PdfReader, PdfWriter
import sys

def create_bilingual_pdf(pt_pdf, en_pdf, output_pdf):
    """
    Create a bilingual PDF by interleaving pages:
    - Left page (even): Portuguese
    - Right page (odd): English
    """

    print("📖 Creating bilingual PDF...")

    # Read both PDFs
    pt_reader = PdfReader(pt_pdf)
    en_reader = PdfReader(en_pdf)

    pt_pages = len(pt_reader.pages)
    en_pages = len(en_reader.pages)

    print(f"Portuguese pages: {pt_pages}")
    print(f"English pages: {en_pages}")

    if pt_pages != en_pages:
        print(f"⚠️  Warning: Page counts don't match! ({pt_pages} vs {en_pages})")
        print("Using minimum page count...")

    # Create writer
    writer = PdfWriter()

    # Interleave pages: PT (left/even), EN (right/odd)
    max_pages = min(pt_pages, en_pages)

    for i in range(max_pages):
        # Add Portuguese page (left)
        writer.add_page(pt_reader.pages[i])
        # Add English page (right)
        writer.add_page(en_reader.pages[i])

        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1}/{max_pages} page pairs...")

    # Write output
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

    total_pages = len(writer.pages)
    print(f"\n✅ Bilingual PDF created: {output_pdf}")
    print(f"📄 Total pages: {total_pages} ({max_pages} Portuguese + {max_pages} English)")
    print(f"\n📖 Reading guide:")
    print("   - Odd pages (1, 3, 5...): Portuguese")
    print("   - Even pages (2, 4, 6...): English")
    print("   - Each spread shows the same content side-by-side")

if __name__ == '__main__':
    pt_pdf = 'MANUAL_FINAL.pdf'
    en_pdf = 'MANUAL_FINAL_EN.pdf'
    output_pdf = 'MANUAL_FINAL_BILINGUAL.pdf'

    try:
        create_bilingual_pdf(pt_pdf, en_pdf, output_pdf)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
