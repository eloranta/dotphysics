Web VPython 3.2

A = 1.0
lam = 8.0
freq = 0.5
r = 0.1
rho = pi/2

k = 2*pi/lam
w = 2*pi*freq

L = 16.0
N = 200
dx = L/(N-1)

t = 0
dt = 0.02

scene = canvas(title="Transmission Line Waves", width=900, height=400)

g = graph(title="Wave on Transmission Line",
          xtitle="x",
          ytitle="Voltage",
          xmin=0, xmax=L,
          ymin=-2.5, ymax=2.5,
          width=800, height=350)

forward_curve = gcurve(color=color.cyan)
reflected_curve = gcurve(color=color.orange)
total_curve = gcurve(color=color.red)

while True:
    rate(60)

    forward_curve.delete()
    reflected_curve.delete()
    total_curve.delete()

    for i in range(N):
        x = i*dx

        Vf = A*sin(w*t - k*x)
        Vr = A*r*sin(w*t + k*x - 2*k*L + rho)
        V  = Vf + Vr

        forward_curve.plot(x, Vf)
        reflected_curve.plot(x, Vr)
        total_curve.plot(x, V)

    t += dt