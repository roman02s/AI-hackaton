from fast_grpc import BaseSchema, FastGRPC, ServicerContext, method

app = FastGRPC()

class HelloRequest(BaseSchema):
    name: str

class HelloReply(BaseSchema):
    message: str

class Greeter:
    @method("SayHello", request_model=HelloRequest, response_model=HelloReply)
    async def say_hello(self, request: HelloRequest, context: ServicerContext) -> HelloReply:
        return HelloReply(message=f"Greeter SayHello {request.name}")

app.add_service(Greeter)
# this step will generate .proto file and python gRPC code, then start a grpc server
app.run()