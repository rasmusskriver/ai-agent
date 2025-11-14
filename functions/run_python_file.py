import os


def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    print(f"abs_working_directory: {abs_working_directory}")
    print(f"abs_file_path: {abs_file_path}")
