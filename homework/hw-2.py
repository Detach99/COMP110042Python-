def almost_equal(x, y, epi):
    if(abs(x-y)<=epi*1e-10):
        return 1
    else:
        return 0


def test_equal():
    """ Try out the equals function """
    i = 0.0
    while not almost_equal(i, 1.0, 0.0001):
        print("i =", i)
        i += 0.1
    print("i =", i)

if __name__=="__main__":
    test_equal()
    

