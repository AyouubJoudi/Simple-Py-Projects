import datetime
print("we are going to count the time (specific countup)\nplease fill in the next tasks in the form of 00")
year = input("year: ")
month = input("month: ")
day = input("day: ")
hour = input("hours: ")
minute = input("minute: ")
second = input("second: ")
while True:
    print(datetime.datetime.now())
    if datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") == f"{year}-{month}-{day} {hour}:{minute}:{second}":
        print(datetime.datetime.now())
        print("Time ended!!!")
        break
