from http.server import BaseHTTPRequestHandler
import socketserver
from cosine import main as execute
from fetch import fetch

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        if(self.path == "/favicon.ico"):
            return
        x=0
        if self.path != "/":
            x = float(self.path[1:])
        
        execute(x,10)
        y = fetch(x)
        
        self.wfile.write(str(y).encode()) 
        
def main():
    port = 1235
    host = "localhost"
    httpdaemon = socketserver.TCPServer( (host, port), SimpleHTTPRequestHandler)
    print("Serving at:",str(host)+":"+str(port))
    httpdaemon.serve_forever()        
        
if __name__ == "__main__":
    main()
