# backend/app/api/v1/__init__.py
from flask import Blueprint, jsonify, request
from app.models.infrastructure import InfrastructureCluster, Server, Metrics
from datetime import datetime, timedelta
import random

# Implement Blueprints 
health_bp = Blueprint('health', __name__)
infrastructure_bp = Blueprint('infrastructure', __name__)
metrics_bp = Blueprint('metrics', __name__, url_prefix='/metrics')

@health_bp.route('/health')
def health_check():
    """Health check endpoint to verify API is running. Critical for load balancers & monitoring."""
    return jsonify({
        'status': 'healthy', 
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'service': 'infrawatch-backend'
    })

@infrastructure_bp.route('/servers')
def get_servers():
    """Get all monitored servers - simulated data for demonstration."""
    # Simulate server data; in prod this would query a database
    mock_servers = [
        Server(
            id=f'server-{i}',
            hostname=f'web-{i}.example.com',
            ip_address=f'10.0.1.{i+10}',
            status=random.choice(['healthy', 'warning', 'critical']),
            cpu_usage=random.uniform(10, 90),
            memory_usage=random.uniform(20, 80),
            disk_usage=random.uniform(30, 70),
            last_heartbeat=datetime.utcnow() - timedelta(seconds=random.randint(0, 300))
        ) for i in range(5)
    ]

    return jsonify({
        'servers': [server.to_dict() for server in mock_servers],
        'total_count': len(mock_servers),
        'timestamp': datetime.utcnow().isoformat()
    })

@infrastructure_bp.route('/clusters')
def get_clusters():
    """Get infrastructure clusters - overview."""
    # Simulate cluster data
    servers = [
        Server(f'node-{i}', f'k8s-node-{i}', f'10.0.2.{i+10}', 
               'healthy', 45.2, 60.1, 35.8, datetime.utcnow())
        for i in range(3)
    ]
    
    cluster = InfrastructureCluster('production-cluster', servers)
    
    return jsonify({
        'cluster_name': cluster.name,
        'total_servers': cluster.total_servers,
        'healthy_servers': cluster.healthy_servers,
        'servers': [server.to_dict() for server in cluster.servers]
    })

@metrics_bp.route('/metrics/response-times')
def get_response_time_metrics():
    """Get response time metrics for monitored services."""
    # Simulate response time metrics
    metrics = Metrics(
        metric_name='response_time',
        values=[random.uniform(100, 500) for _ in range(10)],
        timestamps=[(datetime.utcnow() - timedelta(minutes=i)).isoformat() for i in range(10)]
    )

    metrics_response_times = metrics.get_response_times()

    return jsonify({
        'metric_name': metrics.metric_name,
        'values': metrics.values,
        'timestamps': metrics.timestamps,
        'response_times': metrics_response_times
    })

@metrics_bp.route('/metrics/error-rates')
def get_error_rate_metrics():
    """Get error rate metrics for monitored services."""
    # Simulate error rate metrics
    metrics = Metrics(
        metric_name='error_rate',
        values=[random.uniform(0, 5) for _ in range(10)],
        timestamps=[(datetime.utcnow() - timedelta(minutes=i)).isoformat() for i in range(10)]
    )

    metrics_error_rates = metrics.get_error_rates()

    return jsonify({
        'metric_name': metrics.metric_name,
        'values': metrics.values,
        'timestamps': metrics.timestamps,
        'error_rates': metrics_error_rates
    })