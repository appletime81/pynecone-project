import os


def delete_pycache():
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            if dir == "__pycache__":
                os.system(f"rm -rf {os.path.join(root, dir)}")
                print(f"rm -rf {os.path.join(root, dir)}")


if __name__ == "__main__":
    delete_pycache()
