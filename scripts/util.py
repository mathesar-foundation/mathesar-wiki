import os

def get_files(root, logger, extensions=None):
    """
    Gathers file of given extensions recursively

    Args:
        root: Root directory to search from
        logger: Logger to log with
        extensions: A list of strings, where each string is an extension of the
        form ".ext". Ex: ".txt", ".md", ".pdf". If not passed, all files are
        returned
    """
    logger.info("Gathering files...")
    if extensions:
        all_files = {ext: [] for ext in extensions}
    else:
        all_files = []

    for dir_path, dirs, files in os.walk(root):
        for f in files:
            full_path = os.path.join(dir_path, f)
            _, file_ext = os.path.splitext(f)
            if extensions is None:
                all_files.append(full_path)
            elif file_ext in all_files:
                all_files[file_ext].append(full_path)

    return all_files
