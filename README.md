# 📊 Simulation Dashboard (Monte Carlo + Queue + Inventory)

An interactive **Streamlit-based simulation dashboard** that demonstrates key concepts of **Operations Research and Monte Carlo Simulation**.  
This project visualizes real-world systems like **dice probability, queuing systems, and inventory management** using random simulations.

---

## 🚀 Features

### 🎲 1. Dice Simulation (Monte Carlo)
- Simulates dice throws using random numbers
- Estimates probability distribution
- Visualizes results using bar charts

### 🧍 2. Single Server Queue Simulation
- Models an **M/M/1 queue system**
- Calculates customer waiting time
- Displays dynamic waiting trends

### 📦 3. Inventory Simulation
- Simulates demand for 10 days
- Implements reorder logic
- Tracks inventory levels over time

### 📊 4. Analytical vs Simulation Comparison
- Compares theoretical vs simulated results
- Validates queueing theory formulas
- Demonstrates accuracy of simulations

### 🧠 5. Theory Section
- Advantages and limitations of simulation
- Real-world example (food delivery systems)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Dashboard UI)
- **NumPy** (Random simulation)
- **Pandas** (Data handling)
- **Matplotlib** (Visualization)

---

## 📁 Project Structure

```

simulation_dashboard/
│── app.py
│── requirements.txt

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/simulation-dashboard.git
cd simulation-dashboard
````

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python -m streamlit run app.py
```

---

## 📸 Output

* Interactive dashboard with multiple simulation tabs
* Real-time graphs and probability distributions
* Adjustable parameters for experimentation

---

## 💡 Use Cases

* Academic projects (Operations Research / Simulation)
* Understanding queueing systems
* Inventory optimization studies
* Demonstrating Monte Carlo methods

---

## ⚠️ Notes

* Ensure Streamlit is installed properly
* Use a virtual environment to avoid dependency conflicts
* This project is designed for learning and demonstration purposes

---

## 🔥 Future Improvements

* Add animated simulations
* Real-time queue visualization
* Integration with maps (delivery simulation)
* Advanced UI (dark mode, KPI cards)

---
