import os

base_dir = '.'  # Directory containing your HTML files

icon_link = '  <link rel="icon" href="pics\\ebook (1).png" type="image/x-icon">\n'


def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # Flags to know if we're inside the <head> tags
    in_head = False
    icon_added = False

    new_content = []
    for line in content:
        # Start of head tag
        if '<head>' in line:
            in_head = True
            new_content.append(line)
            continue

        # End of head tag
        if '</head>' in line:
            in_head = False

        if in_head:
            # Remove duplicate or whitespace lines
            if line.strip() in ['', icon_link.strip()] or line.count('ebook (1).png'):
                continue
            if not icon_added and '<link rel="stylesheet"' in line:
                new_content.append(icon_link)
                icon_added = True
        new_content.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_content)


for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            fix_html_file(filepath)

print("HTML files cleaned up!")

