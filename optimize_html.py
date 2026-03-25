import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Reduce massive background blurs on mobile
html = html.replace('blur-[120px]', 'md:blur-[120px] blur-[60px]')
html = html.replace('blur-[100px]', 'md:blur-[100px] blur-[50px]')

# 2. Downgrade backdrop-blur to save GPU
html = html.replace('backdrop-blur-xl', 'backdrop-blur-sm')
html = html.replace('backdrop-blur-lg', 'backdrop-blur-sm')

# 3. Remove mix-blend-screen to avoid heavy composite painting
html = html.replace(' mix-blend-screen', '')

# 4. Add loading="lazy" and decoding="async" to images (excluding logo to keep LCP fast)
def lazy_img(match):
    img_tag = match.group(0)
    if 'loading=' not in img_tag and 'logo' not in img_tag.lower():
        # Insert before closing bracket
        return img_tag[:-1] + ' loading="lazy" decoding="async">'
    return img_tag

html = re.sub(r'<img [^>]+>', lazy_img, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML optimizations applied.")
