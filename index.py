import passwordman as psm
import owner as d
import customer as c
import checker as ch
import deleter as remover


t = input("Are you customer or owner:")
t = t.title()

if (t == "Owner" or t == "O"):
    t = "Owner"
    m = psm.dict[t]
    n = 3

    while (n > 0):
        g = input("Enter password:")
        if (g == m):
            ret = d.doct(t)
            if (ret == "None" or ret == -1):
                n = 0

        else:
            print("Incorrect password entered")
            n = n-1
            print("no. of chances left:", n)

    remover.fileremover()


if (t == "Customer" or t == "C"):
    name = input("Enter your name:")
    # password=input("enter password to open your file:")
    val = ch.reader(name)
    if(val!=1):
        print("Your file doesn't exist")

    if (val == 1):
        password = input("Enter password to open your file:")
        t = name
        w = psm.executer()
        n = 3
        while (n > 0):
            if (password == w[name]):
                c.pat(t, name)
                break

            else:
                print("Incorrect password entered")
                n = n-1
                print("no. of chances left:", n)
