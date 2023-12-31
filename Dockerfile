FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["streamlit", "run", "dashboard/app.py"]

EXPOSE 80