from pathlib import Path

def paths_to_files_in(dir):
    paths = []
    for path in Path(dir).iterdir():
        if path.is_dir():
            paths += paths_to_files_in(path)
        else:
            paths.append(path)
    return paths
