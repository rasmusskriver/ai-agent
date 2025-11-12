import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(working_directory_path):
        return f"Error: Cannot read {working_directory_path} as it is outside the permitted working directory"
    if not os.path.isfile(target_dir):
        return f"Error: File not found or is not a regular file: {target_dir}"
    try:
        with open(target_dir) as file_yes:
            content = file_yes.read(MAX_CHARS)
            if os.path.getsize(target_dir) > MAX_CHARS:
                content += f'[...File "{target_dir}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error reading file "{target_dir}": {e}'
