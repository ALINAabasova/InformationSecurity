from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000
RECEIVED_FILE = "received_log.txt"


class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/logs":
            self.send_error(404, "Endpoint not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Invalid Content-Length")
            return

        if content_length <= 0 or content_length > 1_000_000:
            self.send_error(400, "Request body must be between 1 byte and 1 MB")
            return

        data = self.rfile.read(content_length)

        with open(RECEIVED_FILE, "ab") as received_file:
            received_file.write(data)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Sample log received successfully!")

    def log_message(self, format_string, *args):
        print(f"{self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), LogHandler)
    print(f"Local API server listening at http://{HOST}:{PORT}/logs")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()
