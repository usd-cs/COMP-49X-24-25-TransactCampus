FROM python:3.12

WORKDIR /usr/local/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=5001

ENV PATH="/home/app/.local/bin:$PATH"

RUN useradd -m app

USER app

EXPOSE 5001

CMD ["flask", "run"]
