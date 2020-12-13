FROM daisukekobayashi/darknet:gpu


RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
python-dev python-pip

ADD ../model /root/model
ADD ../apply_net.py /root/apply_net.py

WORKDIR /root
CMD [ "/bin/bash" ]