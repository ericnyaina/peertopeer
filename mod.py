import socket as sk

conn = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

conn.bind(('', 12800))
conn.listen(5)