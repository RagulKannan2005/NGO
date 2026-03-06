import glob
import os

html_files = glob.glob('Pages/*.html') + ['index.html']
missing = []

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # We are checking if the string 'index.html' appears anywhere in the file.
            # Even better, checking for href="...index.html" or similar.
            if 'index.html' not in content:
                missing.append(f)
    except Exception as e:
        print(f"Error reading {f}: {e}")

print("Pages without any reference to 'index.html':")
if not missing:
    print("None. All pages have a reference to index.html.")
else:
    for m in missing:
        print("- " + m)
