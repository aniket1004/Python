def SumFactor(no):
	if no<0:
		no=-no;
	sum=0;
	for i in range(1,no):
		if no%i==0:
			sum=sum+i;
	return sum;

def main():
	print ("Enter the number: ");
	num=int(input());
	ans=SumFactor(num);
	print ("Sum of factors of number is ",ans);

if __name__=="__main__":
	main();