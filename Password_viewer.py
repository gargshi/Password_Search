import os
F_DIR="D:\\Users\\Shivam Garg\\Documents\\Chrome Passwords.csv"
f=open(F_DIR,'r')
con=f.read()
f.close()
URL=input("Enter NAME of website (OR A PART OF IT):")
con=con.split("\n")
for i in con:
	x=i.split(",")
	if URL in i:
		print(x)


