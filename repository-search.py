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


def all_files(dir_path) -> list:
    result = []
    for file in files(dir_path):
        result.append(file)
    return result