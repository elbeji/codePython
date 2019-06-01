#import http.server
#import socketserver
#port=80
#address=("",port)
#handler = http.server.SimpleHTTPRequestHandler
#httpd=socketserver.TCPServer(address,handler)
#print("serveur demmarer sur le port {port}")

#hhtpd.serve_forever()


import http.server
port=80
address=("",port)
server = http.server.CGIHTTPRequestHandler
httpd=socketserver.TCPServer(address,handler)
print("serveur demmarer sur le port {port}")

hhtpd.serve_forever()

