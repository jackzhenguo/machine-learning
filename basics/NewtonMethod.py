"""
Newton method to find solve to f(x)
"""
def newton(x0,niter,threshold,f,fgrad):
    iter=0
    while niter>0:
        x1 = x0 - f(x0)/fgrad(x0)
        if f(x1)<threshold:
            break
        x0 = x1
        iter+=1
        print(str(iter)+ " x= "+str(x1))
        niter-=1
    return x1


s = newton(50,100,1e-10,lambda x: x*x-11*x+10,lambda x: 2*x - 11)
print("solve= "+str(s))