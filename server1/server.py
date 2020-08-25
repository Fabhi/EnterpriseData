from http.server import BaseHTTPRequestHandler
import socketserver
import os

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
            
        os.system("echo "+str(x)+" > in.txt"  )
        os.system('gfortran sine.f95');
        os.system('./a.out < in.txt > out.txt')
        handle = open("out.txt","r") 
        y = round(float(handle.read().strip()),4)
        self.wfile.write(str(y).encode()) 
        os.system("rm in.txt out.txt a.out")
        
def main():
    port = 1234
    host = "localhost"
    httpdaemon = socketserver.TCPServer( (host, port), SimpleHTTPRequestHandler)
    print("Serving at:",str(host)+":"+str(port))
    httpdaemon.serve_forever()        
        
if __name__ == "__main__":
    main()
