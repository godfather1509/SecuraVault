import checker as ch
import passwordman as psm
import os
def doct(t):
    omp=1
    while (omp==1):
        q = input("Do you want to open existing file or new file(E/N): ")
        q = q.lower()

        if (q == "n" or q=="new"):
            try:
                os.mkdir("Files")
            except Exception as e:
                pass

            p = "Files"
            while True:
                file_name = input("enter the name of user:")
                val=ch.reader(file_name)
                if(val!=1):
                    data=psm.dynamic(file_name)
                    patientName = f"{file_name}.txt"
                    l = fr"{p}/{patientName}"
                    # 'r' prefix before the string means it is a raw string it means iterpreter shall take escape sequences as literal characters
                    h = open(l, 'w')
                    old = ""
                    print("Type what you want:")
                    while True:
                        z = input()
                        h.write(z)
                        h.write("\n")
                        if (z == ""):
                            if (old == ""):
                                break
                            else:
                                old = ""
                        else:
                            old = z
                    h.close()
                    break
                
                if(val==1):
                    print("file name already in use")
                    continue
                

        if (q == "no" or q == "No"):
            omp=-1
            return -1

        if (q == "E"):
            p = r"C:\Users\ayush\OneDrive\Desktop\multi mini project\Files"
            m = input("enter the name of user:")
            password=input("enter password of the file:")
            data=psm.executer()
            name=data[m]
            t = f"{m}.txt"
            l = fr"{p}/{t}"
            val = ch.reader(m)

            if (val == 1 and name==password):
                que = input("Do you want to read or make changes to the file(R/W):")
                que = que.title()

                if (que == "W"):
                    h = open(l, "a")
                    old = ""
                    print("Type what you want:")
                    while True:
                        z = input()
                        h.write(z)
                        h.write("\n")
                        if (z == ""):
                            if (old == ""):
                                break
                            else:
                                old = ""
                        else:
                            old = z
                    h.close()

                if (que == "R"):
                    h = open(l, "r")
                    red = h.read()
                    print(red, "\n")
                    h.close()
