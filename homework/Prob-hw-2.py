def P(n):
    '''
    return n!
    '''    
    if n ==0:
        return 1
    res = 1
    for i in range(1, n+1):
        res =res * i
    return res

def C(n, m):
    '''
    n must be greater than m
    C(n,m) = n!/[m!(n-m)!]
    '''
    if n>=m:
        return P(n)/(P(n-m)*P(m))
    else:
        raise("error: n must be greater than m!")
    


if __name__ == '__main__':
    ''' 1
    ans = 0
    for i in range(1,5):
        ans = ans + (-1)**(i+1)*C(4,i)*C(52-i*2, 13-i*2)/C(52,13)    
    print(ans)
    '''
    r = 1
    ans = 0
    while 4*r<=13:
        ans = ans + (-1)**(r+1)*C(13,r)*C(52-r*4, 13-r*4)/C(52,13)
        r = r+1
    print("question 2:\t"+repr(ans))