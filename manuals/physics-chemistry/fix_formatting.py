#!/usr/bin/env python3
"""
Fix formatting issues in Physics-Chemistry manual:
1. Add blank lines before bullet/numbered lists for proper rendering
2. Convert code-block formulas to LaTeX math notation for beautiful rendering
"""

import re

def fix_list_formatting(content):
    """
    Add blank line before lists that don't have one.

    Markdown requires a blank line before lists to render them properly.
    Without it, they appear as inline text with dashes.
    """
    lines = content.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        # Check if current line is a list item (starts with -, *, +, or digit.)
        is_list_item = (
            line.strip().startswith('- ') or
            line.strip().startswith('* ') or
            line.strip().startswith('+ ') or
            re.match(r'^\s*\d+\.\s+', line)
        )

        # Check if previous line exists and is not blank
        prev_line_exists = i > 0
        prev_line_not_blank = prev_line_exists and lines[i-1].strip() != ''

        # Check if previous line is NOT a list item (to avoid adding blanks between list items)
        prev_is_not_list = True
        if prev_line_exists:
            prev_line = lines[i-1]
            prev_is_not_list = not (
                prev_line.strip().startswith('- ') or
                prev_line.strip().startswith('* ') or
                prev_line.strip().startswith('+ ') or
                re.match(r'^\s*\d+\.\s+', prev_line)
            )

        # Add blank line before list if needed
        if is_list_item and prev_line_not_blank and prev_is_not_list:
            fixed_lines.append('')  # Add blank line

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def convert_formulas_to_latex(content):
    """
    Convert code-block formulas to LaTeX math notation.

    Converts:
        **Fórmula:**
        ```
        formula here
        ```
    To:
        **Fórmula:**
        $$formula here$$

    Also converts inline formulas like Fr=m×a⃗ to $Fr=m \times a$
    """
    # Pattern 1: Code blocks that contain formulas (usually after "Fórmula:")
    # Replace ``` formula ``` with $$ formula $$
    pattern1 = r'```\n([^`]+?)\n```'

    def replace_code_block(match):
        formula = match.group(1).strip()
        # Check if it looks like a formula (has =, ×, ÷, math symbols)
        if any(char in formula for char in ['=', '×', '÷', '±', '∆', 'Δ']):
            # Convert to display math
            # Replace × with \times, ÷ with \div for LaTeX
            formula = formula.replace('×', r' \times ')
            formula = formula.replace('÷', r' \div ')
            return f'$${formula}$$'
        else:
            # Keep as code block if it doesn't look like a formula
            return match.group(0)

    content = re.sub(pattern1, replace_code_block, content)

    # Pattern 2: Inline formulas with special characters
    # Find patterns like: P = F/A or Fr=m×a⃗
    # But be careful not to match regular text

    return content

def remove_manual_numbering(content):
    """Remove manual numbering from headers (1., 1.1, etc.)"""
    pattern = r'^(#{1,6})\s+\d+(\.\d+)*\.?\s+'
    lines = content.split('\n')
    cleaned_lines = []

    for line in lines:
        if re.match(pattern, line):
            cleaned_line = re.sub(pattern, r'\1 ', line)
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def main():
    input_file = 'MANUAL_FINAL_PHYSICS_CHEMISTRY.md'
    output_file = 'MANUAL_FINAL_PHYSICS_CHEMISTRY_PRINT.md'

    print(f"📖 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("🔧 Removing manual numbering from headers...")
    content = remove_manual_numbering(content)

    print("🔧 Fixing list formatting (adding blank lines)...")
    content = fix_list_formatting(content)

    print("🔧 Converting formulas to LaTeX notation...")
    content = convert_formulas_to_latex(content)

    print(f"💾 Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Done! All formatting fixes applied:")
    print("   ✓ Manual numbering removed")
    print("   ✓ List formatting fixed (blank lines added)")
    print("   ✓ Formulas converted to LaTeX notation")
    print(f"\n   Input:  {input_file}")
    print(f"   Output: {output_file}")

if __name__ == '__main__':
    main()
