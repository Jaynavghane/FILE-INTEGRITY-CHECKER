import hashlib
import os
import json

HASH_FILE = "file_hashes.json"

def calculate_hash(filepath):
    hash_algo = hashlib.sha256()
    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def monitor(folder_path):
    print(f"\nMonitoring folder: {folder_path}\n")
    old_hashes = load_hashes()
    new_hashes = {}
    for root, _, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_hash(filepath)
            new_hashes[filepath] = file_hash

            if filepath not in old_hashes:
                print(f"[NEW FILE]     {filepath}")
            elif old_hashes[filepath] != file_hash:
                print(f"[MODIFIED]     {filepath}")
            else:
                print(f"[UNCHANGED]    {filepath}")

    save_hashes(new_hashes)
    print("\nMonitoring complete.\n")

if __name__ == "__main__":
    folder = input("Enter folder path to monitor: ").strip()
    folder = folder.strip('"').strip("'")
    folder = os.path.expanduser(folder)

    if os.path.isdir(folder):
        monitor(folder)
    else:
        print("\n❌ ERROR: Invalid folder path!")
        print(r'Correct → "C:\Users\HP\OneDrive\Desktop\my folder"')
