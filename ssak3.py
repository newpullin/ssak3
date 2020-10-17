import os


def is_folder(path: str):
    return os.path.isdir(path)


def ssak3_file(path):
    files = []
    ff = os.listdir(path)

    for f in ff:
        path_all = path + "/" + f
        if is_folder(path_all):
            files.extend(ssak3_file(path_all))

        else:
            files.append(path_all)

    return files

