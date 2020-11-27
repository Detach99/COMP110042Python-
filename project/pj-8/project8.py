if __name__ == "__main__":
    f = open("project8.txt", "r")
    raw = f.readlines()
    f.close()
    print("If {} closed: {}".format(f.name, f.closed))

    d = open("decorate.txt", "w+")
    text = []
    maxcount = 0
    text.append([line.rstrip() for line in raw])
    for line in text[0]:
        if len(line) > maxcount:
            maxcount = len(line) 
            
    print("Begin Printing...")
    d.writelines("+"+"-"*maxcount+"+"+"\n")
    for line in text[0]:
        new_line = "|" + line +" "*(maxcount-len(line)) + "|" + "\n"
        d.writelines(new_line)
    d.writelines("+"+"-"*maxcount+"+")
    print("Writing done!\nUse 'cat decorate.txt' to check!")
    d.close()
    print("If {} closed: {}".format(d.name, d.closed))
