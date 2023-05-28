with open("./task_flag.jpg","rb") as f1:
    f = f1.read()
    with open("./flag.jpg","ab") as f2:
        len = len(f)
        i = 0
        while i < len:
            hex = f[i:i+4][::-1]
            f2.write(hex)
            i += 4