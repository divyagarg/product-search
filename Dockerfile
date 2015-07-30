FROM ubuntu
MAINTAINER prince <prince@askme.in>

# basics
RUN apt-get update && apt-get install -y python python-dev build-essential python-pip
ADD . /app
WORKDIR /app

# install requirements
RUN pip install -r requirement.txt
EXPOSE 9000
RUN chmod +x /app/start.sh
# launch application
CMD ["/app/start.sh"]
# $ docker run -d -p 9000:9000 proj
