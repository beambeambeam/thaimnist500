import os
import tarfile


def extract_all_files(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, "r") as tar:
        tar.extractall(extract_to)


CATEGORIES = ["letters", "digits"]
DATA = f"{os.path.dirname(__file__)}/data"
TAR = [f"{os.path.dirname(__file__)}/{x}.tar" for x in CATEGORIES]
os.makedirs(DATA, exist_ok=True)

CATEGORIES_DATA = [f"{DATA}/{x}" for x in CATEGORIES]

for i, _ in enumerate(CATEGORIES):
    extract_all_files(TAR[i], CATEGORIES_DATA[i])

print("Data transformation done")
