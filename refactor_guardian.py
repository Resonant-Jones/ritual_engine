import os

REPLACEMENTS = {
    "npcpy": "ritual_engine",
    "NPC": "Guardian"
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old, new in REPLACEMENTS.items():
            content = content.replace(old, new)
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Skipped: {filepath} ({e})")

def sweep_directory(root="."):
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith((".py", ".md", ".txt", ".json", ".yaml", ".yml")):
                replace_in_file(os.path.join(dirpath, file))

if __name__ == "__main__":
    sweep_directory("ritual_engine")