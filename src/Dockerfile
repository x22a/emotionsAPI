FROM python:3.8.1

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN python3 nltk-requirements.py

CMD ["python3","api.py"]