import os


def write_file(working_directory, file_path, content):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(working_directory_path):
        return f"Error: Cannot read {working_directory_path} as it is outside the permitted working directory"
    try:
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error {e}"
