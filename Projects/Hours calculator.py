vid = int(input("Vids number:\n"))
total_hours = 0
total_minutes = 0
total_seconds = 0
for i in range(vid):
    nlist = input(">>>\n").split(" ")
    hours = int(nlist[0])
    minutes = int(nlist[1])
    seconds = int(nlist[2])
    total_hours += hours
    total_minutes += minutes
    total_seconds += seconds
    if total_seconds>=60:
        total_minutes += 1
        total_seconds = 0
        if total_minutes>=60:
            total_hours += 1
            total_minutes = 0
print(f"{total_hours}:{total_minutes}:{total_seconds}")
#410:30:28
#I did this for calculating hours in a playlist and turns out its been helpfull
#also I'm chocked about the number
