FROM python:3.6.4-alpine3.7

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
# Install all build dependencies
RUN apk update && apk add build-base libev-dev

WORKDIR /

RUN mkdir /log

COPY app.py /app.py
COPY requirements.txt /requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3","/app.py" ]
