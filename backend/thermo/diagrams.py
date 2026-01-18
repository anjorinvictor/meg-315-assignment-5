import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
from CoolProp.CoolProp import PropsSI
import numpy as np


def plot_ts(cycle):
    # ===== 1. Saturation dome =====
    T_sat = np.linspace(273.16, 647.0, 400)  # slightly below critical
    s_f = []
    s_g = []

    for T in T_sat:
        s_f.append(PropsSI("S", "T", T, "Q", 0, "Water"))
        s_g.append(PropsSI("S", "T", T, "Q", 1, "Water"))

    # ===== 2. Cycle process line =====
    s_cycle = []
    T_cycle = []

    for state in cycle["states"]:
        if "T" in state and "s" in state:
            s_cycle.append(state["s"])
            T_cycle.append(state["T"])
        else:
            # use PropsSI with safe temperature
            T_val = min(PropsSI("T", "P", state["P"], "Q", 0, "Water"), 647.0)
            s_val = PropsSI("S", "P", state["P"], "Q", 0, "Water")
            s_cycle.append(s_val)
            T_cycle.append(T_val)

    # ===== 3. Plot =====
    fig, ax = plt.subplots(figsize=(8,6))

    # Saturation dome
    ax.plot(s_f, T_sat, "b", label="Saturated Liquid")
    ax.plot(s_g, T_sat, "b", label="Saturated Vapor")

    # Cycle
    ax.plot(s_cycle, T_cycle, "ro-", label="Regenerative Rankine Cycle")

    ax.set_xlabel("Entropy (J/kg·K)")
    ax.set_ylabel("Temperature (K)")
    ax.set_title("T–s Diagram (Regenerative Rankine Cycle)")
    ax.legend()
    ax.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    return buf



def plot_pv(cycle):
    # ===== 1. Saturation curve =====
    T_sat = np.linspace(273.16, 647.0, 400)  # slightly below critical
    P_sat = []
    v_f = []
    v_g = []

    for T in T_sat:
        try:
            P = PropsSI("P", "T", T, "Q", 0, "Water")
            v_liq = PropsSI("V", "T", T, "Q", 0, "Water")
            v_vap = PropsSI("V", "T", T, "Q", 1, "Water")
            P_sat.append(P)
            v_f.append(v_liq)
            v_g.append(v_vap)
        except:
            continue  # skip points where PropsSI fails

    # ===== 2. Cycle process =====
    P_cycle = []
    v_cycle = []

    for state in cycle["states"]:
        P_state = state["P"]
        # Handle supercritical or missing data safely
        try:
            if "v" in state:
                v_val = state["v"]
            else:
                # Use saturated values if available
                v_val = PropsSI("V", "P", P_state, "Q", 0, "Water")
        except:
            v_val = 1e-3  # fallback small value
        P_cycle.append(P_state)
        v_cycle.append(v_val)

    # ===== 3. Plot =====
    fig, ax = plt.subplots(figsize=(8,6))

    # Saturation dome
    ax.plot(v_f, P_sat, "b", label="Saturated Liquid")
    ax.plot(v_g, P_sat, "b", label="Saturated Vapor")

    # Cycle line
    ax.plot(v_cycle, P_cycle, "ro-", label="Regenerative Rankine Cycle")

    ax.set_xlabel("Specific Volume (m³/kg)")
    ax.set_ylabel("Pressure (Pa)")
    ax.set_yscale("log")  # log scale for better visibility
    ax.set_title("P–v Diagram (Regenerative Rankine Cycle)")
    ax.legend()
    ax.grid(True, which="both", linestyle="--")

    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    return buf






# import matplotlib.pyplot as plt
# from io import BytesIO
# from CoolProp.CoolProp import PropsSI
# import numpy as np

# def plot_ts(cycle):
#     # ===== 1. Saturation dome =====
#     T_crit = 647.095  # Slightly below critical temperature
#     T_sat = np.linspace(273.16, T_crit, 400)  # Water limits
#     s_f = []
#     s_g = []

#     for T in T_sat:
#         s_f.append(PropsSI("S", "T", min(T, T_crit-0.0001), "Q", 0, "Water"))
#         s_g.append(PropsSI("S", "T", min(T, T_crit-0.0001), "Q", 1, "Water"))

#     # ===== 2. Cycle process line =====
#     s_cycle = []
#     T_cycle = []

#     for state in cycle["states"]:
#         if "T" in state and "s" in state:
#             s_cycle.append(state["s"])
#             T_cycle.append(state["T"])
#         else:
#             P_val = state["P"]
#             # Use saturated liquid at P if T not given
#             T_val = PropsSI("T", "P", P_val, "Q", 0, "Water")
#             s_val = PropsSI("S", "P", P_val, "Q", 0, "Water")
#             s_cycle.append(s_val)
#             T_cycle.append(T_val)

#     # ===== 3. Plot =====
#     # Use Agg backend for non-GUI (avoids QApplication warnings)
#     plt.switch_backend('Agg')
#     fig, ax = plt.subplots(figsize=(8,6))

#     # Saturation dome
#     ax.plot(s_f, T_sat, "b", label="Saturated Liquid")
#     ax.plot(s_g, T_sat, "b", label="Saturated Vapor")

#     # Cycle
#     ax.plot(s_cycle, T_cycle, "ro-", label="Regenerative Rankine Cycle")

#     ax.set_xlabel("Entropy (J/kg·K)")
#     ax.set_ylabel("Temperature (K)")
#     ax.set_title("T–s Diagram (Regenerative Rankine Cycle)")
#     ax.legend()
#     ax.grid(True)

#     buf = BytesIO()
#     plt.savefig(buf, format="png", bbox_inches="tight")
#     plt.close(fig)
#     return buf


# def plot_pv(cycle):
#     plt.switch_backend('Agg')
#     P = []
#     v = []

#     for state in cycle["states"]:
#         P_state = state["P"]
#         try:
#             v_state = PropsSI("V", "P", P_state, "Q", 0, "Water")
#         except:
#             v_state = PropsSI("V", "P", P_state, "T", state.get("T", 300), "Water")

#         P.append(P_state)
#         v.append(v_state)

#     fig, ax = plt.subplots(figsize=(8,6))
#     ax.plot(v, P, marker="o")
#     ax.set_xlabel("Specific Volume (m³/kg)")
#     ax.set_ylabel("Pressure (Pa)")
#     ax.set_title("P–v Diagram (Regenerative Rankine Cycle)")
#     ax.grid(True)

#     buf = BytesIO()
#     plt.savefig(buf, format="png", bbox_inches="tight")
#     plt.close(fig)
#     return buf

