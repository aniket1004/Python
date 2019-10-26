def Pattern(no):
	if no<0:
		no=-no;
	for i in range(1,no+1):
		for j in range(1,no+1):
			print (j,end=' ');
		print (" ");
	
def main():
	print ("Enter the number: ");
	num=int(input());
	Pattern(num);
	
if __name__=="__main__":
	main();