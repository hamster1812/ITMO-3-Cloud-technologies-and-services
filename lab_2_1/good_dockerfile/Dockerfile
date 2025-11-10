FROM python:3.13-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY calc.py .
RUN chmod +x calc.py

CMD ["python", "calc.py"]