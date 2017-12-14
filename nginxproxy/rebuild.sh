#!/bin/bash
set -e
echo "Note, this does not renew the cert, use renewcert.sh for that"
docker build -t nginxproxy .
docker rm nginxproxy && docker run -d --name nginxproxy --restart unless-stopped -p 80:80 -p 443:443 --link QQQBACKENDQQQ:backend nginxproxy
