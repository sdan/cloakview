FROM tensorflow/tensorflow:1.14.0-gpu-py3

RUN apt-get update
RUN apt-get install -y pkg-config libfontconfig1-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev libgles2-mesa-dev
RUN apt install libgl1-mesa-glx 
RUN pip install --upgrade pip
RUN apt install sed
COPY . .
RUN pip install -r ./fawkes/requirements.txt
CMD python start.py
