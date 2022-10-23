import  cv2 , socket , time , threading as th


def accept_req():
    while True:
        msg = input('Enter : ')
        if len(msg)>0:
            client.send(str.encode(msg))

def data_recv():
    for i in range(50):
        print('receiving')
        time.sleep(1)


# username = input('Enter  your name : ')

# host , port = '3.6.122.107' , 16081
host , port = 'localhost' , 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created...')

client.connect((host,port))
print('connected...to the host : ',socket.gethostname())

accept_th = th.Thread(target=accept_req)
data_recv_th = th.Thread(target=data_recv)

accept_req()
# accept_th.start()
# data_recv_th.start()