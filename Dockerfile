FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY user.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./start.py" ]