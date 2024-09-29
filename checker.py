def reader(name):
    folder_name = "Files"
    file_name = f"{name}.txt"
    path = fr"{folder_name}/{file_name}"
    try:
        h = open(path)
        h.close()
        return 1
    except FileNotFoundError as error:
        return 0
