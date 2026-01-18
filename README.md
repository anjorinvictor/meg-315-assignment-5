Steam Cycle Visualizer – Regenerative Rankine Cycle
Project Overview

The Steam Cycle Visualizer is a web-based tool for mechanical engineering students to simulate and visualize thermodynamic steam cycles, focusing on the Regenerative Rankine Cycle.
It generates T–s (Temperature–Entropy) and P–v (Pressure–Specific Volume) diagrams based on user input, helping students understand cycle behavior and energy efficiency.

Project Architecture
steam-cycle-visualizer/
│
├── backend/                  # FastAPI backend
│   ├── main.py               # Main server and endpoints
│   ├── thermo/               # Thermodynamic utilities
│   │   ├── properties.py     # Functions for thermodynamic properties
│   │   ├── cycles.py         # Cycle calculations
│   │   └── diagrams.py       # Functions to generate T-s and P-v diagrams
│
├── frontend/                 # Static frontend files
│   ├── index.html            # Main web page
│   ├── css/style.css         # Styling
│   └── js/app.js             # JavaScript for form handling & API calls
│
└── README.md                 # Project documentation

How it Works

Frontend collects user inputs (boiler pressure, temperature, condenser pressure) through a form.

Sends POST requests to the backend API.

Backend (FastAPI):

Calculates the steam cycle states using properties.py and cycles.py

Generates diagrams using diagrams.py and Matplotlib / CoolProp

Returns diagrams as images to frontend for display in the browser.

Libraries / Dependencies

Python (Backend)

fastapi – Web framework for API endpoints

uvicorn – ASGI server for FastAPI

coolprop – Thermophysical properties of water/steam

matplotlib – For plotting T–s and P–v diagrams

numpy – Numerical calculations

python-multipart – Form handling

aiofiles – Serve static files asynchronously

Frontend

Standard HTML, CSS, JavaScript

fetch API to communicate with backend

Setup Instructions
1. Clone the repository
git clone <repo_url>
cd steam-cycle-visualizer

2. Create Python virtual environment
python -m venv venv
# Activate
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

3. Install dependencies
pip install fastapi uvicorn matplotlib numpy coolprop python-multipart aiofiles

4. Run the backend
python -m uvicorn backend.main:app --reload


FastAPI runs at: http://127.0.0.1:8000

Test API root: http://127.0.0.1:8000/

5. Access the frontend

Open in a browser:

http://127.0.0.1:8000/static/index.html


Input cycle parameters

Click Generate T–s Diagram or Generate P–v Diagram

Diagrams will render below the form

Important: Do not open index.html directly with file://, it must go through FastAPI to access static files and communicate with backend.

Usage Example

Input cycle parameters:

Parameter	Value
Boiler Pressure	30 bar
Boiler Temperature	450°C
Condenser Pressure	0.04 bar

Generate diagrams:

Click Generate T–s Diagram

Click Generate P–v Diagram

Diagrams appear below the form

Notes / Troubleshooting

Ensure CoolProp temperatures do not exceed 647.096 K (water critical point).

If diagrams fail to render, check console for errors.

Make sure frontend is served via /static route through FastAPI.

Project Goal

Help students visualize regenerative Rankine cycles

Understand changes in temperature, entropy, pressure, and volume

Provide interactive learning for thermodynamics courses