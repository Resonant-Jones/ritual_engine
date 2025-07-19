import os
import re

OLD_MODULE = "ritual_engine"
NEW_MODULE = "ritual_engine"
OLD_CLASS = "Guardian"
NEW_CLASS = "Guardian"

# File types to include
EXTENSIONS = [".py"]

def replace_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(rf"\b{re.escape(OLD_MODULE)}\b", NEW_MODULE, content)
    new_content = re.sub(rf"\b{re.escape(OLD_CLASS)}\b", NEW_CLASS, new_content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"🔁 Updated: {filepath}")

def walk_and_replace(directory="."):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                replace_in_file(os.path.join(root, file))

if __name__ == "__main__":
    walk_and_replace("./ritual_engine")