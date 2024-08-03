import os
import time
if __name__ == '__main__':
    while True:
        file_list = os.listdir('/tmp')
        for file_index in file_list:
            if file_index.startswith('fuzz'):
                try:
                    os.remove('/tmp/' + file_index)
                except:
                    pass
        time.sleep(10)