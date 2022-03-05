

import os
import re
import sys

def get_abs_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    else:
        return os.path.realpath(path)

def rename_in_dirs(dir_path: str):
    # rename recursively in folders
    for dir in os.listdir(dir_path):
        full_dir = os.path.join(dir_path, dir)

        if os.path.isfile(full_dir):
            file_ext = re.search('(?<=index).*[\w+]', dir)
            parent_dir = dir_path.split('\\')[-1]

            if (file_ext):
                # rename index to folder name
                print(f'Renaming {dir} to {parent_dir}{file_ext[0]}')
        else:
            rename_in_dirs(full_dir)

    

def main():
    args = sys.argv[1:]
    dir_path = get_abs_path(args[0])

    rename_in_dirs(dir_path)
    

if (__name__ == '__main__'):
    main()