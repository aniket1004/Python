def Pattern(no):
	if no<0:
		no=-no;
	for i in range(0,no):
		for j in range(0,no):
			print ("*",end="	");
		print ("");

def main():
	print ("Enter number:");
	num=int(input());
	Pattern(num);

if __name__=="__main__":
	main();