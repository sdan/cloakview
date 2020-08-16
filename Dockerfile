FROM tensorflow/tensorflow:1.15.2-gpu-py3

RUN apt-get update
RUN apt-get install -y pkg-config libfontconfig1-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgles2-mesa-dev
RUN apt install libgl1-mesa-glx 
RUN pip install --upgrade pip
RUN apt install sed
COPY . .
RUN python setup.py install
