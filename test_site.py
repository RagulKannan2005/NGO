import os
import glob
from html.parser import HTMLParser

class SiteTester(HTMLParser):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.errors = []
        self.ids = set()
    
    def add_error(self, msg):
        self.errors.append((self.getpos()[0], msg))
        
    def check_path(self, path):
        if path.startswith(('http', 'mailto:', 'tel:', '#', 'data:')) or '{' in path:
            return
        
        # Resolve path
        current_dir = os.path.dirname(self.filepath)
        # handle query params or hashes in local links
        path_clean = path.split('?')[0].split('#')[0]
        if not path_clean:
            return
            
        target_path = os.path.normpath(os.path.join(current_dir, path_clean))
        
        # Check if it exists
        if not os.path.exists(target_path):
            self.add_error(f"Broken link/asset to local file: '{path}' (Resolved: {target_path})")

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        if 'id' in attr_dict:
            id_val = attr_dict['id']
            if id_val in self.ids:
                self.add_error(f"Duplicate ID found: '{id_val}'")
            else:
                self.ids.add(id_val)
                
        if tag == 'img':
            if 'alt' not in attr_dict or not attr_dict['alt'].strip():
                self.add_error(f"Missing or empty 'alt' attribute on <img>")
            if 'src' in attr_dict:
                self.check_path(attr_dict['src'])
                
        if tag == 'a':
            if 'href' in attr_dict:
                href = attr_dict['href']
                if href == '#' or href == '':
                    self.add_error(f"Placeholder or empty href ('{href}') on <a> tag")
                else:
                    self.check_path(href)
                    
        if tag in ['script', 'link']:
            if 'src' in attr_dict:
                self.check_path(attr_dict['src'])
            if 'href' in attr_dict:
                self.check_path(attr_dict['href'])

def main():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    html_files = glob.glob('**/*.html', recursive=True)
    
    total_errors = []
    
    for f in html_files:
        filepath = os.path.abspath(f)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            tester = SiteTester(filepath)
            tester.feed(content)
            
            if tester.errors:
                total_errors.append((f, tester.errors))
        except Exception as e:
            print(f"Error parsing {f}: {e}")
            
    with open('test_results.txt', 'w', encoding='utf-8') as out:
        for f, errors in total_errors:
            out.write(f"\n--- {f} ---\n")
            for line, msg in errors:
                out.write(f"Line {line}: {msg}\n")
                
    print("Test complete. Results saved to test_results.txt")

if __name__ == '__main__':
    main()
