import time
from service.files_and_hashes import FilesHashes
from service.send_files import FileSender
from service.argpaser import parser


url, port, timer = parser()

files = set()
file_sender = FileSender("http://{}:{}/upload/api/".format(url, port))

while True:
    files_and_hashes_obj = FilesHashes("test_files/*test")
    hashes = files_and_hashes_obj.files_hashes_list()
    if files != hashes:
        files_to_send = hashes.difference(files)
        files.update(hashes)
        file_sender.send(list(files_to_send))
    time.sleep(timer)
