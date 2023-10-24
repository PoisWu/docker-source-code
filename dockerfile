FROM ubuntu
RUN apt-get update && apt-get install -y \
    curl \
    python-is-python3
RUN echo "This container is a single-connection server" > ./INFO
ADD . /opt/
EXPOSE 55555
CMD ["python", "/opt/server.py"]

