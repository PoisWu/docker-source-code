FROM psmae/ubuntu-python
RUN echo "This container is a single-connection server" > ./INFO
ADD . /opt/
EXPOSE 55555
CMD ["python", "/opt/server.py"]

