FROM python:3.9.5

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /code

WORKDIR /code

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD [ "gunicorn", "eshop.wsgi:application", "--bind", "0.0.0.0:8000" ]