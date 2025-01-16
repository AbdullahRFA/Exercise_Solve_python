import os

def clear_clutter(folder_path):
    """
    Clears clutter in the specified folder by renaming files based on their type.
    Each file type is renamed sequentially (e.g., 1.png, 2.png, etc.).

    Args:
        folder_path (str): Path to the folder to organize.
    """
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Get all files in the folder
    files = os.listdir(folder_path)
    print(f"Files in the folder '{folder_path}':\n{files}\n")

    # Dictionary to track numbering for each file extension
    file_counters = {}

    # Process each file in the folder
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Skip if it's not a file
        if not os.path.isfile(file_path):
            print(f"Skipping non-file: {file}")
            continue

        # Get the file extension
        file_extension = os.path.splitext(file)[1].lower()

        # Initialize the counter for this file type if not already
        if file_extension not in file_counters:
            file_counters[file_extension] = 1

        # Generate the new file name
        new_file_name = f"{file_counters[file_extension]}{file_extension}"
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        try:
            os.rename(file_path, new_file_path)
            print(f"Renamed: '{file}' -> '{new_file_name}'")
        except Exception as e:
            print(f"Error renaming '{file}': {e}")

        # Increment the counter for this file type
        file_counters[file_extension] += 1

    print("\nClutter cleared and files renamed successfully!")

# Example usage
folder_to_clean = "clutterFolder"  # Replace with the path to your folder
clear_clutter(folder_to_clean)