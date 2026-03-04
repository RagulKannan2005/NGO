import os
import re

# Standard Footer HTML
FOOTER_TEMPLATE = """
    <!-- FOOTER -->
    <footer class="footer">
      <div class="footer-grid">
        <div class="footer-col">
          <h4 style="color: var(--primary); font-size: 1.5rem; margin-bottom: 1rem; font-family: 'Outfit', sans-serif;">🌍 NGO Training</h4>
          <p>
            Empowering individuals and organizations with conflict resolution skills for a more peaceful world. Our platform provides high-quality, accessible training for everyone.
          </p>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="{prefix}index.html">Home</a></li>
            <li><a href="{prefix}TrainingPage.html">Programs</a></li>
            <li><a href="{prefix}Impact.html">Our Impact</a></li>
            <li><a href="{prefix}Community.html">Community</a></li>
            <li><a href="{prefix}404.html">404 Page</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="{prefix}Contact.html">Help Center</a></li>
            <li><a href="{prefix}wishlist.html">Wishlist</a></li>
            <li><a href="{prefix}Settings.html">Settings</a></li>
            <li><a href="{prefix}login.html">Login / Register</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Follow Us</h4>
          <p style="margin-bottom: 1.5rem;">Join our community on social media to stay updated.</p>
          <div class="social-links">
            <a href="#"><i data-lucide="facebook"></i></a>
            <a href="#"><i data-lucide="twitter"></i></a>
            <a href="#"><i data-lucide="instagram"></i></a>
            <a href="#"><i data-lucide="linkedin"></i></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> NGO Training Platform. All rights reserved.</p>
        <div class="footer-legal">
          <a href="#" style="color: var(--muted); text-decoration: none; margin-left: 20px;">Privacy Policy</a>
          <a href="#" style="color: var(--muted); text-decoration: none; margin-left: 20px;">Terms of Service</a>
        </div>
      </div>
    </footer>
"""

PAGES_DIR = r"e:\websitengo\NGO\Pages"

def get_footer_for_file(filepath):
    # Determine the prefix based on nesting
    rel_path = os.path.relpath(filepath, PAGES_DIR)
    # depth counts how many subdirs deep from Pages
    depth = rel_path.count(os.sep)
    prefix = "../" * depth
    return FOOTER_TEMPLATE.format(prefix=prefix)

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. CLEANUP
        # Remove any existing footer markers (old or new)
        content = re.sub(r'<!--\s*FOOTER\s*-->', '', content, flags=re.IGNORECASE)
        # Remove any existing footer tag
        content = re.sub(r'<footer\b[^>]*>.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)

        footer_to_inject = get_footer_for_file(filepath)

        # 2. INJECTION LOGIC
        # Case A: Admin Dashboards (Inject inside bento-scroll container)
        if '<div class="bento-scroll">' in content:
            # Look for the last </div> before the close of main content
            # Most admin pages follow a specific template from make_admin_pages.py
            # </div> <!-- End bento-grid -->
            # </div> <!-- End bento-scroll -->
            # </main>
            if '</div>\n        </div>\n      </main>' in content:
                 content = content.replace('</div>\n        </div>\n      </main>', footer_to_inject + '\n        </div>\n      </main>', 1)
            elif '</div>\n      </main>' in content:
                 content = content.replace('</div>\n      </main>', footer_to_inject + '\n      </main>', 1)
            else:
                 content = re.sub(r'(</body>)', footer_to_inject + r'\n  \1', content, count=1, flags=re.IGNORECASE)
        else:
            # Case B: Regular pages (Inject before scripts or </body>)
            # Find the position where the body content ends or scripts begin
            # We want to inject BEFORE the first script which is NOT in head
            parts = re.split(r'(<body)', content, maxsplit=1, flags=re.IGNORECASE)
            if len(parts) > 1:
                pre_body = parts[0] + parts[1]
                body_rest = parts[2]
                
                # In body_rest, find the first script tag
                # But wait, common templates put scripts at the VERY bottom.
                # Let's find the LAST </section> or major block and inject after it.
                # Actually, let's just use </body> but make it robust.
                if '</body>' in content or '</BODY>' in content:
                     content = re.sub(r'(</body>)', footer_to_inject + r'\n  \1', content, count=1, flags=re.IGNORECASE)
                else:
                     content = content + footer_to_inject

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed: {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def run():
    for root, dirs, files in os.walk(PAGES_DIR):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    run()
