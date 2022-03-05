# 1. Write a Python script to display the various Date Time formats - Go to the editor
import datetime
# a) Current date and time
print(datetime.datetime.now())
# b) Current year
print(datetime.datetime.now().year)
# c) Month of year
print(datetime.datetime.now().month)
# d) Week number of the year
print(datetime.datetime.now().isocalendar().week)
# e) Weekday of the week
print(datetime.datetime.now().isoweekday())
# f) Day of year
print("date of the year:", datetime.datetime.now().strftime("%j"))
# g) Day of the month
print(datetime.datetime.now().strftime("%B"))
# h) Day of week
print(datetime.datetime.now().strftime("%A"))