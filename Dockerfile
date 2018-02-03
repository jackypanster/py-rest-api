FROM python:3.6.4-alpine3.7

# Install all build dependencies
# Add bash for debugging purposes
#RUN apk update && apk add build-base
RUN apk add libev-dev

WORKDIR /

RUN mkdir /log

COPY app.py /app.py
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3","/app.py" ]