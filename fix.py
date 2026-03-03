import os, glob

def fix():
    files = glob.glob('Pages/*.html')
    for f in files:
        with open(f, 'r', encoding='utf-8') as h:
            c = h.read()
        
        while '<script src="../assets/js/theme.js"></script>\n    <script src="../assets/js/theme.js"></script>' in c:
            c = c.replace('<script src="../assets/js/theme.js"></script>\n    <script src="../assets/js/theme.js"></script>', '<script src="../assets/js/theme.js"></script>')
        while '<script src="../assets/js/theme.js"></script>\n<script src="../assets/js/theme.js"></script>' in c:
            c = c.replace('<script src="../assets/js/theme.js"></script>\n<script src="../assets/js/theme.js"></script>', '<script src="../assets/js/theme.js"></script>')
        while '<script src="../assets/js/theme.js"></script><script src="../assets/js/theme.js"></script>' in c:
            c = c.replace('<script src="../assets/js/theme.js"></script><script src="../assets/js/theme.js"></script>', '<script src="../assets/js/theme.js"></script>')
            
        with open(f, 'w', encoding='utf-8') as h:
            h.write(c)
        print("Fixed", f)

if __name__ == "__main__":
    fix()
