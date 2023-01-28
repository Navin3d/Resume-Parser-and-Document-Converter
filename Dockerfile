FROM ubuntu

WORKDIR ./program/resume_parser

RUN apt-get update && apt upgrade -y
RUN apt-get install python3 --yes
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-venv
RUN apt-get install libreoffice-writer -y

RUN python3 -m venv venv
RUN . venv/bin/activate
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY ./ ./

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# resume-parser-and-document-converter