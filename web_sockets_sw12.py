import socket
import sys  
import tramas 


port = 4001  # web
ip = '192.168.2.97'
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MySocketSW12:
    def __init__(self, ip_target):
        self.rx_var_formated = []
        self.__rx_var = bytearray(2048)
        self.__rx_num = 0
        self.__num = 11
        self.__ips_connected = []
        self.__port = 4001
        self.ip_target = ip_target
        self.__tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connect()
    def __connect(self):
        try:
            self.__tcpSocket.connect((self.ip_target,self.__port))
        except socket.error:
            sys.exit()
    def readPendingDatagrams(self,__frame):
        self.__tcpSocket.sendto(__frame,(self.ip_target,self.__port))
        reply = self.__tcpSocket.recv(1024)
        self.rx_var_formated = []
        data = list(reply)
        if (data[8]== 131):
            for i in range(11,len(data)-2):
                self.rx_var_formated.append(data[i])
            return True
        else:
            print("trama incorrecta")
            return False
    def getFases(self):
        try:
            if(self.readPendingDatagrams(tramas.fases_frame)):
                print("Fases Obtenidas")
                fases_data = []
                counter = 0
                for i in self.rx_var_formated:
                    counter +=1
                    fase = {'id':'fase-{}'.format(counter),'value':i}
                    fases_data.append(fase)
                return fases_data
        except socket.error:
            sys.exit()
    def getPlanes(self):
        pass
    def disconnect(self):
        self.__tcpSocket.close()


tcp_client = MySocketSW12('192.168.2.97')
fases = tcp_client.getPlanes()
print(fases)
tcp_client.disconnect()

