def FindLen(str):
	icnt=0;
	for i in str:
		icnt=icnt+1;
	return icnt;
		
def main():
	print ("Enter string: ");
	str=input();
	ans=FindLen(str);
	print ("String length is :",ans);

if __name__=="__main__":
	main();