import os
import re

# Use relative or absolute Windows paths
admin_dir = r"Pages\Adminpages"
root_admin_file = r"Pages\AdminDashboard.html"

# Get absolute paths to be safe
base_path = r"e:\websitengo\NGO"
admin_dir_abs = os.path.join(base_path, admin_dir)
root_admin_file_abs = os.path.join(base_path, root_admin_file)

if not os.path.exists(admin_dir_abs):
    print(f"Error: {admin_dir_abs} not found")
    exit(1)

files = [os.path.join(admin_dir_abs, f) for f in os.listdir(admin_dir_abs) if f.endswith(".html")]
files.append(root_admin_file_abs)

def fix_content(content):
    # 1. Physical to Logical for badges
    content = content.replace('right: 15px', 'inset-inline-end: 15px')
    # 2. Sidebar hover margin
    content = content.replace('margin-left: 24px', 'margin-inline-start: 24px')
    # 3. Duplicate class fix
    # e.g., class="nav-btn" data-page="..." class="active"
    content = re.sub(r'class="nav-btn"\s+data-page="([^"]*)"\s+class="active"', r'class="nav-btn active" data-page="\1"', content)
    content = re.sub(r'class="active"\s+data-page="([^"]*)"\s+class="nav-btn"', r'class="nav-btn active" data-page="\1"', content)
    
    # 4. Correct relative paths in sidebar for admin sub-pages
    # If a page is inside Adminpages, it shouldn't have href="Adminpages/..."
    # But AdminDashboard.html (in Pages/) IS correct to have href="Adminpages/..."
    
    return content

for path in files:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Specific logic for sub-pages: if they contain Adminpages/Admin*.html, change to current dir
        if "Adminpages" in path and "AdminDashboard.html" not in path:
            content = content.replace('href="Adminpages/', 'href="')
            
        new_content = fix_content(content)
        
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {os.path.basename(path)}")
        else:
            print(f"Skipped: {os.path.basename(path)} (No changes needed)")
    except Exception as e:
        print(f"Error processing {os.path.basename(path)}: {e}")
