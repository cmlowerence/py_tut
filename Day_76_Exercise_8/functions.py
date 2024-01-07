import time
import os
def isDir(path: str) -> bool:
    """
    Check if the specified path refers to an existing directory.

    Parameters:
        path (str): The path to be checked.

    Returns:
        bool: True if the path is an existing directory, False otherwise.

    Raises:
        TypeError: If the provided path is not a string.

    Examples:
        >>> isDir('/path/to/directory')
        True

        >>> isDir('/path/to/nonexistent_directory')
        False
    """
    if not isinstance(path, str):
        raise TypeError("Input path must be a string.")

    return os.path.isdir(path)

# Checks weather the input file path is pdf or not
def isPDF(path: str) -> bool:
    """
    Check if the specified file path corresponds to a PDF file based on its extension.

    Parameters:
        path (str): The file path to be checked.

    Returns:
        bool: True if the file has a '.pdf' extension, False otherwise.

    Raises:
        TypeError: If the provided path is not a string.

    Examples:
        >>> isPDF('/path/to/document.pdf')
        True

        >>> isPDF('/path/to/non_pdf_file.txt')
        False
    """
    if not isinstance(path, str):
        raise TypeError("Input path must be a string.")

    return path.lower().endswith('.pdf')



def changeDir(path: str) -> None:
    """
    Change the current working directory to the specified path.

    Parameters:
        path (str): The path to set as the new current working directory.

    Returns:
        None
    """
    os.chdir(path)



def checkType(content: str) -> str:
    """
    Determine the type of the specified content (file or directory).

    Parameters:
        content (str): The path to check.

    Returns:
        str: 'dir' if content is a directory, 'file' if it's a file, 'unknown' otherwise.
    """
    if os.path.isdir(content):
        return 'dir'
    elif os.path.isfile(content):
        return 'file'
    else:
        return 'unknown'



def content_dir(path: str) -> list:
    """
    Get a list of dictionaries containing information about contents in the specified directory.

    Parameters:
        path (str): The path to the directory.

    Returns:
        list: A list of dictionaries with keys 'name', 'type', and 'index'.
    """
    contents = os.listdir(path)
    return [{'name': content, 'type': checkType(content), 'index': index} for index, content in enumerate(contents, 1)]

def get_valid_dir_name() -> str:
    """
    Prompt the user to enter a valid directory name. Allow the user to exit the program by entering 'exit'.
    
    Returns:
        str: A valid directory name entered by the user or None if the user chooses to exit.
    """
    dir_name = input("Enter the directory name (enter 'exit' to stop): ")

    if dir_name.lower() == 'exit':
        print("Terminating the program",end='', flush = True)
        time.sleep(.8)
        print('.',end='', flush = True)
        time.sleep(.8)
        print('.',end='', flush = True)
        time.sleep(.8)
        print('.',end='', flush = True)
        time.sleep(.9)
        print()
        return None

    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        return dir_name
    else:
        print(f"Invalid directory name: '{dir_name}'. Please enter a valid directory name.")
        return get_valid_dir_name()