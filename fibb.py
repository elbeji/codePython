def fibb(n : int)-> int :
    a,b=0,1
    for _ in range(n):
        yield a
        b,a=a+b,b
    return(a)
