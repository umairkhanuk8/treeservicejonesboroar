import os, re

BASE = r"d:\Projects\treeservicejonesboroar"
BLOG_DIR = os.path.join(BASE, "blog")

print("=== FINAL COMPLETE AUDIT ===\n")

# 1. All 11 blog files
print("1. BLOG FILES (11 expected):")
expected_blog = [
    "index.html", "tree-removal-cost-jonesboro-ar.html",
    "when-to-remove-vs-trim-damaged-tree.html", "storm-tree-problems-northeast-arkansas.html",
    "professional-tree-trimming-jonesboro-properties.html", "diy-tree-cutting-vs-hiring-arborist.html",
    "tree-falls-on-jonesboro-property.html", "stump-grinding-safety-appearance.html",
    "tree-care-older-homes-jonesboro.html", "commercial-tree-maintenance-jonesboro-businesses.html",
    "prepare-trees-severe-weather-arkansas.html",
]
all_ok = True
for f in expected_blog:
    path = os.path.join(BLOG_DIR, f)
    size = os.path.getsize(path) if os.path.exists(path) else 0
    ok = size > 5000
    if not ok:
        all_ok = False
    label = "OK" if ok else "FAIL"
    print("   " + label + " (" + str(size) + "B): " + f)
print("   Result: " + ("PASS" if all_ok else "FAIL"))

# 2. Blog nav in ALL main pages
print("\n2. BLOG NAV IN ALL MAIN PAGES:")
main_html = [f for f in os.listdir(BASE) if f.endswith(".html") and os.path.isfile(os.path.join(BASE, f))]
missing = []
for f in sorted(main_html):
    content = open(os.path.join(BASE, f), encoding="utf-8").read()
    if "blog/index.html" not in content and "blog/" not in content:
        missing.append(f)
if missing:
    print("   FAIL - Missing in: " + str(missing))
else:
    print("   PASS - All " + str(len(main_html)) + " main pages contain blog link")

# 3. Sitemap
print("\n3. SITEMAP (11 blog URLs expected):")
sitemap = open(os.path.join(BASE, "sitemap.xml"), encoding="utf-8").read()
blog_slugs = [
    "blog/index.html", "blog/tree-removal-cost-jonesboro-ar.html",
    "blog/when-to-remove-vs-trim-damaged-tree.html", "blog/storm-tree-problems-northeast-arkansas.html",
    "blog/professional-tree-trimming-jonesboro-properties.html", "blog/diy-tree-cutting-vs-hiring-arborist.html",
    "blog/tree-falls-on-jonesboro-property.html", "blog/stump-grinding-safety-appearance.html",
    "blog/tree-care-older-homes-jonesboro.html", "blog/commercial-tree-maintenance-jonesboro-businesses.html",
    "blog/prepare-trees-severe-weather-arkansas.html",
]
sm_ok = all(s in sitemap for s in blog_slugs)
print("   " + ("PASS" if sm_ok else "FAIL") + " - All 11 blog URLs in sitemap")

# 4. Images
print("\n4. BLOG IMAGES (10 expected):")
IMG_DIR = os.path.join(BASE, "images", "blog")
expected_images = [
    "tree-removal-cost-jonesboro-ar.png", "remove-vs-trim-damaged-tree.png",
    "storm-tree-problems-northeast-arkansas.png", "tree-trimming-protects-jonesboro-property.png",
    "diy-vs-professional-arborist.png", "tree-falls-on-jonesboro-property.png",
    "stump-grinding-safety-appearance.png", "tree-care-older-homes-jonesboro.png",
    "commercial-tree-maintenance-jonesboro.png", "prepare-trees-severe-weather-arkansas.png",
]
imgs_ok = all(os.path.exists(os.path.join(IMG_DIR, img)) for img in expected_images)
print("   " + ("PASS" if imgs_ok else "FAIL") + " - All 10 blog images present")

# 5. Forbidden keyword check
print("\n5. FORBIDDEN KEYWORD IN ARTICLE BODIES:")
forbidden = "tree service jonesboro ar"
blog_posts = [f for f in os.listdir(BLOG_DIR) if f.endswith(".html") and f != "index.html"]
violations = []
for f in blog_posts:
    content = open(os.path.join(BLOG_DIR, f), encoding="utf-8").read().lower()
    match = re.search(r'<main class="article-body">(.*?)</main>', content, re.DOTALL)
    if match and forbidden in match.group(1):
        violations.append(f)
kw_ok = len(violations) == 0
print("   " + ("PASS" if kw_ok else "FAIL - VIOLATIONS: " + str(violations)))

# 6. Internal service links
print("\n6. INTERNAL SERVICE LINKS IN BLOG POSTS:")
service_pages = [
    "tree-removal-jonesboro-ar", "tree-trimming-jonesboro-ar", "tree-pruning-jonesboro-ar",
    "stump-grinding-jonesboro-ar", "emergency-tree-service-jonesboro-ar",
    "storm-damage-tree-cleanup-jonesboro-ar", "land-clearing-jonesboro-ar",
    "commercial-tree-service-jonesboro-ar"
]
link_ok = True
for f in blog_posts:
    content = open(os.path.join(BLOG_DIR, f), encoding="utf-8").read()
    links = sum(1 for sp in service_pages if sp in content)
    if links < 2:
        link_ok = False
        print("   WARN: " + f + " has only " + str(links) + " service links")
if link_ok:
    print("   PASS - All " + str(len(blog_posts)) + " posts link to 2+ service pages")

# 7. Check interlinking between blog posts
print("\n7. CROSS-POST INTERNAL LINKS:")
all_slugs = [f for f in os.listdir(BLOG_DIR) if f.endswith(".html") and f != "index.html"]
cross_ok = True
for f in blog_posts:
    content = open(os.path.join(BLOG_DIR, f), encoding="utf-8").read()
    other_posts = [s for s in all_slugs if s != f]
    cross_links = sum(1 for s in other_posts if s in content)
    if cross_links < 3:
        cross_ok = False
        print("   WARN: " + f + " has only " + str(cross_links) + " cross-post links")
if cross_ok:
    print("   PASS - All posts cross-link to 3+ other blog posts")

print("\n=== AUDIT SUMMARY ===")
all_pass = all_ok and not missing and sm_ok and imgs_ok and kw_ok and link_ok and cross_ok
print("Overall: " + ("ALL PASS" if all_pass else "SOME ISSUES - review above"))
