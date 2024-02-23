from concurrent import futures
import time

import grpc
import message_pb2
import message_pb2_grpc

class MessageServicer(message_pb2_grpc.MessageService):
    def SendMessage(self, request, context):
        print(f"Received message: {request.message} from {request.sender} at {request.timestamp}")
        #send_message_reply = message_pb2.MessageReply(message=f'[{time.strftime("%H:%M:%S")}] {request.message} received! - {request.name})')
        response = message_pb2.StateMessage(status=message_pb2.state.OK, message="Message received successfully")
        return response
    def HealthCheck(self, request, context):
        return super().HealthCheck(request, context)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()