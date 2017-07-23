FROM python:2.7-alpine

ADD https://github.com/alexellis/faas/releases/download/0.5.1-alpha/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

COPY handler.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV fprocess="python handler.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
