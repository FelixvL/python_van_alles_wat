from http.server import HTTPServer, BaseHTTPRequestHandler

class abc(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write("hello ".encode())

def main():
    PORT = 8000
    server = HTTPServer(('',PORT), abc)
    print('Server running 8000')
    server.serve_forever()

if __name__ =='__main__':
    main()