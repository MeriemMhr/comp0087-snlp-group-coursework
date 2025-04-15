import os
import json

def clean_metadata(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)

        if "cells" not in nb:
            raise ValueError("Missing 'cells' in notebook.")

        # Clean metadata at notebook level
        nb["metadata"] = nb.get("metadata", {})

        # Clean metadata in each cell
        for cell in nb.get("cells", []):
            cell["metadata"] = cell.get("metadata", {})

        # Clean metadata at notebook format level
        nb["nbformat"] = nb.get("nbformat", 4)
        nb["nbformat_minor"] = nb.get("nbformat_minor", 0)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=2)

        print(f"✅ Cleaned: {path}")
    except Exception as e:
        print(f"❌ Failed: {path} — {str(e)}")

def walk_and_clean():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".ipynb"):
                full_path = os.path.join(root, file)
                clean_metadata(full_path)

if __name__ == "__main__":
    walk_and_clean()
