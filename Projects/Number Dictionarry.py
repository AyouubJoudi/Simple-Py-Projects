import time
numbers = input("Type a number only by 0;1;2;3;4 : \n")
num = {
    "0" : "Zero ",
    "1" : "One ",
    "2" : "Two ",
    "3" : "Three ",
    "4" : "Four "
    }
l = ""
for i in numbers:
    l += num.get(i, "   wtf bro??   ") 
print(l)
time.sleep(200)
