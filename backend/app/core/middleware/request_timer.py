# backend/app/core/middleware/request_timing.py
import time
from flask import request, g


def request_timer(app, metrics):
    """Time request duration and record in metrics.
    
    Note: Metrics is injected to avoid circular imports 
    and tight coupling to infrastructure
    """
    
    @app.before_request
    def start_timer():
        """Start timing before request is processed"""
        g.start_time = time.perf_counter()

    @app.after_request
    def record_duration(response):
        """Calculate duration after request is processed and record metrics"""
        if hasattr(g, 'start_time'):
            # Calculate duration in milliseconds
            duration_ms = (time.perf_counter() - g.start_time) * 1000
            
            # Record the metric using the existing method
            metrics.record_response_time(
                path=request.path,
                method=request.method,
                status=response.status_code,
                duration_ms=duration_ms,
            )
            
            # Optional: Add response time header for debugging
            response.headers['X-Response-Time'] = f"{duration_ms:.2f}ms"
        
        return response