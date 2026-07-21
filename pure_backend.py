from http.server import BaseHTTPRequestHandler, HTTPServer
import json

import requests

# Define some initial data
data = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        """Sets headers required for CORS"""
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        # Handle GET requests
        if self.path == '/data':
            # Return all data
            self.send_response(200)

            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path.startswith('/data/'):
            # Return a specific item
            item_id = int(self.path.split('/')[-1])
            for item in data:
                if item['id'] == item_id:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(item).encode())
                    break
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_POST(self):
        # Handle POST requests
        if self.path == '/data':
            content_length = int(self.headers['Content-Length'])
            print("content-length", content_length)
            post_data = self.rfile.read(content_length)
            new_item = json.loads(post_data.decode())
            new_item['id'] = len(data) + 1
            data.append(new_item)
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Location', '/data/{}'.format(new_item['id']))
            self.end_headers()
            self.wfile.write(json.dumps(new_item).encode())
        else:
                self.send_error(404)


    def do_PUT(self):
        # Handle PUT requests
        if self.path.startswith('/data/'):
            item_id = int(self.path.split('/')[-1])
            for i, item in enumerate(data):
                if item['id'] == item_id:
                    content_length = int(self.headers['Content-Length'])
                    put_data = self.rfile.read(content_length)
                    updated_item = json.loads(put_data.decode())
                    updated_item['id'] = item_id
                    data[i] = updated_item
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(updated_item).encode())
                    break
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_DELETE(self):
        # Handle DELETE requests
        if self.path.startswith('/data/'):
            item_id = int(self.path.split('/')[-1])
            for i, item in enumerate(data):
                if item['id'] == item_id:
                    del data[i]
                    self.send_response(204)
                    self.end_headers()
                    break
            else:
                self.send_error(404)
        else:
            self.send_error(404)


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
    print("Server started at localhost:8001")
    httpd.serve_forever()
