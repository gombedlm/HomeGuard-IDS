// Function to render the Dashboard
function renderDashboard() {
    const mainContent = document.getElementById('mainContent');
    mainContent.innerHTML = `
        <div class="container">
            <div class="quick-links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#" data-link="alerts" class="button-widget">Alerts</a></li>
                    <li><a href="#" data-link="logs" class="button-widget">Logs</a></li>
                    <li><a href="#" data-link="reports" class="button-widget">Reports</a></li>
                </ul>
            </div>
            <div id="dynamicContent" class="widgets-container">
                <div class="widget widget-large" id="dashboard">
                    <h3>Monitoring Suite</h3>
                    <p>Real-time network traffic monitoring.</p>
                    <a href="#" class="button button-widget" data-link="monitoring">Open Monitoring</a>
                </div>
            </div>
        </div>
    `;

    // Event listener for widget clicks
    mainContent.addEventListener('click', function(event) {
        if (event.target.matches('[data-link]')) {
            event.preventDefault();
            const link = event.target.getAttribute('data-link');
            const title = event.target.textContent; // Use textContent for the title

            // Update URL path
            history.pushState({ link }, title, `/${link}`);

            // Handle widget click action here
            switch (link) {
                case 'alerts':
                    // Handle Alerts widget click action
                    break;
                case 'logs':
                    // Handle Logs widget click action
                    break;
                case 'reports':
                    // Handle Reports widget click action
                    break;
                default:
                    console.log(`Unknown link: ${link}`);
            }
        }
    });
}

export { renderDashboard };
