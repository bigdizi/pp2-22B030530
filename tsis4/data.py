import datetime
# firstly
# a = datetime.datetime.now()
# b = datetime.datetime(x.year, x.month, x.day - 5)
# print(y.strftime("%x"))

# secondly
# a1 = datetime.datetime.now()
# print(a1.day - 1, a1.day, a1.day + 1)

# thirdly
# a2 = datetime.datetime.today().replace(microsecond=0)
# print(a2)

# 4

a3 = datetime.datetime.now()
year = int(input())
month = int(input())
day = int(input())

if (a3.year != year):
    year_time = ((a3.year - year) * 365 * 24 * 60)
elif (a3.year == year):
    year_time = 0

if (a3.month != month):
    month_time = ((a3.month - month) * 30 * 24 * 60)
elif (a3.month == month):
    month_time = 0

if (a3.day != day):
    day_time = ((a3.day - day) * 24 * 60)
elif (a3.day == day):
    day_time = 0

calc = ((day_time + month_time + year_time) * 60) + a3.minute * 60
print(calc)