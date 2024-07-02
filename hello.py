from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8888

class HandlerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h3>Hello World</h3>")

serv = HTTPServer(('', PORT), HandlerClass)
print('HTTP Server started...[', PORT, ']')
serv.serve_forever()
