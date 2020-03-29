FROM python:3.8-alpine
RUN apk add --no-cache bash libexif udev chromium chromium-chromedriver xvfb
RUN pip install --no-cache-dir boto3 beautifulsoup4 selenium
WORKDIR /app
COPY . .
