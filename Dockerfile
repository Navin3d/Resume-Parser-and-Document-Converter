FROM ubuntu

WORKDIR ./program/resume_parser

RUN apt update && apt upgrade -y
RUN apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
RUN mkdir /python && cd /python
RUN wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0a1.tgz
RUN tar -xvf Python-3.12.0a1.tgz
RUN cd Python-3.12.0a1S
RUN ./configure --enable-optimizations
RUN make install

#RUN apt install python3
RUN pip install virtualenv

RUN python3 -m venv venv
RUN source venv/bin/activate
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver"]
