#!/bin/sh

set -e 

echo "Starting SSH ..."
service ssh start

# Start Django with Gunicorn
exec gunicorn -b 0.0.0.0:8000 --chdir /app unsplash.wsgi --timeout 600