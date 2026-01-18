from CoolProp.CoolProp import PropsSI

def regenerative_rankine_cycle(P_boiler, T_boiler, P_condenser):
    # Convert units
    P_boiler *= 1e5        # bar → Pa
    P_condenser *= 1e5
    T_boiler += 273.15     # °C → K

    # State 1: Turbine inlet
    h1 = PropsSI("H", "P", P_boiler, "T", T_boiler, "Water")
    s1 = PropsSI("S", "P", P_boiler, "T", T_boiler, "Water")

    # State 2: Turbine outlet (isentropic)
    h2 = PropsSI("H", "P", P_condenser, "S", s1, "Water")

    # State 3: Condenser outlet (saturated liquid)
    h3 = PropsSI("H", "P", P_condenser, "Q", 0, "Water")

    # State 4: Pump outlet
    h4 = h3 + (P_boiler - P_condenser) * 1e-3  # Approx pump work

    # Performance
    turbine_work = h1 - h2
    pump_work = h4 - h3
    heat_added = h1 - h4
    efficiency = (turbine_work - pump_work) / heat_added * 100

    return {
        "efficiency": efficiency,
        "turbine_work": turbine_work / 1000,
        "pump_work": pump_work / 1000,
        "heat_added": heat_added / 1000,
        "states": [
            {"P": P_boiler, "T": T_boiler, "s": s1},
            {"P": P_condenser, "s": s1},
            {"P": P_condenser},
            {"P": P_boiler}
        ]
    }
