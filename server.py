import  cv2 , socket , time , threading as th

global conn,address , flag
flag =  0

def accept_req():
    global conn,address , flag
    while True:
        server.listen()
        # print('Waiting......')
        conn , address = server.accept()
        
        data_recv_th = th.Thread(target=data_recv)
        data_recv_th.start()
        flag = 1

def data_recv():
    global conn,address,flag
    while True:
        if flag:
            # print('Receiving from ',address)
            client_data = conn.recv(1024)
            if len(client_data)>0:
                print(address , ' : ' , client_data.decode())


host , port = '' , 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created...')

server.bind((host,port))
print('Server is ready....')

accept_th = th.Thread(target=accept_req)
# data_recv_th = th.Thread(target=data_recv)

accept_th.start()
# data_recv_th.start()