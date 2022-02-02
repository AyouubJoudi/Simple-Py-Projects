class Talk_t_y_m():
	while True:
		ce = input("(B)for binary   (H)for hexadecimal   (O)for octal\n")
		ce1 = input("(C)coding or (D)decoding\n")
		n = int(input("Whats the number?\n"))
		if ce.upper() in ['B','H','O'] and ce1.upper() in['D','C'] and n>0:
			break
	n1 = ""
	dict = {10:"A",
			11:"B",
			12:"C",
			13:"D",
			14:"E",
			15:"F"
	}
	def coding(d,n,n1):
		print(f"({n})10:\n")
		while n>=1:
			o=n%d
			if o>=10:
				o=dict[o]
			n1=str(o)+n1
			n = n//d
			print(f"{o}   {n}/{d} : {n1}\n")
		print(f"\n({n1}){d}")


	def decoding(d,n,n1):
		n2=str(n)
		n3=0
		n4=n2[::-1]
		print(f"({n2}):\n")
		for w in range(len(n2)-1,0,-1):
			i=n4[w]
			n3+=int(i)*(d**w)
			print(f"{i}*{d}^{w}={n3}\n")
		n1=str(n3)
		print("(",n2,")",d,": ",n1)

	
	if ce1.upper()=="C":
		if ce.upper()=="B":
			coding(2,n,n1)
		elif ce.upper()=="H":
			coding(16,n,n1)
		elif ce.upper()=="O":
			coding(8,n,n1)
	elif ce1.upper()=="D":
		if ce.upper()=="B":
			decoding(2,n,n1)
		elif ce.upper()=="H":
			decoding(16,n,n1)
		elif ce.upper()=="O":
			decoding(8,n,n1)
	else:
		print("Are you dumb\nWhat are you even doing here??")
Talk_t_y_m()