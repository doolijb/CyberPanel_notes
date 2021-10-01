## Check newest version

```url
https://www.litespeedtech.com/open-source/litespeed-sapi/download
```

## Install

```
cd ~
curl -O http://www.litespeedtech.com/packages/lsapi/wsgi-lsapi-1.9.tgz
tar xf wsgi-lsapi-1.9.tgz
cd wsgi-lsapi-1.9
python3 ./configure.py
make
cp lswsgi /usr/local/lsws/fcgi-bin/
cd ~
rm -r wsgi-lsapi-1.9
rm -r wsgi-lsapi-1.9.tgz
```
