from urllib import request
import os


class DownloadURL:
    def download_save(self, fn):
        try:
            data = self.site.read()
            if not os.path.exists('data/Security Now/'):
                os.makedirs('data/Security Now/')
            with open("data/Security Now/" + fn, 'wb') as f:
                f.write(data)
                f.close()
            return True
        except:
            return False

    def download(self):
        data = self.site.read()
        return data

    def __init__(self, url):
        self.url = url
        self.site = request.urlopen(self.url)


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

