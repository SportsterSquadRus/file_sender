import glob
import hashlib


class FilesHashes:
    def __init__(self, path):
        self.path = path

    def files_hashes_list(self):
        new_files = glob.glob(self.path)
        new_files_hash = list(
            map(lambda path: self.file_hash(path), new_files))
        return set(zip(new_files, new_files_hash))

    def file_hash(self, path):

        with open(path, "r", encoding="utf-8") as input_file:
            data = input_file.read()
        return hashlib.md5(data.encode("utf-8")).digest()
