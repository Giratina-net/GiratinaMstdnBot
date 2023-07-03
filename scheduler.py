import schedule
import nattun
import komachan
import hotarun

# 定期実行する関数
def job():
    nattun()
    komachan()
    hotarun()
    

# 毎正時に実行
schedule.every().hour.do(job)
