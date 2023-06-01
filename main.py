import socket
import sys  
import tramas 


port = 4001  # web
ip = '192.168.2.97'
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




def getFases(remote_ip,port):
    host = (remote_ip,port)
    try:
        tcp_client.connect(host)
        tcp_client.sendto(tramas.fases_frame,host)
        reply = tcp_client.recv(1024)
        data = list(reply)
        print(data)
        tcp_client.close()
        
    except socket.error:
        print('Send failed')
        sys.exit()


getFases(remote_ip=ip,port=port)

