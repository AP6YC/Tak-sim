import socket,sys
from Communicator import Communicator

class Server:
	def __init__(self):
		self.communicator_list = []

	def BuildServer(self,port_no,num_clients):
		s = socket.socket()
		host = socket.gethostname()
		self.port = port_no
		s.bind((host,port_no))
		s.listen(5)
		client_count = 0
		while client_count < num_clients:
			# -- Change this for multi client games -- #
			c,addr = s.accept()
			client_count += 1
			self.communicator_list.append(Communicator())
			self.communicator_list[-1].setSocket(c)						
	
	def RecvDataFromClient(self,client_id):
		# -- TODO: INDEX CHECKING ---- #
		return self.communicator_list[client_id].RecvDataOnSocket()

	def SendData2Client(self,client_id,data):
		# -- TODO: INDEX CHECKING ---- #
		self.communicator_list[client_id].SendDataOnSocket(data)

	def CloseClient(self,client_id):
		# -- TODO: INDEX CHECKING ---- #
		self.communicator_list[client_id].closeSocket()

if __name__ == '__main__':
	print 'Start'
	local_Server = Server()
	local_Server.BuildServer(int(sys.argv[1]),2)
	while 1:
		num_from_0 = local_Server.RecvDataFromClient(0)
		local_Server.SendData2Client(1,num_from_0)
		num_from_1 = local_Server.RecvDataFromClient(1)
		local_Server.SendData2Client(0,num_from_1)
		if(int(num_from_1) == 100):
			local_Server.SendData2Client(1,str(int(num_from_1) + 1))
			break
	local_Server.CloseClient(0)
	local_Server.CloseClient(1)



