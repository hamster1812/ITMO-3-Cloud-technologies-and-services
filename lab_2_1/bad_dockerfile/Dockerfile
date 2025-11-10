FROM python:latest

COPY . .

RUN pip install -r requirements.txt
RUN chmod +x calc.py

CMD ["python", "calc.py"]