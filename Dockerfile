FROM python:3.11-slim
##docker build -t linkedin .
##docker run -itd -p 8602:8051 --env-file .env --name linkedinsearch linkedin
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
