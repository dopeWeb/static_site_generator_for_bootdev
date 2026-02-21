import os
import shutil
from textnode import TextNode, TextType

public_path = "/root/Python_Projects/static_site_generator/public"
static_path = "/root/Python_Projects/static_site_generator/static"

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    if os.path.exists(public_path):
        contents = os.listdir(public_path)
        if contents:
            for filename in contents:
                file_path = os.path.join(public_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.remove(file_path)
                        print(f"Deleted file: {filename}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"Deleted directory and its content: {filename}")
                except Exception as e:
                    print(f"Error occurred while deleting {file_path}: {e}")
        else:
            print("Directory is already empty.")
    else:
        print("Directory does not exist, creating it during copy.")

    try:
        shutil.copytree(static_path, public_path, dirs_exist_ok=True)
        print(f"Successfully copied from {static_path} to {public_path}")
    except Exception as e:
        print(f"Error occurred while copying: {e}")

if __name__ == "__main__":
    main()