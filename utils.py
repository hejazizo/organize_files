import subprocess
import os

def create_dir(path):
    process = subprocess.Popen(['mkdir', path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if stderr:
        return False

    return True

def move_file(old_path, new_path):
    process = subprocess.Popen(['mv', old_path, new_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if stderr:
        return False

    return True

def extract_ext(input_path):
    unique_ext = set()
    for item_path in input_path.iterdir():
        if not item_path.is_file():
            continue
        filename, file_extension = os.path.splitext(item_path)
        if file_extension:
            unique_ext.add(file_extension)

    return unique_ext