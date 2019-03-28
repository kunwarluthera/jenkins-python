FROM python:3.7.2-alpine
EXPOSE 5000
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ ./
CMD ["python", "./app.py"]