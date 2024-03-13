FROM zauberzeug/nicegui:1.4.18


COPY . /app

RUN pip install -r /app/requirements.txt

