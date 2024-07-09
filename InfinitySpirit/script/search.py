import os


def folders(dir_path) -> list:
    result = [
        f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
    ]
    return result


def files(dir_path) -> list:
    result = [
        f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
    ]
    return result


def all_files(dir_path, hide_file=False) -> list:
    result = []
    for file in files(dir_path):
        if not file.startswith(".") or hide_file:
            result.append(dir_path + "/" + file)
    for folder in folders(dir_path):
        if not folder.startswith(".") or hide_file:
            for all_file in all_files(dir_path + "/" + folder):
                result.append(all_file)
    return result

