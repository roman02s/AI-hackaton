import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.protos.protobuf_pb2_grpc import ServiceServicer, ServiceStub
from src.protos.protobuf_pb2 import Message

import grpc
from concurrent import futures
import src.protos.protobuf_pb2 as pb2
import src.protos.protobuf_pb2_grpc as pb2_grpc

from src.prepare_data import df_from_knowledge

from langchain_file import get_completion
from text2image import create_photo

app = FastAPI()

def generate_message(request: pb2.Message):
	df = df_from_knowledge()
	text = get_completion(f"Представь что клиент пришёл в пиццерию и хочет попробовать новое блюдо."
                                f" Опиши блюдо в пиццерии который соответствует описанию клиента: {message.text}"
                                f" Дай этому блюду креативное название и красивое краткое описание.")
    
	
@app.post("/prepare_message")
def prepare_message(request):
    # Создание gRPC канала и stub
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.ServiceStub(channel)


	# Вызов метода
	generate_message(request)
    # Вызов метода PrepareMessage
    response = stub.PrepareMessage(request)
    
    # Обработка ответа
    return {
        "sender": response.sender,
        "recipient": response.recipient,
        "content": response.content,
        "timestamp": response.timestamp,
    }


@app.get("/")
def root():
	return {"message": "Hello World"}


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8080)

# import grpc
# from concurrent import futures
# import src.protos.protobuf_pb2 as pb2
# import src.protos.protobuf_pb2_grpc as pb2_grpc

# class YourService(pb2_grpc.ServiceServicer):
#     def PrepareMessage(self, request, context):
#         # Обработка запроса и подготовка ответа
#         response = pb2.Message()
#         # Заполнение полей ответа
#         response.sender = "Отправитель"
#         response.recipient = "Получатель"
#         response.content = "Содержимое сообщения"
#         response.timestamp = 1234567890
#         return response

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     pb2_grpc.add_ServiceServicer_to_server(YourService(), server)
#     server.add_insecure_port('[::]:50051')
#     server.start()
#     server.wait_for_termination()

# if __name__ == '__main__':
#     serve()
