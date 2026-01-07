# core/middleware/request_timing.py
import time
from flask import request, g

def request_timer(app, metrics):
    """Time request duration and record in metrics.
        Note: Metrics is injected to avoid circular imports 
        and tight coupling to infrastructure"""
    @app.before_request
    def start_timer():
        g.start_time = time.perf_counter()

    @app.after_request
    def record_duration(response):
        if hasattr(g, 'start_time'):
            duration_ms = (time.perf_counter() - g.start_time) * 1000
            metrics.request_duration.observe(duration)
            metrics.record_response_time(
                path=request.path,
                method=request.method,
                status=response.status_code,
                duration_ms=duration_ms,
            )
        return response