import os
import multiprocessing

current_path = os.path.dirname(os.path.abspath(__file__))
bind = '0.0.0.0:8080'
workers = multiprocessing.cpu_count() * 2 + 1
# threads = 2
name = 'myproject'
env = 'DJANGO_SETTINGS_MODULE=myproject.settings'
proc_name = 'myproject'
default_proc_name = proc_name
chdir = current_path
loglevel = 'debug'
accesslog = 'gunicorn.access'
errorlog = 'gunicorn.error'
timeout = 120
worker_class = 'meinheld.gmeinheld.MeinheldWorker'
