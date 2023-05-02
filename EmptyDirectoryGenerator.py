import os

#Ask ChatGPT to create a file directory of the software you're creating then use this Empty File and Directory Generator to create the directory
#Then ask ChatGPT to create the contents of each file 
#then troubleshoot with ChatGPT
#This script will strip the leading spaces from directory and file names and only remove the leading dash (-) if it's used for indentation. The dashes within file and directory names will be preserved. Make sure your directory_tree.txt file has the correct structure, and then run the script. It should create the directories and files as expected.

def create_directories(directories):
    for directory in directories:
        clean_dir = directory.strip()
        if not clean_dir:
            continue
        if clean_dir.startswith("-"):
            full_path = os.path.join("project", clean_dir.lstrip("-")).rstrip()
            with open(full_path, "w") as f:
                pass
        else:
            full_path = os.path.join("project", clean_dir).rstrip()
            os.makedirs(full_path, exist_ok=True)

with open("directory_tree.txt", "r") as file:
    directories = file.readlines()

os.makedirs("project", exist_ok=True)
create_directories(directories)
