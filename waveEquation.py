g1 = graph(xtitle="x",ytitle="f",width=400,height=200)
f1 =gcurve(color=color.blue)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.green)

A1 =0.1
w1 = 1
k1 = 4
d1 = pi/10
A2 = 0.08
w2 = 0.8
v = w1/k1
k2 = w2/v

x =0
t = 0
dx = 0.01
dt = 0.01
def s1(xt,tt):
    return(A1*sin(k1*xt-w1*tt + d1))

def s2(xt,tt):
    return(A2*sin(k2*xt-w2*tt))
while t<4:
    rate(100)
    x = 0
    f1data = []
    f2data = []
    f3data = []
    while x<4:
        #f1.plot(x,s1(x,t))
        f1data = f1data + [[x,s1(x,t)]]
        f2data = f2data + [[x,s2(x,t)]]
        f3data = f3data + [[x,s1(x,t)+s2(x,t)]]
        x = x + dx
    f1.data = f1data
    f2.data = f2data
    f3.data = f3data
    t = t + dt
    