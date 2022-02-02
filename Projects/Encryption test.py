ch = ""
while True:
	choice = input("(E)Encrypt/(D)Decrypt/(C)Code ASCII\n")
	if choice in ["E","D","C"]:
		break
	else:
		print("Please enter a 'D' or 'E' or 'C'")
n = input("n=")
if choice == "E":
	for i in range(len(n)):
		if n[i].isdecimal():
			ch+=chr(64+int(n[i]))
		else:
			ch+=str(ord(n[i].upper())-64)
elif choice == "D":
	print("hetha mezelt ne3mel fih")
elif choice == "C":
	for i in range(len(n)):
		ch+=str(ord(n[i]))
print(ch)
# bOzjLmflEGYouQ4ISTNPEujAzs9u+taQTxG7O8o8sABHC3d4KrkDKJU89UgLP3kNh9evkP8RQFQVk6589798566
