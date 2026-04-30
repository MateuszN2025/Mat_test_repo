import datetime
import time
import subprocess
subprocess.run(args="clear")

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


print("datetime.date(2026,1,1) = ",datetime.date(2026,1,1))
print("datetime.datetime(2025,2,2,13,54,43) = ",datetime.datetime(2025,2,2,13,54,43))
print("datetime.datetime.now() = ",datetime.datetime.now())
print("datetime.datetime.now().strftime('%m-%Y %H:%M') = ",datetime.datetime.now().strftime("%m-%Y %H:%M"))
print("time.strftime('%H:%M:%S') = ",time.strftime("%H:%M:%S"))

time_diff = datetime.date(2026,1,1) - datetime.date.today()

print("------------------------------------------")
print(f"{'date':<20} {datetime.date(2026, 1, 1)}")
print(f"{'custom datetime':<20} {datetime.datetime(2025, 2, 2, 13, 54, 43)}")
print(f"{'now':<20} {datetime.datetime.now()}")
print(f"{'formatted now':<20} {datetime.datetime.now().strftime('%m-%Y %H:%M')}")
print(f"{'time':<20} {time.strftime('%H:%M:%S')}")
print("------------------------------------------")

print(time_diff)
print(type(time_diff))
print(time_diff.days)
print(time_diff.total_seconds())

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303