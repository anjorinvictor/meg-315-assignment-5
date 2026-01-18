from CoolProp.CoolProp import PropsSI
import numpy as np

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .thermo.cycles import regenerative_rankine_cycle
from .thermo.diagrams import plot_ts, plot_pv

import base64




app = FastAPI(
    title="Thermodynamic Steam Cycle Visualizer",
    description="Visualize regenerative Rankine cycles with T-s and P-v diagrams",
    version="1.0"
)



# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class CycleInput(BaseModel):
    boiler_pressure: float
    boiler_temp: float
    condenser_pressure: float

@app.get("/")
def root():
    return {"message": "Thermodynamic Steam Cycle Visualizer API is running."}

def encode_image(img_buffer):
    img_buffer.seek(0)
    return base64.b64encode(img_buffer.read()).decode()

@app.post("/generate-ts")
def generate_ts(cycle: CycleInput):
    print("✅ /generate-ts endpoint HIT")
    print("Received data:", cycle)

    cycle_data = regenerative_rankine_cycle(
        P_boiler=cycle.boiler_pressure,
        T_boiler=cycle.boiler_temp,
        P_condenser=cycle.condenser_pressure
    )

    print("Cycle data calculated")

    ts_buffer = plot_ts(cycle_data)
    print("T-s diagram generated")

    ts_base64 = encode_image(ts_buffer)

    return {
        "diagram": ts_base64,
        "efficiency": cycle_data["efficiency"],
        "turbine_work": cycle_data["turbine_work"],
        "pump_work": cycle_data["pump_work"],
        "heat_added": cycle_data["heat_added"]
    }


@app.post("/generate-pv")
def generate_pv(cycle: CycleInput):
    cycle_data = regenerative_rankine_cycle(
        P_boiler=cycle.boiler_pressure,
        T_boiler=cycle.boiler_temp,
        P_condenser=cycle.condenser_pressure
    )
    pv_buffer = plot_pv(cycle_data)
    pv_base64 = encode_image(pv_buffer)
    return {
        "diagram": pv_base64,
        "efficiency": cycle_data["efficiency"],
        "turbine_work": cycle_data["turbine_work"],
        "pump_work": cycle_data["pump_work"],
        "heat_added": cycle_data["heat_added"]
    }










