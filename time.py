import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    print(f"Focus timer started for {minutes} minutes.")

    while time.time() < end_time:
        remaining = round(end_time - time.time())
        print(f"Time remaining: {remaining} seconds")
        time.sleep(1)
    
    print("Focus timer ended. Time to take a break!")

# 设置专注时间为25分钟
focus_timer(25)
