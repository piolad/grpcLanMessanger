import time

import message_pb2
import message_pb2_grpc
import grpc


def run(msg):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
            #MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        #response = stub.SendMessage(message_pb2.MessageRequest(message=msg, name="Python Client", timestamp=int(time.time())))
        response = stub.SendMessage(message_pb2.SimpleMessage(message=msg, sender="Python Client", timestamp=str(int(time.time()))))
        print("Message Sent: ")
        print(f"\tstatus: {response.status}")
        print(f"\tmessage: {response.message}")
    

if __name__ == '__main__':
    while True:
        run(input("Enter the message: "))