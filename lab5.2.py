import re


file_path = "task2.html"

pattern_img_src = r'<img\s+[^>]*src=["\']([^"\']+)["\']'

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

image_links = re.findall(pattern_img_src, content)  

print("all image links:")
for links in image_links:
    print(f"- {links}")

