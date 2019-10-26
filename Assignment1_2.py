def ChkNum(no):
	if no%2==0:
		return True;
	else:
		return False;
		
def main():
	print ("Enter number:");
	num=input();
	ans=ChkNum(int(num));
	if ans==True:
		print ("Even number");
	else:
		print ("Odd number");

if __name__=="__main__":
	main();
	