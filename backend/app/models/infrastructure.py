# backend/app/models/infrastructure.py
from datetime import datetime
from dataclasses import dataclass
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