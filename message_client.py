import time

import message_pb2
import message_pb2_grpc
import grpc
import socket

SERVER_IP = "LOACLHOST"
 
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 

def run(msg, sender="Python Client"):
    with grpc.insecure_channel(f'{SERVER_IP}:50051') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
            #MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        #response = stub.SendMessage(message_pb2.MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        response = stub.SendMessage(message_pb2.SimpleMessage( message=msg, sender=sender, timestamp=str(int(time.time())) ) )
        print("Message Received by server! ")
        print(f"\tstatus: {response.status}")
        print(f"\tmessage: {response.message}")
    

if __name__ == '__main__':
    print("Welcome to the message client!")
    print(f"\tYour IP is: {get_local_ip()}")
    print("\tPress Ctrl+C to exit at any time.")
    name = input("\tEnter your name (blank for default): ")
    if name == "":
        name = "Python Client"
    while True:
        run(input("Enter the message: "), name)