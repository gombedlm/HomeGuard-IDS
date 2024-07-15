// Function to render the Monitoring page
function renderMonitoring() {
    const mainContent = document.getElementById('mainContent');
    mainContent.innerHTML = `
        <div class="container">
            <div class="live-update-widget">
                <h3>Live Network Traffic</h3>
                <pre id="liveData">Loading data...</pre>
            </div>
        </div>
    `;
}

// Function to start monitoring
function startMonitoring() {
    console.log("Starting monitoring...");
    fetchMonitoringData();
    setInterval(fetchMonitoringData, 5000);  // Fetch data every 5 seconds
}

export { renderMonitoring, startMonitoring };
