
# **Steam Cycle Visualizer – Regenerative Rankine Cycle**

**A web-based tool to simulate and visualize regenerative Rankine steam cycles for learning and analysis.**

---

## **📌 Project Overview**

The **Steam Cycle Visualizer** allows users to:

* Input **boiler pressure**, **temperature**, and **condenser pressure**.
* Generate **T–s (Temperature–Entropy)** and **P–v (Pressure–Specific Volume)** diagrams.
* Understand the behavior of a **Regenerative Rankine Cycle**.
* Visualize cycle efficiency and key steam properties.

This project is designed for **mechanical engineering students** learning thermodynamics and power cycles. It combines **Python (FastAPI + CoolProp)** for calculations and **HTML/CSS/JS** for the frontend.

---

## **🛠 Project Structure**

```
steam-cycle-visualizer/
│
├── backend/                  # Python FastAPI backend
│   ├── main.py               # Main API server and routes
│   ├── thermo/               # Thermodynamic calculations
│   │   ├── properties.py     # Steam property calculations
│   │   ├── cycles.py         # Cycle computation logic
│   │   └── diagrams.py       # Generates T–s and P–v diagrams
│
├── frontend/                 # Web interface
│   ├── index.html            # Main webpage
│   ├── css/
│   │   └── style.css         # Styling for the frontend
│   └── js/
│       └── app.js            # Frontend logic for interacting with API
│
└── README.md                 # This documentation
```

---

## **⚙️ Technologies & Libraries Used**

**Backend:**

* [Python 3.x](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) – for API server
* [Uvicorn](https://www.uvicorn.org/) – ASGI server to run FastAPI
* [CoolProp](http://www.coolprop.org/) – Steam property calculations
* [Matplotlib](https://matplotlib.org/) – Plotting T–s and P–v diagrams
* [NumPy](https://numpy.org/) – Numerical calculations
* [io.BytesIO](https://docs.python.org/3/library/io.html) – Buffer images for API

**Frontend:**

* HTML5 – Structure of the webpage
* CSS3 – Styling and layout
* JavaScript – Fetch API to communicate with backend and update diagrams dynamically

---

## **🚀 How to Run the Project**

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/steam-cycle-visualizer.git
cd steam-cycle-visualizer
```

### **2. Create a virtual environment and install dependencies**

```bash
python -m venv venv
# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install fastapi uvicorn matplotlib numpy coolprop
```

### **3. Run the backend API**

```bash
python -m uvicorn backend.main:app --reload
```

* The API will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Test endpoint:

```
GET http://127.0.0.1:8000/
Response: {"message":"Thermodynamic Steam Cycle Visualizer API is running."}
```

### **4. Open the frontend**

* Open `frontend/index.html` directly in a browser **OR** serve it via a local server:

```bash
# If you have Python 3.x installed
cd frontend
python -m http.server 5500
```

* Then open [http://127.0.0.1:5500](http://127.0.0.1:5500) in your browser.

---

## **📝 How It Works**

1. **Frontend** collects user input for:

   * Boiler pressure (bar)
   * Boiler temperature (°C)
   * Condenser pressure (bar)

2. Sends data to **backend** endpoints:

   * `/generate-ts` → Returns T–s diagram
   * `/generate-pv` → Returns P–v diagram

3. **Backend** computes:

   * Steam properties using CoolProp
   * Cycle points using `cycles.py`
   * Generates diagrams with Matplotlib and returns images to frontend

4. **Frontend** displays the diagrams dynamically on the page.

---

## **📊 Example Inputs**

| Parameter          | Example Value |
| ------------------ | ------------- |
| Boiler Pressure    | 30 bar        |
| Boiler Temperature | 450 °C        |
| Condenser Pressure | 0.04 bar      |

---



