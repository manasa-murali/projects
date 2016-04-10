import MYSQLdb

trans = []
def getInput():
	in = input("Enter list of trans: ")
	if(in!="\n"):
		if(in.find("select 
		trans.append(in)
def storeInDB():
	con = MYSQLdb.connect("localhost","root","password","virtualDB")
	cursor = con.cursor()
	for item in trans:
		param = item
		cur.execute("insert into virutalTab values(%s);",param)
def encryptThem():
	con = MYSQLdb.connect("localhost","root","password","virtualDB")
	cursor = con.cursor()
	cursor.execute("select * from virtualTab")
	toLimit = 100-cursor.rowcount
	
id= input("enter id:")
check =  re.compile(r"/d")
if id.find(check)!=-1 and id>=0:
	getInput()