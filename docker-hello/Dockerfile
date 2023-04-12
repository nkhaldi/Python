FROM python:3.7.2-alpine3.8
ENV WORK_DIR="sandbox"
RUN  mkdir WORK_DIR
RUN  cd  WORK_DIR
WORKDIR  /WORK_DIR
ADD hello.py .
CMD ["python3", "hello.py"]