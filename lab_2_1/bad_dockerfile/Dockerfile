FROM python:latest

COPY . .
RUN pip install -r requirements.txt && \
    chmod +x calc.py

CMD ["python", "calc.py"]