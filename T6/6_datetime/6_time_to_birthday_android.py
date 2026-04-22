import datetime
import subprocess
subprocess.run(args="clear")

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
day = int(input("What is Your DAY of the birth: "))
month = int(input("What is Your MONTH of the birth: "))
year = int(input("What is Your YEAR of the birth: "))


print(f"You were born on: {datetime.date(year, month, day)}")
current_year = datetime.datetime.today().year
# print(f"{current_year}")

next_birthday = datetime.datetime(current_year, month, day)
today = datetime.datetime.today().date()
print(f"Today is: {today}")
today = datetime.datetime.today()

print(f"Next birthdays will be at: {next_birthday.date()}")
print(f"It will be in {(abs(today - next_birthday)).days} days")
print(f"It will be in {((abs(today - next_birthday)).days)/30:.2f} months")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
