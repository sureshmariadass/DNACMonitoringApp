#!/bin/sh

sshpass -p C1sc0123 ssh -tt -o StrictHostKeyChecking=no root@10.171.92.112 <<EOF
  cd /usr/local/
  rm -rf dnac_app1
  mkdir dnac_app1
  cd dnac_app1
  git init
  git pull https://github.com/sureshmariadass/DNACMonitoringApp.git
  ls
  virtualenv uv_env -p python3
  source ./uv_env/bin/activate
  pip install -r requirements.txt
  chmod +x manage.py
  ./manage.py migrate
  ./manage.py collectstatic
  cd ..
  chmod 777 -rf dnac_app1
  systemctl restart apache2
  exit
EOF
