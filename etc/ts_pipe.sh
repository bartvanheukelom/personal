#!/bin/bash
# pipe any output stream into this script to prepend the current timestamp to each line
exec perl -pe 'use POSIX strftime; print strftime "[%Y-%m-%d %H:%M:%S] ", localtime'
