#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

HOST = 'localhost'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
try:
    s.connect((HOST, PORT))

    try:
        while True:
            outdata = input('please input message: ')
            if not outdata:
                break
            print('send: ' + outdata)
            s.send(outdata.encode())
            
            indata = s.recv(1024)
            if len(indata) == 0: # connection closed
                s.close()
                print('server closed connection.')
                break
            print('recv: ' + indata.decode())
        
    except KeyboardInterrupt:
                print('client stop')
                
except ConnectionRefusedError as error:
    print("ERROR",error)

