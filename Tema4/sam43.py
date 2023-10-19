from datetime import datetime
from time import sleep


for i in range(5):
    print(datetime.now().replace(microsecond=0))
    sleep(1)
