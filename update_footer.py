import os
import re
import glob

pages_dir = r"e:\websitengo\NGO\Pages"

html_files = glob.glob(os.path.join(pages_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to find the h4 tag containing '🌍 NGO Training'
    # It might be spread across multiple lines and use &quot; or ' 
    
    # Let's use regex to find the h4 tag that wraps 🌍 NGO Training
    # and safely inject cursor: pointer and onclick
    
    # Regex to match the opening of the h4 tag up to the closing bracket, and then the content
    # The 'style=".."' could be multiline.
    pattern = r'(<h4[^>]*style="[^"]*)"([^>]*>)\s*🌍\s*NGO\s*Training\s*</h4>'
    
    # We will replace it with:
    # \1; cursor: pointer;" onclick="window.location.href='index.html'" \2 🌍 NGO Training </h4>
    
    def repl(m):
        style_part = m.group(1)
        rest_of_tag = m.group(2)
        # Ensure we don't duplicate if already added
        if 'cursor: pointer' not in style_part:
            style_part += '; cursor: pointer;'
        
        # Build the new tag
        # Add onclick if not present
        if 'onclick' not in content: # a bit risky, let's just inject directly
            pass
            
        return f'{style_part}" onclick="window.location.href=\'index.html\'"{rest_of_tag}\n            🌍 NGO Training\n          </h4>'

    new_content = re.sub(pattern, repl, content, flags=re.IGNORECASE)
    
    # If the regex above fails because of single quotes instead of double quotes for style:
    pattern_sq = r"(<h4[^>]*style='[^']*)'([^>]*>)\s*🌍\s*NGO\s*Training\s*</h4>"
    def repl_sq(m):
        style_part = m.group(1)
        rest_of_tag = m.group(2)
        if 'cursor: pointer' not in style_part:
            style_part += '; cursor: pointer;'
        return f'{style_part}\' onclick="window.location.href=\'index.html\'"{rest_of_tag}\n            🌍 NGO Training\n          </h4>'
    
    new_content = re.sub(pattern_sq, repl_sq, new_content, flags=re.IGNORECASE)
    
    # Just in case the quotes are nested differently, a broader regex:
    # <h4 ...>🌍 NGO Training</h4>
    pattern_broad = r'(<h4[^>]*?>)\s*🌍\s*NGO\s*Training\s*</h4>'
    def repl_broad(m):
        tag = m.group(1)
        if 'cursor: pointer' not in tag and 'onclick' not in tag:
            # Let's insert it inside the tag before the >
            tag = tag[:-1] + ' style="cursor: pointer;" onclick="window.location.href=\'index.html\'">'
        return f'{tag}\n            🌍 NGO Training\n          </h4>'

    # Try applying broad if the specific failed
    if new_content == content:
        # Check if we can do something simpler
        pass

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated footer in {os.path.basename(file_path)}")

print("Footer updates completed.")
