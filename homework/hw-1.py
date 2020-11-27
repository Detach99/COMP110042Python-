def compare(p1, p2, p3):
    print(x, y, z)
    print(id(x),id(y),id(z))
    if (id(x)==id(y)):
        if(id(x)==id(z)):
            print("id_x = id_y = id_z.\n")
        else:
            print("id_x = id_y != id_z.\n")
    else:
        if(id(x)==id(z)):
            print("id_x ！= id_y; id_x = id_z.\n")
        elif(id(y)==id(z)):
            print("id_x =! id_y; id_y = id_z.\n")
        else:
            print("id_x =! id_y != id_z.\n")



if __name__== "__main__":
    x = y = z = 3000    
    compare(id(x),id(y),id(z))

    y = z + 2000    
    compare(id(x),id(y),id(z))

    x = x + 2000
    compare(id(x),id(y),id(z))

    z = y 
    compare(id(x),id(y),id(z))

