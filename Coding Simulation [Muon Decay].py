import random
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Constants
c = 3e8
H = 10000
t_muon = 2.2e-6

# Initial Number of Muons
N0 = int(input("Enter the number of muons: "))

# Speed of Muons
while True:
    v_muon = float(input("Enter the speed of the muons (c): ")) * c
    if v_muon > c:
        print("Please enter a valid speed (smaller than or equal to the speed of light)")

# Lorentz Constant
def lFactor(v):
    f = 1 / np.sqrt(1 - (v / c)**2)
    return f

# Altitudes
altitudes = []
for i in range(0,H+100,100):
    h = H - i
    altitudes.append(h)

# Maximum Distance
life = lFactor(v_muon) * t_muon
dMax = int(life * v_muon)

# Number of Muons Left
num_muon = []
for i in altitudes:
    if H - i > dMax:
        num = 0
    else:
        num = int(N0 * np.exp(-(((H - i) / v_muon) / t_muon)))
    num_muon.append(num)

# Data Frame
data = {
    "Altitude": altitudes,
    "NumberOfMuons": num_muon
    }
df = pd.DataFrame(data)
print(df.to_string())

# Line Graph
def muonGraph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Altitude_(m)"],
        y=df["NumberOfMuons"],
        mode="lines+markers"
        ))
    fig.update_layout(
        title="Simulation of Muons Travelling through Earth's Atmosphere",
        xaxis_title="Altitudes (m)",
        yaxis_title="Number of Muons Left",
        template="plotly_dark"
        )
    fig.show()
muonGraph()