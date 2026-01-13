#!/bin/sh

# Retry until DB is reachable
until flask db upgrade; do
  echo "Database not ready, retrying in 5s..."
  sleep 5
done

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:80 "app:create_app()"