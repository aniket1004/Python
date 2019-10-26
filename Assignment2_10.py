def SumDigit(no):

	sum=0;
	l=[int(i) for i in no];
	for i in l:
		sum+=i;
	return sum;

def main():
	print ("Enter the number: ");
	num=input();
	ans=SumDigit(num);
	print ("Sum of digits are ",ans);

if __name__=="__main__":
	main();