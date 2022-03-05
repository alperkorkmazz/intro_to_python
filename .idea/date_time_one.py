import datetime
birthDate=datetime.date(2003,12,20)
resolution=datetime.timedelta(-5)
print(birthDate.year)
print(birthDate.month)
print(birthDate.day)
print(birthDate+resolution)
print(birthDate.strftime("%A, %B %d, %Y"))
message="GVR was born on {:%A, %B %d %Y}."
print(message.format(birthDate))


launch_date=datetime.date(2017,3,30)
launch_time=datetime.time(22,27,0)
launch_datetime=datetime.datetime(2017,3,30,22,27,0)
print(launch_date)
print(launch_time)
print(launch_datetime)
print(launch_time.hour)
print(datetime.datetime.today())
print(datetime.datetime.today().microsecond)

moon_landing=datetime.datetime.strptime("11/12/1969","%m/%d/%Y")
print(moon_landing)