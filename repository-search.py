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
    for folder in folders(dir_path):
        for all_file in all_files(dir_path+"/"+folder):
            result.append(all_file)
    return result
