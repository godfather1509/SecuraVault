import os as oop
# os module is used from terminating the program and deleting file
import checker as ch
import passwordman as pwm


def fileremover():

    ask = input("Do you want to delete any file(yes/no):")
    ask = ask.title()
    if (ask == "Yes" or ask == "Y"):
        indentity = input("What is the name of file:")
        return_val = ch.reader(indentity)
        if (return_val == 1):
            path = "Files"
            file_path = fr"{path}/{indentity}"
            oop.remove(f"{file_path}.txt")
            # this function of file handling deletes file from folders
            data=pwm.executer()
            password=data[indentity]
            op=open(r"PassWords/name.txt","a+")
            pw=open(r"PassWords/password.txt","a+")
            iden=op.readlines()
            secu=pw.readlines()
            op.close()
            pw.close()
            n=len(iden)
            m=len(secu)
            while(n>0 or m>0):
                nam=iden[n-1].strip()
                secure=secu[m-1].strip()
                # strip function removes all the trailing unwanted characters from the string
                if(nam==indentity and secure==password):
                    iden.pop(n)
                    secu.pop(m)
                    break
                n=n-1
                m=m-1
           
            n=len(iden)
            m=len(secu)
            op=open(r"PassWords/name.txt","w")
            pw=open(r"PassWords/password.txt","w")
            while(n>0 or m>0):
                op.write(iden[n-1])
                op.write("\n")
                pw.write(secu[m-1])
                pw.write("\n")
                n=n-1
                m=m-1
    else:
        oop._exit(0)
