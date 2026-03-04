import os
import glob

admin_pages_dir = r"e:\websitengo\NGO\Pages\Adminpages"

html_files = glob.glob(os.path.join(admin_pages_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace incorrect script paths
    new_content = content.replace('src="../assets/js/theme.js"', 'src="../../assets/js/theme.js"')
    new_content = new_content.replace('href="../assets/', 'href="../../assets/')
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed paths in {os.path.basename(file_path)}")

print("Done fixing paths.")
