import message_pb2
import message_pb2_grpc

import time

import grpc
import socket

SERVER_IP = "localhost"
 
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
 
def health_check_connection():
    with grpc.insecure_channel(f'{SERVER_IP}:50051') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)

        print("\t[INFO] Health Check Response (0): ")
        response = stub.HealthCheck(message_pb2.Empty())


        print("\t[INFO] Health Check Response: ")
        if(response.status == 0):
            print("\t[OK] Connection to server established! ")
            return True
        else:
            print("\t[ERROR] Connection to server failed! ")
            return False

def run(msg, sender="Python Client"):
    with grpc.insecure_channel(f'{SERVER_IP}:50051') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
            #MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        #response = stub.SendMessage(message_pb2.MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        response = stub.SendMessage(message_pb2.SimpleMessage( message=msg, sender=sender, timestamp=str(int(time.time())) ) )
        if(response.status == 0):
            print("\t[OK] Message Received! ")
        else:
            print("\t[ERROR] Message not received! ")
    

if __name__ == '__main__':
    print("Starting the message client...")
    if not health_check_connection():
        print("Exiting...")
        exit(1)
    print("Welcome to the message client!")
    print(f"\tYour IP is: {get_local_ip()}")
    print("\tPress Ctrl+C to exit at any time.")
    name = input("\tEnter your name (blank for default): ")
    if name == "":
        name = "Python Client"
    while True:
        run(input("Enter the message: "), name)