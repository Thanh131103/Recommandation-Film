FROM python:3.12
EXPOSE 8080
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./
ENTRYPOINT ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]

