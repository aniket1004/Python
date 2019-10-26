def ChkPrime(no):
	if no<0:
		no=-no;
	
	i=2;
	while (i<no):
		if no%i==0:
			break;
		i=i+1;
		
	if i==no:
		return True;
	else:
		return False;

def main():
	print ("Enter number :");
	num=int(input());
	
	ans=ChkPrime(num);
	if ans==True:
		print ("It is prime number");	
	else:
		print ("It is not prime number");

if __name__=="__main__":
	main();