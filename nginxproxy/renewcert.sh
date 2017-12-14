#!/bin/bash
#
# Automatically get a new SSL certificate from Let's Encrypt
#
set -e

domain="QQQDOMAINQQQ"
email="QQQEMAILQQQ"

mkdir -p letsencrypt
docker run --rm -p 443:443 --mount "src=$(pwd)/letsencrypt,target=/etc/letsencrypt,type=bind" \
	certbot/certbot certonly --standalone --domain ${domain} -m ${email} --agree-tos
cp letsencrypt/live/${domain}/*.pem etc/
