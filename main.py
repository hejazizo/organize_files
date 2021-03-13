import os
from pathlib import Path

from tqdm import tqdm

from utils import extract_ext, move_file, create_dir
import sys

if len(sys.argv) < 2:
    raise IndexError("Input path not given!")

MAIN_PATH = Path(sys.argv[1])

ext_dest = {
    ".jpg": "image",
    ".png": "image",
    ".pdf": "doc",
    ".csv": "doc",
    ".mp4": "media",
    ".odt": "image",
    ".pem": "other",
    ".py": "code",
    ".txt": "doc",
    ".xlsm": "doc",
    ".zip": "other"
}

# finding unique extension in the main directory
unique_ext = extract_ext(MAIN_PATH)

# processing files...
counter = 0
pbar = tqdm(list(MAIN_PATH.iterdir()))
for item_path in pbar:

    if not item_path.is_file():
        continue

    # file name and extension extraction
    filename, file_extension = os.path.splitext(item_path)

    # `.png` and `.PNG` are the same, so...
    file_extension = file_extension.lower()

    # moving file extensions to coressponding directory
    if file_extension in ext_dest:

        old_path = item_path
        split_path = str(item_path).split("/")
        new_dir = Path("/".join(split_path[:-1]) + f"/{ext_dest[file_extension]}/")

        # create destination directory if not exits.
        if not new_dir.exists():
            create_dir(new_dir)

        # move file
        success = move_file(old_path=old_path, new_path=new_dir)
        if success:
            counter += 1
        pbar.set_description(f"{counter} files moved successfuly! (Total: {len(pbar)})!")
