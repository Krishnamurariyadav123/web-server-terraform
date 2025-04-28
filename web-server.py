import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Ensure this is pointing to the folder containing your 'index.html'
directory = os.path.abspath('.')  # This sets it to the current directory

os.chdir(directory)  # Change the working directory

# Create the server and handle requests
handler = SimpleHTTPRequestHandler
httpd = TCPServer(("", 8080), handler)

print("Starting web server on port 8080...")
httpd.serve_forever()
