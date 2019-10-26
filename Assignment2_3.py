def factorial(num):
	if num<0:
		num=-num;
	fact=1;
	for i in range(1,num+1):
		fact*=i;
	return fact;

def main ():
	print ("Enter the number: ");
	num=int(input());
	ans=factorial(num);
	print ("Factorial of number is ",ans);

if __name__=="__main__":
	main();