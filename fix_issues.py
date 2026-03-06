import os
import glob
import re

def fix_html_issues(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix missing alt attributes on <img>
    # Finds <img ...> that do not have an alt="..."
    def add_alt(match):
        img_tag = match.group(0)
        if 'alt=' not in img_tag.lower():
            # Insert alt="" before the closing >
            return img_tag[:-1] + ' alt="NGO Image">'
        return img_tag

    content = re.sub(r'<img\s+[^>]+>', add_alt, content, flags=re.IGNORECASE)

    # 2. Fix empty or hash hrefs (href="#" or href="")
    # Replace with href="javascript:void(0)"
    content = re.sub(r'href=["\']#["\']', 'href="javascript:void(0)"', content)
    content = re.sub(r'href=["\']["\']', 'href="javascript:void(0)"', content)

    # 3. Fix specific broken paths in Pages directory
    filename = os.path.basename(filepath)
    if filename == 'Home2.html':
        content = content.replace('href="Home.html"', 'href="Home2.html"')
    elif filename == 'UserDashboard.html':
        # Fix absolute paths /NGO/...
        content = content.replace('href="/NGO/index.html"', 'href="../index.html"')
        content = re.sub(r'href="/NGO/Pages/([^"]+)"', r'href="\1"', content)
        content = content.replace('href="Help.html"', 'href="Contact.html"') # Map Help to Contact
    elif filename == '404.html':
        content = content.replace('href="404.css"', 'href="../assets/css/app.css"')
    elif filename == 'Comingsoon.html':
        content = content.replace('href="coming-soon.css"', 'href="../assets/css/app.css"')
        content = content.replace('src="coming-soon.js"', '') # remove missing js

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed issues in {filepath}")

def main():
    pages = glob.glob('Pages/*.html')
    # add index.html too just in case
    html_files = ['index.html'] + pages

    for f in html_files:
        fix_html_issues(f)

if __name__ == '__main__':
    main()
