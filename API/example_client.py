import grpc
import src.protos.protobuf_pb2 as pb2
import src.protos.protobuf_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.ServiceStub(channel)
    request = pb2.Message()
    # Заполнение полей запроса
    request.sender = "Отправитель"
    request.recipient = "Получатель"
    request.content = "Содержимое сообщения"
    request.timestamp = 1234567890
    response = stub.PrepareMessage(request)
    # Обработка ответа
    print("Ответ сервера:")
    print("Отправитель:", response.sender)
    print("Получатель:", response.recipient)
    print("Содержимое:", response.content)
    print("Временная метка:", response.timestamp)

if __name__ == '__main__':
    run()
