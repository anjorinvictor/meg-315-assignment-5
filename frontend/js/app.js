// Grab input references
const boilerPressureInput = document.getElementById("boilerPressure");
const boilerTempInput = document.getElementById("boilerTemp");
const condenserPressureInput = document.getElementById("condenserPressure");
const diagramContainer = document.getElementById("diagramContainer");

// Create a results container if it doesn't exist
let resultsContainer = document.getElementById("results");
if (!resultsContainer) {
    resultsContainer = document.createElement("div");
    resultsContainer.id = "results";
    resultsContainer.style.marginTop = "15px";
    diagramContainer.parentNode.insertBefore(resultsContainer, diagramContainer.nextSibling);
}

// Show loading message
function showLoading() {
    diagramContainer.innerHTML = "<p>Calculating... Please wait.</p>";
    resultsContainer.innerHTML = "";
}

// Show error message
function showError(message) {
    diagramContainer.innerHTML = `<p style="color:red;">${message}</p>`;
    resultsContainer.innerHTML = "";
}

// Render Base64 diagram image
function renderDiagram(imageBase64) {
    diagramContainer.innerHTML = `<img src="data:image/png;base64,${imageBase64}" alt="Cycle Diagram" style="max-width:100%; border-radius:10px;">`;
}

// Render cycle properties below diagram
function renderResults(data) {
    resultsContainer.innerHTML = `
        <h3>Cycle Properties</h3>
        <p><strong>Thermal Efficiency:</strong> ${data.efficiency.toFixed(2)} %</p>
        <p><strong>Turbine Work:</strong> ${data.turbine_work.toFixed(2)} kJ/kg</p>
        <p><strong>Pump Work:</strong> ${data.pump_work.toFixed(2)} kJ/kg</p>
        <p><strong>Heat Added:</strong> ${data.heat_added.toFixed(2)} kJ/kg</p>
    `;
}

// Validate inputs
function validateInputs() {
    if (!boilerPressureInput.value || !boilerTempInput.value || !condenserPressureInput.value) {
        showError("Please fill all required fields!");
        return false;
    }
    return true;
}

// Generic function to send request to backend
async function generateDiagram(endpoint) {
    if (!validateInputs()) return;

    showLoading();

    const payload = {
        boiler_pressure: parseFloat(boilerPressureInput.value),
        boiler_temp: parseFloat(boilerTempInput.value),
        condenser_pressure: parseFloat(condenserPressureInput.value)
    };

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Server error");

        const data = await response.json();

        if (data.diagram) renderDiagram(data.diagram);
        if (data.efficiency) renderResults(data);

    } catch (err) {
        showError("Failed to calculate cycle. Please make sure the backend is running.");
        console.error(err);
    }
}

// Button event handlers
function generateTS() {
    generateDiagram("http://127.0.0.1:8000/generate-ts");
}

function generatePV() {
    generateDiagram("http://127.0.0.1:8000/generate-pv");
}




