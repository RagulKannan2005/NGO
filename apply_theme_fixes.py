import os
import glob

# The blocking script to prevent theme flash
THEME_SCRIPT = """    <script>
      (function() {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark' || (!theme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      })();
    </script>"""

# Color replacements mapping
COLOR_MAP = {
    '#ef4444': 'var(--admin-danger)',
    '#10b981': 'var(--admin-success)',
    '#f59e0b': 'var(--admin-warning)',
    '#3b82f6': 'var(--admin-info)',
    '#8b5cf6': 'var(--admin-accent)',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Inject Theme Script in <head> if not already there
    if 'document.documentElement.classList.add(\'dark\')' not in content:
        # Insert before <title> or after <meta charset>
        if '<title>' in content:
            content = content.replace('<title>', f'{THEME_SCRIPT}\n    <title>', 1)
        elif '<meta charset' in content:
             content = content.replace('>', f'>\n{THEME_SCRIPT}', 1)

    # 2. Replace hardcoded colors
    for hex_code, var_name in COLOR_MAP.items():
        # Case insensitive replacement for hex codes
        # We look for hex codes followed by semi-colons or in style attributes
        content = content.replace(hex_code, var_name)
        content = content.replace(hex_code.upper(), var_name)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed: {filepath}")

def main():
    # Process all HTML files in Pages/ and its subdirectories
    html_files = glob.glob('Pages/**/*.html', recursive=True)
    for f in html_files:
        process_file(f)

if __name__ == "__main__":
    main()
