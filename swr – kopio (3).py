Web VPython 3.2

A = 1.0
lam = 8.0
freq = 0.5
r = 0.999
rho = pi

k = 2*pi/lam
w = 2*pi*freq

L = 16.0
N = 200
dx = L/(N-1)

t = 0
dt = 0.02

# SWR
SWR = (1+r)/(1-r)

scene = canvas(width=900, height=400)
scene.title = f"Transmission Line with Standing Wave Envelope"

g = graph(title="Forward, Reflected, Total Waves, and Envelope for Total",
          xtitle="x",
          ytitle="Voltage",
          xmin=0, xmax=L,
          ymin=-2.5, ymax=2.5,
          width=800, height=350)

forward_curve = gcurve(color=color.cyan)
reflected_curve = gcurve(color=color.orange)
total_curve = gcurve(color=color.red)
env_pos_curve = gcurve(color=color.green)
#env_neg_curve = gcurve(color=color.green)

while True:
    rate(60)

    forward_curve.delete()
    reflected_curve.delete()
    total_curve.delete()
    env_pos_curve.delete()
    #env_neg_curve.delete()

    for i in range(N):
        x = i * dx

        Vf = A * sin(w*t - k*x)
        Vr = A * r * sin(w*t + k*x - 2*k*L + rho)
        V = Vf + Vr

        # Standing-wave envelope magnitude
        env = A * sqrt(1 + r**2 + 2*r*cos(2*k*x - 2*k*L + rho))

        forward_curve.plot(x, Vf)
        reflected_curve.plot(x, Vr)
        total_curve.plot(x, V)
        env_pos_curve.plot(x, env)
        #env_neg_curve.plot(x, -env)

    t += dt