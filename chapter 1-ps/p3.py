import os

# Specify the path of the directory
directory_path = '. '  # Current directory

try:
    # Get list of all files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
