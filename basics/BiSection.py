"""
bisection to find solve to f(x) when x in (a,b) and f(a)*f(b)<0
"""
def biSection(a,b,threshold,f):
    iter=0
    while a<b:
        mid = a + abs(b-a)/2.0
        if abs(f(mid)) < threshold:
            return mid
        if f(mid)*f(b) < 0:
            a = mid
        if f(a)*f(mid) < 0:
            b=mid
        iter+=1
        print(str(iter)+ " a= "+str(a)+ ", b= "+str(b))


s = biSection(5,50,1e-10,lambda x: x*x-11*x+10)
print("solve= "+str(s))