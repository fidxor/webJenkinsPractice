FROM	ubuntu:22.04
LABEL	maintainer="Donkey"
RUN	apt-get update && apt-get install -y python3
COPY	hello.py /
EXPOSE	8888
CMD	["python3", "/hello.py"]
