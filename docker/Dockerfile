FROM python:3.10
ENV PYTHOMUNBFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --upgrade pi && \
    pip install pipenv && \
    pipenv install --system --dev --deploy
