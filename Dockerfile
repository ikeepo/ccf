FROM zauberzeug/nicegui:1.4.18


COPY . /app
RUN apt-get update \
  && apt-get -y install graphviz \ 
  && apt-get clean

RUN pip install -r /app/requirements.txt

