from Arithmetic import *;

def main():
	print ("Enter first number: ");
	num1=int(input());
	print ("Enter second number: ");
	num2=int(input());
	
	print ("Addition of numbers is ",Add(num1,num2));
	print ("Subtraction of numbers is ",Sub(num1,num2));
	print ("Multiplication of numbers is ",Mult(num1,num2));
	print ("Division of numbers is ",Div(num1,num2));

if __name__=="__main__":
	main();