FROM python:3.10-slim

WORKDIR /app
COPY . .

EXPOSE 80

RUN source ./scrips/script.sh &&\
	pip install -r requirements.txt

CMD ["python", "main.py"]
# sudo docker build -t tg:v1 .
# sudo docker run -d --restart unless-stopped -p 80:80 -t --name tg_bot tg:v1