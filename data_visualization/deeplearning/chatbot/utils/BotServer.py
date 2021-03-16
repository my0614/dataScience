import socket

class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port))) #결합
        self.mySock.listen(int(self.listen)) #준비
        return self.mySock
    
    def ready_for_clinet(self):
        return self.mySock.accept() # 연결하기

    def get_sock(self):
        return self.mySock
    
