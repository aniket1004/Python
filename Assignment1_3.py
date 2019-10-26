def Add(no1,no2):
	return no1+no2;

def main():
	print ("Enter the first number:");
	num1=input();
	print ("Enter the Second number:");
	num2=input();
	ans=Add(int(num1),int(num2));
	print ("Addition of two numbers is: ",ans);
	
if __name__=="__main__":
	main(); 