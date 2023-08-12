FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN pip install -r requirements.txt &&\
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. src/protos/protobuf.proto &&\
	echo "Done!"
CMD ["python", "main.py"]