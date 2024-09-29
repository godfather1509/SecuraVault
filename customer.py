def pat(t, name):
    folder_name = "Files"
    file_name = f"{name}.txt"
    path = fr"{folder_name}/{file_name}"
    h = open(path)
    d = h.read()
    print(d, "\n")
    h.close()