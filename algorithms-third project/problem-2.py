import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.exists(path):
        files_with_suffix = []
        dirs_to_walk = [path]

        # exploring the directories
        while dirs_to_walk:
            folder = dirs_to_walk.pop(0) + "/"  # removing first element
            items = os.listdir(folder)  # getting all items from the folder

            # exploting all items by checking first if its a directory or file.
            for i in items:
                i = folder + i
                if os.path.isdir(i):
                    dirs_to_walk.append(i)
                elif str(i).endswith(suffix):
                    files_with_suffix.append(i)
                    
                    
        return files_with_suffix
    else:
        return []


# tests
print(find_files('.c', 'testdir'))
print(find_files('.h', 'testdir'))
print(find_files('.c', ''))
print(find_files('.c', 'testdir/subdir5'))    
