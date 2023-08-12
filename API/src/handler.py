import grpc

from src.protos.protobuf_pb2_grpc import ServiceServicer, ServiceStub
from src.protos.protobuf_pb2 import Empty, Message, IsValid


class BaseService(ServiceServicer):
	def PrepareMessage(self, request: Message, context: grpc.ServicerContext) -> IsValid:
		raise NotImplementedError

	def SendMessage(self, request: Message, context: grpc.ServicerContext) -> Empty:
		raise NotImplementedError

