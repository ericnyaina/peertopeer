import socket as sk

conn_srv = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

conn_srv.connect(('localhost', 12800))