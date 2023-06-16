FROM python:3.9-slim

WORKDIR /usr/app/src
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ .
ADD https://neurons-lab-public-bucket.s3.eu-central-1.amazonaws.com/lilia_digital_avatar.mp4 ./media/
ADD https://neurons-lab-public-bucket.s3.eu-central-1.amazonaws.com/igor_rotate.mp4 ./media/
ADD https://neurons-lab-public-bucket.s3.eu-central-1.amazonaws.com/alex_rotate.mp4 ./media/
RUN ls -la --recursive .
EXPOSE 80

CMD ["streamlit", "run",\
    "--browser.serverAddress", "0.0.0.0",\
    "--server.enableCORS", "False",\
    "--server.port", "80",\
    "/usr/app/src/Home.py"]
