import time
from service.files_and_hashes import FilesHashes
# from files_and_hashes import FilesHashes
from service.send_files import FileSender
import argparse

url = '127.0.0.1'
port = 8000
timer = 1
parser = argparse.ArgumentParser()
parser.add_argument('--u')
parser.add_argument('--p')
parser.add_argument('--t')

keys = parser.parse_args()
parsed_args = vars(keys)

print(parsed_args)

if parsed_args['u']:
    url = parsed_args['u']
if parsed_args['p'] and parsed_args['p'].isdigit():
    port = parsed_args['p']
if parsed_args['t'] and parsed_args['t'].isdigit():
    timer = int(parsed_args['t'])


files = set()
file_sender = FileSender("http://{}:{}/upload/api/".format(url, port))

while True:
    files_and_hashes_obj = FilesHashes("test_files/*test")
    hashes = files_and_hashes_obj.files_hashes_list()
    if files != hashes:
        files_to_send = hashes.difference(files)
        files.update(hashes)
        file_sender.send(list(files_to_send))
    print('test')
    time.sleep(timer)
