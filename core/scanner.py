import threading
import socket,time
from threading import Thread,Lock


class Scanner:

	def __init__(self):
		self.workers = []
		self.port_list = [ i for i in range(65536)]

		
	def ip_is_valid(self,ip):
		if(ip.lower().strip() == "localhost"):
			return True;
		ip_p = ip;

		ip = ip.split('.')
		if(len(ip) != 4):
			return False
		for i in ip:
			if(not i.isdigit()):
				return False;
			if(int(i) > 255):
				return False;

		try:
			a = socket.gethostbyaddr(ip_p)
		except Exception as e:
			return False

		return True;


	def worker(self,ip,load,callback):
		for port in load:
			# print(f"Trying port {port}")
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
			if(s.connect_ex((ip,port)) == 0):
				callback([port,""])
			s.close()



	def start_scan(self,ip,callback):
		if(not self.ip_is_valid(ip)):
			raise Exception("Invalid IP Address")


		# from 0 - 65535
		# create 12 threads and each thread should handle 5120 ports 

		i = 0;
		for h in range(12):
			load = self.port_list[i:i+5120]
			i+=5120
			thread = Thread(target=self.worker,args=(ip,load,callback))
			thread.daemon = True;
			thread.setDaemon(True);
			thread.start()
