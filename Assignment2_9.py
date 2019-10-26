def FindDigit(no):
	j=0;
	l=[int (i) for i in no];
	for i in l:
		j=j+1;
	return j;

def main ():
	print ("Enter the number: ");
	num=input();
	ans=FindDigit(num);
	print ("Number of digits are :",ans);

if __name__=="__main__":
	main();	