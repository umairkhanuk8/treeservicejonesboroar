# Multi-Page Local Service Business Website Template

Welcome to the **Universal Multi-Page Website Design Template** built with clean HTML5, modern Vanilla CSS (with design tokens/variables), and lightweight vanilla JavaScript.

This template is designed specifically for local service businesses (e.g., Tree Service, Plumbing, Roofing, HVAC, Landscaping, Cleaning, Auto Repair, etc.).

---

## 📁 Directory Structure

```text
website-template/
│
├── index.html            # Homepage Template
├── about.html            # About Us Page Template
├── contact.html          # Contact Us & Free Estimate Page Template
├── services.html         # Main Services Hub Page Template
├── service-detail.html   # Individual Sub-Service Page Template
├── service-area.html     # Main Service Areas Hub Page Template
├── area-detail.html      # Individual Sub-Area/City Page Template
│
├── css/
│   ├── styles.css        # Core Design System, Variables, Reset, & Global Layouts
│   ├── service-page.css  # Specialized Layouts for Sub-Service Detail Pages
│   └── area-page.css     # Specialized Layouts for Sub-Area/City Pages
│
├── js/
│   └── script.js         # Navigation, Sticky Header, Mobile Drawer, Accordion & Animations
│
└── README.md             # Customization & Usage Documentation
```

---

## 🛠️ Easy Customization Guide (Placeholder Mapping)

Search and replace the following placeholder variables across all `.html` files in your project editor (VS Code, Notepad++, etc.):

| Placeholder Variable | Example Replacement | Description |
| :--- | :--- | :--- |
| `{{COMPANY_NAME}}` | `Apex Plumbing Solutions` | Your Business / Company Name |
| `{{SERVICE_TYPE}}` | `Plumbing & Repair` | Your Core Industry / Service Category |
| `{{CITY_NAME}}` | `Atlanta` | Your Primary City / Headquarters City |
| `{{LOCATION_CITY}}` | `Marietta` | Specific Sub-Location / Neighboring City Name |
| `{{SERVICE_NAME}}` | `Drain Cleaning & Jetting` | Specific Sub-Service Name |
| `{{PHONE_NUMBER}}` | `(404) 555-0199` | Formatted Phone Number for display |
| `{{PHONE_NUMBER_RAW}}` | `+14045550199` | Raw phone number format for `tel:` links |
| `{{EMAIL_ADDRESS}}` | `info@apexplumbing.com` | Business Email Address |
| `{{DOMAIN_URL}}` | `apexplumbingatl.com` | Your Website Domain URL |

---

## 🎨 Changing Colors & Theme (CSS Variables)

Open `css/styles.css` and modify the `:root` variables at the top of the file:

```css
:root {
    --color-dark: #2d2e32;
    --color-primary-deep: #1a3c2a;    /* Main Header & Footer Dark Theme Color */
    --color-primary-accent: #2e7d4f;  /* Primary Brand Button & Accent Color */
    --color-gold: #c5a55a;            /* Highlight / Star / CTA Accent Color */
    --radius: 12px;                  /* Global Card Border Radius */
}
```

---

## ⚡ Features Included

1. **Fully Responsive Header & Mobile Menu**: Features interactive dropdown menus on desktop and a clean sliding drawer menu on mobile.
2. **Sticky Header**: Seamless header shadow transition when scrolling past 80px.
3. **Scroll Reveal Animations**: Smooth entry animations (`.reveal`, `.reveal-left`, `.reveal-right`) powered by lightweight `IntersectionObserver`.
4. **FAQ Accordions**: Interactive accordion widgets built-in for zero layout shift.
5. **SEO & Open Graph Meta Structure**: Pre-configured meta tags, canonical links, and semantic HTML5 hierarchy.

---

## 🇮🇳 / 🇵🇰 Roman Urdu Guide (Kaise Use Karein)

1. **Next Project ke liye Template setup**:
   - Is `website-template` folder ko copy karke apne naye project me paste karein.
2. **Details replace karein**:
   - Sab `.html` files me `{{COMPANY_NAME}}`, `{{CITY_NAME}}`, `{{PHONE_NUMBER}}` wagaira ko Apne naye client ki details se replace (Ctrl + Shift + H / Replace All) kar dein.
3. **Color Theme Change karein**:
   - `css/styles.css` file kholein aur top par `:root` variables (`--color-primary-deep`, `--color-primary-accent`, `--color-gold`) ko client ke brand colors ke mutabiq change kar lein.
4. **New Service ya Area Pages add karein**:
   - Service page ke liye `service-detail.html` ki copy banayein aur naya name rakhein (e.g., `drain-cleaning.html`).
   - Area page ke liye `area-detail.html` ki copy banayein aur naya name rakhein (e.g., `plumber-marietta-ga.html`).
