# year = int(input("Enter the year: "))
last_month = input("Enter the last month (number or first 3 letter): ")
# notice_period = int(input("Length of your notice period: "))
# allowance_period = int(input("Length of your allowance period: "))

months = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

print(last_month.isdigit())
#
# if last_month.isdigit():
#     print(f"{months[last_month]}")
# else:
#     key = next((k for k, v in months.items() if v == int(last_month)), None)
#     print(f"{months[str(key)]}")




