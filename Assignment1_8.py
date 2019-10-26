def Pattern(no):
	if no<0:
		no=-no;
	i=0;
	while (i<no):
		print ("*",end=' '),
		i=i+1;

def main():
	print ("Enter number:");
	num=input();
	Pattern(int(num));

if __name__=="__main__":
	main();