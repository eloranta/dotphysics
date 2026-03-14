g1 = graph(xtitle="x",ytitle="f",width=400,height=200)
f1 =gcurve(color=color.blue)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.green)

A1 =0.1
w1 = 1
k1 = 4
d1 = pi/10
Web VPython 3.2
g1 = graph(xtitle="x",ytitle="f",width=400,height=200)
f1 = gcurve(color=color.blue)

A1 = 1
w1 = 1
k1 = 4
d1 = 0

x = 0
t = 0
dx = 0.01
dt = 0.01

def s1(x,t):
    return A1*sin(t)

while t<6.28:
    f1.plot(t,s1(x,t))
    t = t + dt
