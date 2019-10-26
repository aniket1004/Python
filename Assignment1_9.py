def PrintEven(no):
	if no<0:
		no=-no;
	i=0;
	j=1;
	while (no!=i):
		if j%2==0:
			print (j,end=' ');
			i=i+1;
		j=j+1;
def main():
	print ("Enter number: ");
	num=input();
	PrintEven(int(num));

if __name__=="__main__":
	main();
			
	