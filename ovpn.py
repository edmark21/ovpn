import os
import sys
os.system("clear")
logo = '''

********************************************************************************
                                  OVPN CONNECT
                                       v1
********************************************************************************
'''

print logo

name = raw_input("Enter ovpn path: ")
if name == "":
     print "Please enter ovpn filename.ovpn"

os.system("openvpn --config " + name)

