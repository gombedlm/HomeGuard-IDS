import { renderDashboard } from './dashboard.js';
import { renderMonitoring, startMonitoring } from './monitoring.js';

// Function to handle navigation
function handleNavigation(event) {
    if (event.target.matches('[data-link]')) {
        event.preventDefault();
        const link = event.target.getAttribute('data-link');
        const title = event.target.textContent; // Use textContent for the title

        // Update URL path
        history.pushState({ link }, title, `/${link}`);

        // Update active state in navigation
        updateActiveLink(link);

        // Render content based on link
        switch (link) {
            case 'dashboard':
                renderDashboard();
                break;
            case 'monitoring':
                renderMonitoring();
                startMonitoring();
                break;
            default:
                console.log(`Unknown link: ${link}`);
        }
    }
}

// Function to update active link based on current URL path
function updateActiveLink(currentLink) {
    const navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(link => {
        if (link.getAttribute('data-link') === currentLink) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Event listener for navigation clicks
document.body.addEventListener('click', handleNavigation);

// Event listener for popstate (back/forward navigation)
window.addEventListener('popstate', function(event) {
    const state = event.state;
    if (state && state.link) {
        const link = state.link;

        // Update active state in navigation
        updateActiveLink(link);

        // Render content based on link
        switch (link) {
            case 'dashboard':
                renderDashboard();
                break;
            case 'monitoring':
                renderMonitoring();
                startMonitoring();
                break;
            default:
                console.log(`Unknown link: ${link}`);
        }
    }
});

// Render the dashboard by default on page load
document.addEventListener("DOMContentLoaded", function() {
    const currentPath = window.location.pathname.split('/')[1] || 'dashboard';
    const defaultLink = document.querySelector(`[data-link="${currentPath}"]`);
    if (defaultLink) {
        defaultLink.classList.add('active');
    }
    switch (currentPath) {
        case 'dashboard':
            renderDashboard();
            break;
        case 'monitoring':
            renderMonitoring();
            startMonitoring();
            break;
        default:
            console.log(`Unknown path: ${currentPath}`);
    }
});

export { handleNavigation };
