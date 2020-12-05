import socket as sk
import sys
from threading import Thread
import time

id_port = 12800

class serveur(Thread):

    def __init__(self):
		Thread.__init__(self)
		self.conn = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
		self.conn.bind(('', id_port))
		self.conn.listen(5)

    def run(self):
        
		while 1:
			conn_client, infos_conn = self.conn.accept()
			print "on recoit un nouveau client : " + str(infos_conn)
			
srv = serveur()
srv.start()


