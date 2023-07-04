import schedule
from time import sleep
import nattun
import komachan
import hotarun


# 定期実行する関数
def job():
    hotarun.run()
    nattun.run()
    komachan.run()
    
# 30分ごとにjobを実行
schedule.every(60).minutes.do(job)

job()

while True:
    schedule.run_pending()
    sleep(1)
