# year = int(input("Enter the year: "))
notice_month = input("Enter the last month (number or first 3 letter): ")
# notice_period = int(input("Length of your notice period: "))
# allowance_period = int(input("Length of your allowance period: "))
# period_70 = int(input(f"Length of your 70% benefit period: "))

year = 2026
# print(f"Enter the year: {year}")
# notice_month = "4"
print(f"Enter the NOTICE month (number or first 3 letter): {notice_month}")
notice_period = 3
print(f"Length of your notice period: {notice_period}")
allowance_period = 2
print(f"Length of your allowance period: {allowance_period}")
period_70 = 2
print(f"Length of your 70% benefit period: {allowance_period}")

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

def count_safe_period(notice_month, year=2026):
    notice_month_int = 0
    if notice_month.isdigit():
        notice_month_int = int(notice_month)
    else:
        for num1, month1 in months.items():
            if notice_month == month1:
                notice_month_int = int(num1)

    n70 = notice_period + allowance_period
    months_range = n70 + period_70 + 1

    counter = 0

    for i in range(notice_month_int,months_range+notice_month_int):
        if i > 12:
            year += 1
            for j in range(1, months_range + 1):
                if n70 >= 0:
                    print(f"({counter})>>>: {j}|{year}")
                else:
                    print(f"({counter})>>>: {j}|{year}" + "| 70%")
                n70 -= 1
            counter += 1
            break
        if n70 >= 0:
            print(f"({counter})>>>: {i}|{year}")
        else:
            print(f"({counter})>>>: {i}|{year}" + "| 70%")
        n70 -= 1
        months_range -= 1
        counter += 1



if notice_month.isdigit():
    print("------notice_month------")
    print(f"{notice_month}:{months[notice_month]}|{year}")
    print("------------------------")
    count_safe_period(notice_month,year)

else:
    for num, month in months.items():
        if notice_month == month:
            print("------notice_month------")
            print(f"{num}:{month}|{year}")
            print("------------------------")
            count_safe_period(notice_month,year)







