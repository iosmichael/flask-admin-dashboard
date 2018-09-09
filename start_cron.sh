cd ~/admin
export FLASK_APP=cron_jobs.py
export FLASK_ENV=production
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
/usr/local/bin/flask run --host=0.0.0.0 --port=5002
