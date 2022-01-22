#!/bin/bash
gunicorn -b 0.0.0.0:5000 -w 2 --threads 2 --timeout 60 app:app