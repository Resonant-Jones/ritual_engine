import os
import re

# Define replacements
replacements = {
    r'\bnpcpy\b': 'ritual_engine',
    r'\bNPC\b': 'Guardian'
}

# Define file extensions to target
allowed_ext = ['.py']

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for pattern, repl in replacements.items():
        content = re.sub(pattern, repl, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"🔁 Rewritten: {filepath}")

def process_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in allowed_ext):
                replace_in_file(os.path.join(root, file))

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    process_dir(root_dir)
