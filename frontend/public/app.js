
const URL = "http://localhost:3001"
async function loadInfrastructureStatus() {
    try {
        const response = await fetch(`${URL}/api/infra/status`);
        const data = await response.json();

        const container = document.getElementById("status-container");
        container.innerHTML = `
            <div class="status-grid">
                ${data.services.map(service => `
                    <div class="status-card status-healthy">
                        <h3>${service.name}</h3>
                        <p>Status: ${service.status}</p>
                        <p>Uptime: ${service.uptime}</p>
                    </div>
                `).join('')}
            </div>
            <p class="status-last-updated">
                Last updated: ${new Date(data.timestamp).toLocaleString()}
            </p>
        `;
    } catch (err) {
        document.getElementById("status-container").innerHTML = `
            <p class="status-error">Error loading infrastructure status: ${err.message}.
            Please check again later.</p>
        `;
    }

}

// Load status on page load & refresh every 30 seconds
loadInfrastructureStatus();
setInterval(loadInfrastructureStatus, 30000);