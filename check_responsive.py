import os
import glob
import re

def check_media_queries(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    
    queries = set()
    for style in styles:
        matches = re.findall(r'@media\s*\([^\{]+\)', style)
        for m in matches:
            queries.add(m.strip())
            
    return queries

def main():
    pages = glob.glob('Pages/*.html') + ['index.html']
    
    with open('responsive_report.txt', 'w', encoding='utf-8') as out:
        out.write("Media Queries Used Per File:\n")
        out.write("-" * 40 + "\n")
        
        all_queries = set()
        file_queries_map = {}
        
        for page in pages:
            queries = check_media_queries(page)
            file_queries_map[page] = queries
            all_queries.update(queries)
            
        for page, queries in file_queries_map.items():
            if not queries:
                out.write(f"{os.path.basename(page)}: NONE\n")
            else:
                out.write(f"{os.path.basename(page)}:\n")
                for q in sorted(list(queries)):
                    out.write(f"  - {q}\n")
                    
        out.write("\nAll Unique Breakpoints Found Across Project:\n")
        out.write("-" * 40 + "\n")
        for q in sorted(list(all_queries)):
            out.write(f"  - {q}\n")

if __name__ == "__main__":
    main()
