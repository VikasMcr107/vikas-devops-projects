from python:3.12-slim
workdir /app
copy . .
run pip install -r requirements.txt
expose 5000
CMD ["python", "app.py"]