#!/usr/bin/python3
"""Simple REST API example."""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class RequestHandler(BaseHTTPRequestHandler):
    """Handles HTTP GET requests."""

    def send_custom_response(self, code, content_type, content):
        """Reusable response sender."""
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.end_headers()

        if isinstance(content, (dict, list)):
            content = json.dumps(content)

        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):
        path = self.path

        if path == "/":
            self.send_custom_response(
                200,
                "text/html",
                "Hello, this is a simple API!"
            )

        elif path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_custom_response(
                200,
                "application/json",
                data
            )

        elif path == "/status":
            self.send_custom_response(
                200,
                "text/plain",
                "OK"
            )

        else:
            self.send_custom_response(
                404,
                "text/html",
                "Endpoint not found"
            )


def main():
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
