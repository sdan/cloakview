FROM python:3.6
COPY . ./
RUN cd ./
RUN LC_ALL=C.UTF-8 LANG=C.UTF-8 pip install -r requirements.txt
CMD LC_ALL=C.UTF-8 LANG=C.UTF-8 streamlit run Cloakview.py

EXPOSE 8502
