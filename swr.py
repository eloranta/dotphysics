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

SWR = (1+r)/(1-r)

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

scene.append_to_caption("\n\nr: ")
r_value_text = wtext(text=f"{r:.2f}  ")
scene.append_to_caption("\n")
scene.append_to_caption("rho (deg): ")
rho_value_text = wtext(text=f"{rho*180/pi:.1f}")

def set_r(s):
    global r
    r = s.value
    r_value_text.text = f"{r:.2f}  "
    
def set_rho(s):
    global rho
    rho = s.value
    rho_value_text.text = f"{rho*180/pi:.1f}"

r_slider = slider(min=0, max=0.99, value=r, length=300, bind=set_r, right=15)
rho_slider = slider(min=-pi, max=pi, value=rho, length=300, bind=set_rho, right=15)

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

    t += dt