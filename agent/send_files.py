import requests
import time


class FileSender:
    def __init__(self, url, file_list=None):
        self.file_list = file_list
        self.url = url

    def send(self, file_list):

        dict_of_files = dict()

        for i in range(len(file_list)):

            dict_of_files['file{}'.format(i)] = open(file_list[i][0], 'rb')
        r = requests.post(self.url, files=dict_of_files)
        print(r.text)
