import os
import glob
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine if this file is in the root or in Pages/
    is_root = (os.path.basename(os.path.dirname(os.path.abspath(file_path))) != 'Pages')

    # Mapping of known pages that exist in the Pages directory
    pages_dir_files = [os.path.basename(p) for p in glob.glob('Pages/*.html')]

    def repl_href(match):
        full_match = match.group(0)
        prefix = match.group(1) # href=" or href='
        link = match.group(2)
        suffix = match.group(3) # " or '

        if link.startswith('http') or link.startswith('#') or link.startswith('mailto:') or '{' in link:
            return full_match

        # Normalize Home.html to Home2.html if Home.html doesn't exist
        if link == 'Home.html' and 'Home.html' not in pages_dir_files and 'Home2.html' in pages_dir_files:
            link = 'Home2.html'

        if is_root:
            if link == 'index.html':
                 return full_match # Correct in root
            elif link in pages_dir_files:
                 return f'{prefix}Pages/{link}{suffix}'
            elif link.startswith('../'): # sometimes accidently added
                 pass # leaving as is
            # else maybe already has Pages/
        else:
            if link == 'index.html':
                return f'{prefix}../index.html{suffix}'
            elif link == '../index.html':
                return full_match # Correct
            elif link.startswith('Pages/'):
                return f'{prefix}{link[6:]}{suffix}'
            elif link in pages_dir_files:
                return full_match
        
        return f'{prefix}{link}{suffix}'

    # Replace href="..."
    new_content = re.sub(r'(href=["\'])(.*?)(["\'])', repl_href, content)

    # For index.html, fix window.location.href = 'Something.html'
    def repl_js_loc(match):
        prefix = match.group(1) # window.location.href = '
        link = match.group(2)
        suffix = match.group(3) # '
        if is_root:
            if link in pages_dir_files:
                return f'{prefix}Pages/{link}{suffix}'
        else:
             if link == 'index.html':
                 return f'{prefix}../index.html{suffix}'
        return match.group(0)

    new_content = re.sub(r'(window\.location\.href\s*=\s*["\'])(.*?)(["\'])', repl_js_loc, new_content)

    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed links in {file_path}")

def main():
    root_files = glob.glob('*.html')
    pages_files = glob.glob('Pages/*.html')
    for f in root_files + pages_files:
        process_file(f)

if __name__ == '__main__':
    main()
