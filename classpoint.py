#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection


   
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close()             

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print ("destroyed")

pt1 = Point()
pt2 = Point()
pt3 = Point()
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts


#!/usr/bin/python
import time;  # This is required to include time module.
import calendar
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
cal1 = calendar.month(1977, 9)
cal2 = calendar.month(1986, 2)
cal3 = calendar.month(2017, 5)

print(cal1 ,  cal2 , cal3)

import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

