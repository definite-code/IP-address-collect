from alpine:latest

RUN apk update
RUN apk add --no-cache python3-dev
RUN apk add py-pip

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["collect_ipaddress_iot.py"]