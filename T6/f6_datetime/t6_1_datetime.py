import datetime
import time
import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

# print(datetime)

date = datetime.date(2025,4,1)
today = datetime.date.today()
now = datetime.datetime.now()
print("------------------------------------------")
print(date)
print(today)
print(now)
print(f">>> {time.strftime('%H:%M:%S', time.localtime())} <<<")
print("------------------------------------------")
print(today - date)
print("------------------------------------------")
now = now.strftime("%H:%M%S %m-%d-%Y") # ℹ️
print(f"{now}")
print("------------------------------------------")
target_datetime = datetime.datetime(2026,5,4,15,30,33) # ℹ️
print(f"{target_datetime}")
current_datetime = datetime.datetime.now() # ℹ️
print(f"{current_datetime}")
print(f"{current_datetime-target_datetime}")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303