import os
dict={"Owner":"ayush1509"}

def dynamic(name):
    # name=input("enter name:")
    password=input("enter password for new file:")
    try:
        os.mkdir("PassWords")
    except Exception as e:
        pass
    op=open(r"PassWords/name.txt","a")
    pw=open(r"PassWords/password.txt","a")

    op.write(name)
    op.write("\n")
    pw.write(password)
    pw.write("\n")
    op.close()
    pw.close()

    op=open(r"PassWords/name.txt","r")
    pw=open(r"PassWords/password.txt","r")

    iden=op.readlines()
    secu=pw.readlines()
    n=len(iden)
    m=len(secu)
    dic={}
    while(n>0 or m>0):
        nam=iden[n-1].strip()
        secure=secu[m-1].strip()
        # strip function removes all the trailing unwanted characters from the string
        dic[nam]=secure
        n=n-1
        m=m-1
    
    return dic
        
def executer():
    op=open(r"PassWords/name.txt","r")
    pw=open(r"PassWords/password.txt","r")

    iden=op.readlines()
    secu=pw.readlines()
    n=len(iden)
    m=len(secu)
    dic={}
    while(n>0 or m>0):
        nam=iden[n-1].strip()
        secure=secu[m-1].strip()
        # strip function removes all the trailing unwanted characters from the string
        dic[nam]=secure
        n=n-1
        m=m-1
    
    return dic
        








