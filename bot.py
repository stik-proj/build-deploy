import schedule
import time

def job():
    print("I'm working...")

# 매 분마다 job 함수를 실행합니다.
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
