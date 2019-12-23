FROM python:3

RUN git clone http://dengyuting:dyt_123456@gitlab.fjmaimaimai.com/dengyuting/ability_api.git /ability_api&& cd /ability_api && git pull
WORKDIR /ability_api

RUN pip install --no-cache-dir -r requirements.txt

RUN hrun testsuites/ability_suites.yml --save-tests

CMD [ "python", "sendmsg.py" ]