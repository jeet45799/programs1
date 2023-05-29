file=open("d:\\tops1.txt","w")
file.write("this is file management demo using python")
file.close()
print("file written successfully")


file=open("tops1.txt","r")
print(file.read())
file.close()


file=open("tops1.txt","a")
file.write("\nnow this file is appended")
file.close()
file=open("tops1.txt","r")
print(file.read())
file.close()


file=open("tops2.txt","w+")
file.write("this is w+ mode using python.")
print("current file possition:",file.tell())
file.seek(0)
print("file data :",file.read())
file.close()
