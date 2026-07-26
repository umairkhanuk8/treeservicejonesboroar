"""
add_blog_nav.py
Adds a Blog nav link to all main site HTML pages (not the blog/ subdirectory).
Inserts <a href="blog/index.html">Blog</a> before the Contact link in desktop nav,
and before </div> closing the mobile-menu Contact link.
"""
import os, re

BASE = r"d:\Projects\treeservicejonesboroar"

# Get all HTML files in root only (not blog/ subdirectory)
html_files = [
    f for f in os.listdir(BASE)
    if f.endswith('.html') and os.path.isfile(os.path.join(BASE, f))
]

print(f"Found {len(html_files)} HTML files in root directory")

updated = 0
skipped = 0

for fname in sorted(html_files):
    fpath = os.path.join(BASE, fname)
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has blog nav link
    if 'href="blog/index.html"' in content or 'href="blog/"' in content:
        print(f"SKIP (already has Blog link): {fname}")
        skipped += 1
        continue
    
    # Check if this page has the nav structure we expect
    if '<a href="contact.html">Contact</a>' not in content:
        print(f"SKIP (no contact link found): {fname}")
        skipped += 1
        continue
    
    original = content
    
    # 1. Add Blog link in desktop nav - insert before Contact link
    # Pattern: <a href="contact.html">Contact</a>
    desktop_pattern = '<a href="contact.html">Contact</a>\n                </nav>'
    desktop_replacement = '<a href="blog/index.html">Blog</a>\n                    <a href="contact.html">Contact</a>\n                </nav>'
    
    if desktop_pattern in content:
        content = content.replace(desktop_pattern, desktop_replacement, 1)
    else:
        # Try alternative whitespace
        alt_pattern = '<a href="contact.html">Contact</a>'
        if alt_pattern in content:
            # Only replace the first occurrence (desktop nav)
            content = content.replace(alt_pattern, '<a href="blog/index.html">Blog</a>\n                    <a href="contact.html">Contact</a>', 1)
    
    # 2. Add Blog link in mobile menu - find mobile contact link and insert before it
    # Mobile pattern: <a href="contact.html">Contact</a> inside mobile-menu div
    mobile_pattern = '        <a href="contact.html">Contact</a>'
    mobile_replacement = '        <a href="blog/index.html">Blog</a>\n        <a href="contact.html">Contact</a>'
    
    if mobile_pattern in content:
        # Replace last remaining occurrence (mobile menu), leaving desktop already handled
        # Count occurrences
        count = content.count(mobile_pattern)
        if count >= 1:
            # Find position of last occurrence
            last_pos = content.rfind(mobile_pattern)
            content = content[:last_pos] + mobile_replacement + content[last_pos + len(mobile_pattern):]
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED: {fname}")
        updated += 1
    else:
        print(f"NO CHANGE: {fname}")
        skipped += 1

print(f"\nDone. Updated: {updated}, Skipped: {skipped}")
