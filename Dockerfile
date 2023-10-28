FROM python:latest

# TODO: Add your image build instructions here
# /src
WORKDIR / 
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /src .
COPY /data /data
