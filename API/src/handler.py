import grpc

from src.protos.protobuf_pb2_grpc import ServiceServicer, ServiceStub
from src.protos.protobuf_pb2 import Message


class BaseService(ServiceServicer):
	def PrepareMessage(self, request: Message, context: grpc.ServicerContext) -> Message:
		raise NotImplementedError
