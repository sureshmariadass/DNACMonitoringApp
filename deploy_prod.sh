#!/bin/sh

sshpass -p C1sc0123 ssh -tt -o StrictHostKeyChecking=no root@10.171.92.112 <<EOF
  cd /DNAC/
  git pull
  virtualenv env -p python3
  source ./env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  exit
EOF
