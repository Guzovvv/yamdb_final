FROM python:3.7-slim
RUN python3 -m pip install --upgrade pip
COPY ./ /app
RUN pip3 install -r /app/requirements.txt
WORKDIR /app/api_yamdb/
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]