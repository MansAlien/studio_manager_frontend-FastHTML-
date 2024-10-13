FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update

RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt /app/
RUN pip install python-fasthtml
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

COPY . .

# create a CMD to run the django project server
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5001"]
CMD ["python", "main.py"]
