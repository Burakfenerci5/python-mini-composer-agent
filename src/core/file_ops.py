import os

def read_file(filepath):
    """Reads the content of a target file."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return f.read()

def write_file(filepath, content):
    """Writes new content to the file (The 'Apply' step)."""
    with open(filepath, "w") as f:
        f.write(content)
    print(f"💾 Saved changes to: {filepath}")

def list_files(directory):
    """Lists files in the playground so the agent knows what exists."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files