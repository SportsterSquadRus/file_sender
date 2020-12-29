import time
from files_and_hashes import FilesHashes
from send_files import FileSender


files = set()
file_sender = FileSender("http://127.0.0.1:8000/upload/api/")

while True:
    files_and_hashes_obj = FilesHashes("test_files/*test")
    hashes = files_and_hashes_obj.files_hashes_list()
    if files != hashes:
        files_to_send = hashes.difference(files)
        files.update(hashes)
        file_sender.send(list(files_to_send))
    time.sleep(1)
