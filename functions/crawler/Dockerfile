FROM lambci/lambda:build-python2.7

ENV AWS_DEFAULT_REGION ap-northeast-2
ENV APP_DIR /var/task

ADD . .

CMD pip install -r requirements.txt -t $APP_DIR && \
  zip -9 quiettime.zip living_life_crawler.py && \
  zip -9 quiettime_crawler.zip daily_bible_crawler.py && \
  zip -r9 quiettime_crawler.zip *
