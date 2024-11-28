FROM python:3.12-slim
WORKDIR /app
COPY . /app
ENV PYTHONPATH /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5555
CMD ["python", "src/app.py"]