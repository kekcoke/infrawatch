# backend/app/models/infrastructure.py
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Server:
    """Represents a monitored server"""
    id: str
    hostname: str
    ip_address: str
    status: str # 'healthy', 'warning', 'critical'
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    last_heartbeat: datetime

    def to_dict(self) -> Dict:
        """Convert Server instance to dictionary; serialize for API responses"""
        return {
            "id": self.id,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "status": self.status,
            "metrics" : {
                "cpu_usage": self.cpu_usage,
                "memory_usage": self.memory_usage,
                "disk_usage": self.disk_usage,
            },
            "last_heartbeat": self.last_heartbeat.isoformat(),
        }
    
@dataclass
class InfrastructureCluster:
    """Represents a cluster of servers"""
    # id: str
    name: str
    servers: List[Server]
    # created_at: datetime
    # updated_at: datetime

    def to_dict(self) -> Dict:
        """Convert InfrastructureCluster instance to dictionary; serialize for API responses"""
        return {
            # "id": self.id,
            "name": self.name,
            "servers": [server.to_dict() for server in self.servers],
            # "created_at": self.created_at.isoformat(),
            # "updated_at": self.updated_at.isoformat(),
        }

    @property
    def healthy_servers(self) -> int:
        return len([s for s in self.servers if s.status == 'healthy'])
    
    @property
    def total_servers(self) -> int:
        return len(self.servers)
    
@dataclass
class Metrics:
    """Metrics data for collecting and aggregating data over time"""
    metric_type: Optional[str] = None
    metric_name: Optional[str] = None
    source: Optional[str] = None
    window_seconds: Optional[int] = None
    values: List[float] = field(default_factory=list)
    timestamps: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert Metrics instance to dictionary; serialize for API responses"""
        return {
            "metric_type": self.metric_type,
            "metric_name": self.metric_name,
            "source": self.source,
            "window_seconds": self.window_seconds,
            "values": self.values,
            "timestamps": self.timestamps,
        }

    @property
    def response_times(self) -> Dict[str, float]:
        """Simulate response time metrics aggregation"""
        # In production, this would query a time-series database
        return {
            "p50": 120.5,
            "p90": 200.3,
            "p99": 350.7,
            "average": 150.2,
        }
    
    @property
    def error_rates(self) -> Dict[str, float]:
        """Simulate error rate metrics aggregation"""
        # In production, this would query a time-series database
        return {
            "total_requests": 10000,
            "error_requests": 150,
            "error_rate_percentage": 1.5,
        }

    def record_response_time(
            self, 
            path: str, 
            method: str, 
            status: int, 
            duration_ms: float
        ) -> None:
        """Record a response time metric"""
        # In production, this would store the metric in a time-series database
        self.values.append(duration_ms)
        self.timestamps.append(datetime.utcnow().isoformat())