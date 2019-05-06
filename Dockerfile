FROM python:3.6-slim-stretch

EXPOSE 3000

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    python3-dev \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    git clone https://github.com/ageitgey/face_recognition && \
    cd  face_recognition/ && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

# For the web app
RUN pip install flask-restful && \
    pip install imagehash

RUN cd /

COPY face_reco.py face_reco.py

ENTRYPOINT ["python","face_reco.py"]