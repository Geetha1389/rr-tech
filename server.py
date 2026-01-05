from http.server import SimpleHTTPRequestHandler, HTTPServer
import json


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/hello":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            payload = {"message": "Hello from Python server!"}
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            super().do_GET()


if __name__ == "__main__":
    port = 8000
    print(f"Serving on http://localhost:{port}")
    HTTPServer(("0.0.0.0", port), MyHandler).serve_forever()
