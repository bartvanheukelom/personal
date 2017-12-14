#!/bin/bash
#
# Automatically get a new SSL certificate from Let's Encrypt
#
set -e

# settings
domain="QQQDOMAINQQQ"
email="QQQEMAILQQQ"


ledir="$(pwd)/letsencrypt"
destdir="etc"

# acquire certificate
docker run --rm -p 443:443 --volume "${ledir}:/etc/letsencrypt" \
	certbot/certbot certonly --standalone --domain ${domain} -m ${email} --agree-tos

# copy to destination
cp "${ledir}/live/${domain}/*.pem" "${destdir}/"
