FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pytest

CMD "python" "game.py"