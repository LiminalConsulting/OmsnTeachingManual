#!/usr/bin/env python3
"""
Fix formatting issues in Physics-Chemistry manual:
1. Add blank lines before bullet/numbered lists for proper rendering
2. Convert code-block formulas to LaTeX math notation for beautiful rendering
"""

import re

def fix_element_lists(content):
    """
    Convert element electron configuration lists to proper markdown lists.

    Converts:
        **Exemplos (Z≤20):**

        1H – 1
        2He – 2
        3Li – 2,1
    To:
        **Exemplos (Z≤20):**

        - 1H – 1
        - 2He – 2
        - 3Li – 2,1
    """
    lines = content.split('\n')
    fixed_lines = []

    in_element_list = False

    for i, line in enumerate(lines):
        # Check if we're entering an element list section
        if 'Exemplos' in line and 'Z' in line:
            in_element_list = True
            fixed_lines.append(line)
            continue

        # Check if line matches element pattern: starts with digit, element symbol, dash
        # Pattern: 1H – 1  or  11Na – 2,8,1
        if in_element_list and re.match(r'^\d+[A-Z][a-z]?\s*–\s*', line.strip()):
            fixed_lines.append(f'- {line.strip()}')
            continue

        # Exit element list if we hit a non-element line that's not blank
        if in_element_list and line.strip() != '' and not re.match(r'^-?\s*\d+[A-Z][a-z]?\s*–', line.strip()):
            in_element_list = False

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

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
            # Check if already wrapped in $$, if so just return it
            if formula.startswith('$$') and formula.endswith('$$'):
                return formula
            return f'$${formula}$$'
        else:
            # Keep as code block if it doesn't look like a formula
            return match.group(0)

    # Disabled - causes $$$$
    # content = re.sub(pattern1, replace_code_block, content)

    # Pattern 2: Inline formulas after "Fórmula:" that aren't in code blocks
    # Matches: **Fórmula:** formula_with_math_symbols
    pattern2 = r'(\*\*Fórmula[^:]*:\*\*)\s+([^\n]+[=×÷±∆Δ][^\n]+)'

    def replace_inline_formula(match):
        label = match.group(1)
        formula = match.group(2).strip()
        # Convert to LaTeX
        formula = formula.replace('×', r' \times ')
        formula = formula.replace('÷', r' \div ')
        # Convert underscores to subscripts for variables like F_colisão
        formula = re.sub(r'([A-Za-z]+)_([A-Za-zção]+)', r'\1_{\2}', formula)
        return f'{label}\n\n$${formula}$$'

    content = re.sub(pattern2, replace_inline_formula, content)

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

    print("🔧 Converting element lists to markdown lists...")
    content = fix_element_lists(content)

    print("🔧 Fixing list formatting (adding blank lines)...")
    content = fix_list_formatting(content)

    print("🔧 Converting formulas to LaTeX notation...")
    content = convert_formulas_to_latex(content)

    print(f"💾 Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Done! All formatting fixes applied:")
    print("   ✓ Manual numbering removed")
    print("   ✓ Element lists converted to markdown lists")
    print("   ✓ List formatting fixed (blank lines added)")
    print("   ✓ Formulas converted to LaTeX notation")
    print(f"\n   Input:  {input_file}")
    print(f"   Output: {output_file}")

if __name__ == '__main__':
    main()
