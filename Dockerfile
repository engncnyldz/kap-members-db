FROM python:3.10.8

WORKDIR /usr/src/kap-members-db

RUN mkdir logs 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001"]