  cd "C:\DNAC monitoring App"
  git pull
  "C:\DNAC monitoring App\dnac_monitoring\venv\Scripts\activate.bat"
  pip install -r requirements.txt
  ./manage.py migrate
  httpd -k restart
  exit