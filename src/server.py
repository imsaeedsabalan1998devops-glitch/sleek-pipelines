from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from health import health_check
from metrics import get_metrics

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = health_check()
        elif self.path == "/metrics":
            response = get_metrics()
        else:
            response = {"error": "not found"}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def start_server(port=8000):
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
