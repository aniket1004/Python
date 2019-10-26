def ChkNum(no):
	if no==0:
		print ("Zero");
	elif no>0:
		print ("Positive number");
	else:
		print ("Negative number");

def main():
	print ("Enter number:");
	num=input();
	ChkNum(int(num));

if __name__=="__main__":
	main();