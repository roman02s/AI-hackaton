import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import grpc
from src.protos.protobuf_pb2_grpc import ServiceServicer, ServiceStub
from src.protos.protobuf_pb2 import Empty, Message, IsValid

import src.handler

app = FastAPI()


# @app.get("/message")
# def prepare_message_from_client(message: Message) -> Message:
# 	channel = grpc.insecure_channel("localhost:8080")
# 	client = ServiceStub(channel)
# 	request = ServiceServicer.PrepareMessage(message)
# 	# TODO: add logic
# 	response = client.SendMessage(request)
# 	return response


if __name__ == "__main__":
	channel = grpc.insecure_channel("localhost:8080")
	client = ServiceStub(channel)
	request = ServiceServicer.PrepareMessage(message)
	# TODO: add logic
	response = client.SendMessage(request)

	# uvicorn.run(app, host="0.0.0.0", port=8000)
