import re

# Local images to cycle through
local_images = [
    "./custom_packaging.png",
    "./custom_molded_interior.png",
    "./skincare_packaging.jpeg",
    "./user_experience.jpg",
    "./watch_packaging.png"
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update body margin for full width
    body_css_old = "    body {\n      font-family: 'Assistant', sans-serif;\n      background: #fff;\n      color: #252729;\n      font-size: 16px;\n      line-height: 1.6;\n      overflow-x: hidden;\n    }"
    body_css_new = "    body {\n      font-family: 'Assistant', sans-serif;\n      background: #fff;\n      color: #252729;\n      font-size: 16px;\n      line-height: 1.6;\n      overflow-x: hidden;\n      margin: 0;\n      padding: 0;\n    }"
    content = content.replace(body_css_old, body_css_new)
    
    # Alternatively, just in case the format differs slightly:
    content = re.sub(r'body\s*\{[^}]*overflow-x:\s*hidden;', r'\g<0>\n      margin: 0;\n      padding: 0;', content)

    # 2. Replace all mushroompackaging.com image URLs
    # We will find all unique URLs first
    urls = re.findall(r'https://mushroompackaging\.com/cdn/shop/files/[^\s"\'<>]*', content)
    unique_urls = list(set(urls))
    
    for i, url in enumerate(unique_urls):
        local_img = local_images[i % len(local_images)]
        content = content.replace(url, local_img)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('mushroombiopackaging.html')

print("Replaced all external mushroompackaging URLs and updated body margin.")
