if __name__=="__main__":
    expected = 2.71828182845823
    e = 0
    for i in range(0, 10000000):
        permu = 1
        for j in range(i):
            permu *= j+1
        e += 1/permu        
        if abs(e-expected)<1e-10:
            break
    print("e = {}".format(e))