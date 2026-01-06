const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Sample route
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Health check
app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    service: 'infrawatch-backend'
  });
});

// Infra status endpoints
app.get('/api/infra/status', (req, res) => {
    res.json({
        services: [
            { name: 'database', status: 'running', uptime: '99.9%' },
            { name: 'cache', status: 'running', uptime: '99.5%' },
            { name: 'message-queue', status: 'degraded', uptime: '95.0%' },  
            { name: 'api-gateway', status: 'running', uptime: '99.8%' },
            { name: 'auth-service', status: 'running', uptime: '99.7%'},
            { name: 'storage-service', status: 'maintenance', uptime: 'N/A' },
            { name: 'notification-service', status: 'running', uptime: '99.6%' },
            { name: 'analytics-service', status: 'running', uptime: '99.4%' },
            { name: 'search-service', status: 'running', uptime: '99.3%' },
            { name: 'logging-service', status: 'running', uptime: '99.9%' },
            { name: 'load-balancer', status: 'running', uptime: '99.95%' }
        ],
        timestamp: new Date().toISOString()
    });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
