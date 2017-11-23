#!/bin/bash
set -e
echo "RSNAPHOT"
echo "Going to perform backup..."
sudo rsnapshot -c Dropbox.conf -v daily
echo "Backup completed! Calculating disk usage..."
du -sh Dropbox/*
echo "Press any key to quit"
read
