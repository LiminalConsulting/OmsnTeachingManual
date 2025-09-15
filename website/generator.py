#!/usr/bin/env python3
"""
OMSN Teaching Manual Website Generator

A dynamic, content-agnostic static site generator that converts markdown manuals
into beautiful, interactive websites. Automatically discovers and processes any
markdown files ending with "Manual" in the name.

Features:
- Automatic table of contents generation
- Responsive design with dark/light theme
- Search functionality
- Progress tracking
- Interactive navigation
- Zero maintenance after setup

Usage:
    python3 generator.py

Author: OMSN Teaching Manual Project
License: GNU Affero General Public License v3.0
"""

import os
import re
import sys
import glob
import html
from pathlib import Path
from urllib.parse import quote


def install_dependencies():
    """Install required Python packages if not available."""
    try:
        import markdown2
        return markdown2
    except ImportError:
        print("Installing required dependencies...")
        try:
            # Try with --user flag first
            result = os.system(f"{sys.executable} -m pip install --user markdown2")
            if result != 0:
                # Try with --break-system-packages if --user fails
                result = os.system(f"{sys.executable} -m pip install --break-system-packages markdown2")
                if result != 0:
                    print("❌ Failed to install markdown2. Please install manually:")
                    print("   Option 1: pip3 install --user markdown2")
                    print("   Option 2: pip3 install --break-system-packages markdown2")
                    print("   Option 3: Create virtual environment and install there")
                    sys.exit(1)
            import markdown2
            return markdown2
        except Exception as e:
            print(f"❌ Error installing dependencies: {e}")
            print("Please install markdown2 manually: pip3 install --user markdown2")
            sys.exit(1)


def clean_filename(filename):
    """Convert filename to URL-friendly format."""
    name = Path(filename).stem
    # Remove common prefixes and clean up
    name = re.sub(r'^(Grade_?\d+_|Unified_)', '', name)
    name = re.sub(r'[^a-zA-Z0-9_-]', '-', name)
    name = re.sub(r'-+', '-', name).strip('-').lower()
    return name


def extract_title_from_markdown(content):
    """Extract the main title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return "Manual"


def generate_table_of_contents(content):
    """Generate HTML table of contents from markdown headers."""
    headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    if not headers:
        return "<ul><li>No sections found</li></ul>"

    toc_html = ["<ul>"]

    for level_hashes, title in headers:
        level = len(level_hashes)
        # Skip h1 as it's usually the main title
        if level == 1:
            continue

        # Clean title for ID generation
        anchor_id = re.sub(r'[^a-zA-Z0-9_-]', '-', title.lower())
        anchor_id = re.sub(r'-+', '-', anchor_id).strip('-')

        # Create navigation item
        escaped_title = html.escape(title)
        toc_item = f'<li><a href="#{anchor_id}" class="level-{level}">{escaped_title}</a></li>'
        toc_html.append(toc_item)

    toc_html.append("</ul>")
    return "\n".join(toc_html)


def add_header_ids(html_content):
    """Add IDs to headers for navigation linking."""
    def replace_header(match):
        tag = match.group(1)
        content = match.group(2)

        # Generate ID from content
        header_id = re.sub(r'[^a-zA-Z0-9_-]', '-', content.lower())
        header_id = re.sub(r'-+', '-', header_id).strip('-')

        return f'<{tag} id="{header_id}">{content}</{tag}>'

    # Add IDs to h2-h6 headers (h1 is usually the main title)
    html_content = re.sub(r'<(h[2-6])>(.+?)</(h[2-6])>', replace_header, html_content)
    return html_content


def enhance_content(html_content):
    """Enhance HTML content with special styling and interactive elements."""
    # Enhanced checkbox styling
    html_content = html_content.replace(
        '<input type="checkbox"',
        '<input type="checkbox" onclick="this.disabled=true"'
    )

    # Add visual markers for special content
    html_content = re.sub(
        r'📊\s*\*\*([^*]+)\*\*',
        r'<span class="visual-marker">📊 VISUAL</span><strong>\1</strong>',
        html_content
    )

    html_content = re.sub(
        r'🔗\s*\*\*([^*]+)\*\*',
        r'<span class="connection-marker">🔗 CONNECTION</span><strong>\1</strong>',
        html_content
    )

    # Enhance emoji content
    emoji_pattern = r'([📊📚🧩🔍💻💬🔗📐🔢📈])'
    html_content = re.sub(emoji_pattern, r'<span class="emoji-icon">\1</span>', html_content)

    # Add copy buttons to code blocks (will be enhanced by JavaScript)
    html_content = re.sub(r'<pre><code', r'<pre class="code-block"><code', html_content)

    return html_content


def generate_index_page(manual_files, output_dir):
    """Generate an index page listing all available manuals."""
    template_path = Path(__file__).parent / "template.html"
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Create manual listing
    manual_list = []
    manual_list.append('<div style="text-align: center; margin-bottom: 3rem;">')
    manual_list.append('<h1>🎓 OMSN Teaching Manual Collection</h1>')
    manual_list.append('<p style="font-size: 1.2rem; color: var(--text-secondary);">Interactive educational resources for visual, creative mathematics teaching</p>')
    manual_list.append('</div>')

    manual_list.append('<div style="display: grid; gap: 1.5rem; max-width: 800px; margin: 0 auto;">')

    for manual_file in manual_files:
        # Read manual to extract title and description
        with open(manual_file, 'r', encoding='utf-8') as f:
            content = f.read()

        title = extract_title_from_markdown(content)
        clean_name = clean_filename(manual_file)

        # Extract first paragraph as description
        lines = content.split('\n')
        description = "Comprehensive teaching manual and resource collection"
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('*') and not line.startswith('**'):
                description = line[:150] + "..." if len(line) > 150 else line
                break

        manual_card = f'''
        <div style="
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            transition: var(--transition);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'"
           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.1)'">

            <h3 style="margin-top: 0; color: var(--primary-color);">
                <a href="{clean_name}.html" style="text-decoration: none; color: inherit;">
                    {html.escape(title)}
                </a>
            </h3>
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">
                {html.escape(description)}
            </p>
            <a href="{clean_name}.html" style="
                display: inline-block;
                background: var(--primary-color);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 500;
                transition: var(--transition);
            " onmouseover="this.style.background='var(--secondary-color)'"
               onmouseout="this.style.background='var(--primary-color)'">
                View Manual →
            </a>
        </div>
        '''
        manual_list.append(manual_card)

    manual_list.append('</div>')

    # Add footer
    manual_list.append('''
    <div style="text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border-color);">
        <p style="color: var(--text-secondary);">
            <strong>OMSN Teaching Manual Project</strong><br>
            Supporting visual, creative, and integrated mathematics education<br>
            <small>Generated automatically from markdown source files</small>
        </p>
    </div>
    ''')

    content_html = '\n'.join(manual_list)
    toc_html = '''
    <ul>
        <li><a href="#" class="level-1">Manual Collection</a></li>
        <li><a href="#about" class="level-2">About This Project</a></li>
    </ul>
    '''

    # Replace template placeholders
    html_output = template.replace('{{TITLE}}', 'OMSN Teaching Manual Collection')
    html_output = html_output.replace('{{CONTENT}}', content_html)
    html_output = html_output.replace('{{TABLE_OF_CONTENTS}}', toc_html)

    # Write index page
    index_path = output_dir / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"✅ Generated index page: {index_path}")


def process_manual(manual_file, output_dir, template):
    """Process a single manual markdown file into HTML."""
    print(f"🔄 Processing: {manual_file}")

    # Read markdown content
    with open(manual_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Extract title
    title = extract_title_from_markdown(markdown_content)

    # Convert markdown to HTML
    markdown2 = install_dependencies()
    html_content = markdown2.markdown(
        markdown_content,
        extras=[
            'fenced-code-blocks',
            'tables',
            'task_list',
            'strike',
            'target-blank-links',
            'header-ids'
        ]
    )

    # Generate table of contents
    toc_html = generate_table_of_contents(markdown_content)

    # Enhance content
    html_content = add_header_ids(html_content)
    html_content = enhance_content(html_content)

    # Replace template placeholders
    html_output = template.replace('{{TITLE}}', html.escape(title))
    html_output = html_output.replace('{{CONTENT}}', html_content)
    html_output = html_output.replace('{{TABLE_OF_CONTENTS}}', toc_html)

    # Generate output filename
    clean_name = clean_filename(manual_file)
    output_file = output_dir / f"{clean_name}.html"

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"✅ Generated: {output_file}")
    return output_file


def main():
    """Main function to generate the website."""
    print("🚀 OMSN Teaching Manual Website Generator")
    print("="*50)

    # Setup paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_dir = script_dir / "output"
    template_path = script_dir / "template.html"

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Load HTML template
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Find all manual files
    manual_patterns = [
        str(project_root / "*Manual*.md"),
        str(project_root / "*manual*.md"),
        str(project_root / "Manual*.md"),
        str(project_root / "manual*.md"),
    ]

    manual_files = []
    for pattern in manual_patterns:
        manual_files.extend(glob.glob(pattern))

    # Remove duplicates and sort
    manual_files = sorted(list(set(manual_files)))

    if not manual_files:
        print("⚠️  No manual files found matching patterns:")
        for pattern in manual_patterns:
            print(f"   - {pattern}")
        print("\nMake sure your markdown files contain 'Manual' in the filename.")
        sys.exit(1)

    print(f"📚 Found {len(manual_files)} manual(s):")
    for manual in manual_files:
        print(f"   - {Path(manual).name}")
    print()

    # Process each manual
    generated_files = []
    for manual_file in manual_files:
        try:
            output_file = process_manual(manual_file, output_dir, template)
            generated_files.append(output_file)
        except Exception as e:
            print(f"❌ Error processing {manual_file}: {e}")
            continue

    # Generate index page
    if generated_files:
        generate_index_page(manual_files, output_dir)

    print(f"\n🎉 Website generation complete!")
    print(f"📁 Output directory: {output_dir}")
    print(f"🌐 Open in browser: {output_dir}/index.html")

    if len(generated_files) > 0:
        print(f"✅ Successfully generated {len(generated_files)} manual page(s)")
    else:
        print("❌ No files were generated successfully")


if __name__ == "__main__":
    main()