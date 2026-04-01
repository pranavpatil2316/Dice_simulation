import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulation Dashboard", layout="wide")

st.title("📊 Simulation Dashboard (Monte Carlo + Queue + Inventory)")

# Sidebar
st.sidebar.header("Controls")
sim_runs = st.sidebar.slider("Number of Simulation Runs", 100, 10000, 1000)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎲 Dice Simulation",
    "🧍 Queue Simulation",
    "📦 Inventory Simulation",
    "📊 Analytical vs Simulation",
    "🧠 Theory"
])

# -----------------------------
# 🎲 1. Dice Simulation
# -----------------------------
with tab1:
    st.header("🎲 Dice Throw Simulation (Monte Carlo)")

    dice_rolls = np.random.randint(1, 7, sim_runs)

    counts = pd.Series(dice_rolls).value_counts().sort_index()
    probs = counts / sim_runs

    st.subheader("Estimated Probabilities")
    st.write(probs)

    fig, ax = plt.subplots()
    ax.bar(probs.index, probs.values)
    ax.set_xlabel("Dice Face")
    ax.set_ylabel("Probability")
    st.pyplot(fig)

# -----------------------------
# 🧍 2. Queue Simulation
# -----------------------------
with tab2:
    st.header("🧍 Single Server Queue Simulation")

    arrival_rate = st.slider("Arrival Rate (λ)", 1, 10, 4)
    service_rate = st.slider("Service Rate (μ)", 2, 15, 6)

    arrivals = np.random.exponential(1/arrival_rate, sim_runs)
    services = np.random.exponential(1/service_rate, sim_runs)

    arrival_times = np.cumsum(arrivals)
    service_start = np.zeros(sim_runs)
    service_end = np.zeros(sim_runs)

    for i in range(sim_runs):
        if i == 0:
            service_start[i] = arrival_times[i]
        else:
            service_start[i] = max(arrival_times[i], service_end[i-1])
        service_end[i] = service_start[i] + services[i]

    waiting_time = service_start - arrival_times
    avg_wait = np.mean(waiting_time)

    st.subheader(f"Average Waiting Time: {avg_wait:.3f}")

    fig, ax = plt.subplots()
    ax.plot(waiting_time[:100])
    ax.set_title("Waiting Time (First 100 Customers)")
    st.pyplot(fig)

# -----------------------------
# 📦 3. Inventory Simulation
# -----------------------------
with tab3:
    st.header("📦 Inventory Demand Simulation (10 Days)")

    days = 10
    demand = np.random.randint(5, 20, days)
    inventory = 100
    stock = []

    for d in demand:
        inventory -= d
        if inventory < 20:
            inventory += 50  # reorder
        stock.append(inventory)

    df = pd.DataFrame({
        "Day": range(1, days+1),
        "Demand": demand,
        "Inventory": stock
    })

    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.plot(df["Day"], df["Inventory"], marker='o')
    ax.set_title("Inventory Levels")
    st.pyplot(fig)

# -----------------------------
# 📊 4. Analytical vs Simulation
# -----------------------------
with tab4:
    st.header("📊 Analytical vs Simulation (M/M/1 Queue)")

    λ = st.slider("Arrival Rate λ", 1, 10, 4, key="a")
    μ = st.slider("Service Rate μ", 2, 15, 6, key="b")

    if λ >= μ:
        st.warning("System is unstable (λ >= μ)")
    else:
        # Analytical
        Wq_analytical = λ / (μ * (μ - λ))

        # Simulation
        arrivals = np.random.exponential(1/λ, sim_runs)
        services = np.random.exponential(1/μ, sim_runs)

        arrival_times = np.cumsum(arrivals)
        service_start = np.zeros(sim_runs)
        service_end = np.zeros(sim_runs)

        for i in range(sim_runs):
            if i == 0:
                service_start[i] = arrival_times[i]
            else:
                service_start[i] = max(arrival_times[i], service_end[i-1])
            service_end[i] = service_start[i] + services[i]

        waiting_time = service_start - arrival_times
        Wq_sim = np.mean(waiting_time)

        st.write(f"📘 Analytical Waiting Time: {Wq_analytical:.3f}")
        st.write(f"🧪 Simulated Waiting Time: {Wq_sim:.3f}")

# -----------------------------
# 🧠 5. Theory
# -----------------------------
with tab5:
    st.header("🧠 Advantages & Limitations of Simulation")

    st.subheader("✅ Advantages")
    st.markdown("""
    - Can model complex real-world systems
    - No strict assumptions required
    - Useful for decision making
    - Visual and interactive
    """)

    st.subheader("❌ Limitations")
    st.markdown("""
    - Computationally expensive
    - Results are approximate
    - Requires good random modeling
    - Not always generalizable
    """)

    st.subheader("📌 Real-Life Example")
    st.markdown("""
    **Food Delivery Apps (like Swiggy/Zomato)**

    Simulation helps:
    - Assign delivery partners
    - Estimate delivery time
    - Reduce waiting time

    Companies simulate thousands of scenarios before real deployment.
    """)