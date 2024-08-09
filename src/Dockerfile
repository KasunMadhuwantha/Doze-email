FROM python:3.9.13

COPY . /usr/src/
WORKDIR /usr/src/

RUN mkdir -p /usr/src/log

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN python -u ./create_pipeline.py >> log.log

CMD ["python", "-u", "./email_automater.py", ">>", "output.log", "2>&1"]