FROM python:3.13-slim

COPY requirements.txt calc.py ./
RUN pip install -r requirements.txt && \
    chmod +x calc.py

CMD ["python", "calc.py"]