import os
import re

base_dir = r"e:\websitengo\NGO\Pages"
admin_template_path = os.path.join(base_dir, "AdminDashboard.html")

with open(admin_template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

pages_config = [
    ("Dashboard", "AdminDashboard.html", "layout-dashboard", "Platform Overview", "Control, monitor, and improve platform productivity."),
    ("Manage Users", "AdminUsers.html", "users", "Manage Users", "View, search, filter, and manage all registered users."),
    ("Training Programs", "AdminTraining.html", "book-open", "Training Programs", "Create, edit, and organize conflict resolution courses."),
    ("Resources Hub", "AdminResources.html", "folder", "Resources Hub", "Upload and categorize toolkits, articles, and guides."),
    ("Community", "AdminCommunity.html", "message-square", "Community Moderation", "Moderate discussions, pin topics, and track engagement."),
    ("Certificates", "AdminCertificates.html", "award", "Certificates", "Generate, verify, and track user training certificates."),
    ("Impact Tracking", "AdminImpact.html", "globe", "Impact Tracking", "Analyze platform reach, success stories, and global footprint."),
    ("Notifications", "AdminNotifications.html", "bell", "Notifications", "Send platform updates and email announcements to users."),
    ("Reports & Analytics", "AdminReports.html", "pie-chart", "Reports & Analytics", "View detailed data on user activity and training completion."),
    ("Feedback & Support", "AdminFeedback.html", "headphones", "Feedback & Support", "Respond to support requests and view user feedback."),
    ("Content Management", "AdminContent.html", "file-text", "Content Management", "Update banners, testimonials, and FAQs."),
    ("Settings", "AdminSettings.html", "settings", "Settings", "Configure platform roles, profile settings, and general preferences.")
]

# Step 1: Replace sidebar links in the html_content
# We need to find the sidebar section and replace it with the new properly linked one.
# We'll use regex to isolate the sidebar and rewrite it.

sidebar_match = re.search(r'<div class="nav-items">(.*?)<a\s+href="index\.html"\s+class="nav-btn"\s+style="color', html_content, re.DOTALL)
if not sidebar_match:
    print("Could not find sidebar nav items.")
    exit(1)

original_nav_items = sidebar_match.group(1)

# Generate new nav items structure
new_nav_items = ""
for name, link, icon, title, desc in pages_config:
    if name == "Notifications":
        # special badge handling
        new_nav_items += f'''
            <a href="{link}" class="nav-btn" data-page="{name}">
              <i data-lucide="{icon}"></i>
              <span>{name}
                <span class="badge" style="background: #ef4444; color: white; border-radius: 50%; font-size: 0.65rem; padding: 2px 6px; position: absolute; right: 15px; top: 10px;">2</span>
              </span>
            </a>'''
    else:
        new_nav_items += f'''
            <a href="{link}" class="nav-btn" data-page="{name}">
              <i data-lucide="{icon}"></i> <span>{name}</span>
            </a>'''

# Replace the original nav items
html_content = html_content.replace(original_nav_items, new_nav_items)

# Now html_content has the updated sidebar with correct hrefs, but NO active class.
# Let's save a copy of this Base HTML to use for all pages.
base_html = html_content

# We also need a function to replace the main content and set the active class
def generate_page(name, filename, title, desc):
    page_html = base_html
    
    # Set the active class in sidebar
    target_link = f'data-page="{name}"'
    active_link = f'data-page="{name}" class="active"'
    page_html = page_html.replace(target_link, target_link + ' class="active"')
    
    # Change the document title
    page_html = re.sub(r'<title>.*?</title>', f'<title>{title} - Admin - NGO Training</title>', page_html)
    
    # Change the header title
    page_html = re.sub(r'<h2>.*?<span class="admin-badge">Admin</span></h2>', f'<h2>{title} <span class="admin-badge">Admin</span></h2>', page_html)
    
    # Change header desc
    page_html = re.sub(r'<p>Control, monitor, and improve platform productivity.</p>', f'<p>{desc}</p>', page_html)
    
    # For sub-pages (not Dashboard), replace the <div class="bento-scroll"> contents
    if filename != "AdminDashboard.html":
        # Replace the entire bento-grid contents with a generic message
        grid_pattern = r'<div class="bento-grid">.*?</div>\n        </div>\n      </main>'
        replacement = f'''<div class="bento-grid">
            <div class="bento-card bento-hero" style="grid-column: span 4;">
              <h3 class="hero-title">
                {title} <span>Module</span>
              </h3>
              <p class="hero-desc">
                {desc}
              </p>
              <div style="margin-top: 20px;">
                <p style="color: var(--muted); font-style: italic;">This section is currently being integrated. Check back soon for full functionality.</p>
              </div>
            </div>
          </div>
        </div>
      </main>'''
        page_html = re.sub(grid_pattern, replacement, page_html, flags=re.DOTALL)
    
    # Write the file
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as out:
        out.write(page_html)
        
    print(f"Generated {filename}")

for name, link, icon, title, desc in pages_config:
    generate_page(name, link, title, desc)

print("All admin pages generated successfully.")
