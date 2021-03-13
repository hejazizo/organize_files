import os
import subprocess
from pathlib import Path

from tqdm import tqdm


class OrganizeDir:
    def __init__(self, input_dir):
        self.input_dir = Path(input_dir)
        self.unique_ext = self.extract_ext()
        self.ext_dest = {
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

    def run(self):
        # processing files...
        counter = 0
        pbar = tqdm(list(self.input_dir.iterdir()))
        for item_path in pbar:

            if not item_path.is_file():
                continue

            # file name and extension extraction
            filename, file_extension = os.path.splitext(item_path)

            # `.png` and `.PNG` are the same, so...
            file_extension = file_extension.lower()

            # moving file extensions to coressponding directory
            if file_extension in self.ext_dest:

                old_path = item_path
                split_path = str(item_path).split("/")
                new_dir = Path("/".join(split_path[:-1]) + f"/{self.ext_dest[file_extension]}/")

                # create destination directory if not exits.
                if not new_dir.exists():
                    self.create_dir(new_dir)

                # move file
                success = self.move_file(old_path=old_path, new_path=new_dir)
                if success:
                    counter += 1
                pbar.set_description(f"{counter} files moved successfuly! (Total: {len(pbar)})!")


    def extract_ext(self):
        unique_ext = set()
        for item_path in self.input_dir.iterdir():
            if not item_path.is_file():
                continue
            filename, file_extension = os.path.splitext(item_path)
            if file_extension:
                unique_ext.add(file_extension)

        return unique_ext

    def create_dir(self, path):
        process = subprocess.Popen(['mkdir', path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            return False

        return True

    def move_file(self, old_path, new_path):
        process = subprocess.Popen(['mv', old_path, new_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            return False

        return True
