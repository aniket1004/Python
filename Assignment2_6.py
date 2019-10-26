def Pattern(no):
	if no<0:
		no=-no;
	while (no>0):
		i=0;
		while (i<no):
			print ("*",end=' ');	
			i=i+1;
		print (" ");
		no=no-1;

def main():
	print ("Enter the number: ");
	num=int(input());
	Pattern(num);

if __name__=="__main__":
	main();