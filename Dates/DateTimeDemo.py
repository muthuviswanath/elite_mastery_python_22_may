import datetime

now = datetime.datetime.now()
print(now)
today = datetime.date.today()
print(today)

print(dir(datetime))
my_bday = datetime.date(1984,5,16)
print(my_bday)

from datetime import date as Dt
print(Dt(1947,8,15))

tstamp = Dt.fromtimestamp(1234567890)
print(f"Date: {tstamp}")

print(f"Year: {tstamp.year}")
print(f"Month: {tstamp.month} ")
print(f"Date: {tstamp.day}")
