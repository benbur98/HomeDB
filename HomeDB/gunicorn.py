"""Gunicorn Config file"""

wsgi_app = "HomeDB.wsgi:application"

# The socket to bind
bind = "0.0.0.0:8099"

# The number of worker processes for handling requests
workers = 2
# Restart workers when code changes (development only!)
reload = True

# The granularity of Error log outputs
loglevel = "debug"
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"

# Redirect stdout/stderr to log file
capture_output = True

# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"

# Daemonize the Gunicorn process (detach & enter background)
daemon = True