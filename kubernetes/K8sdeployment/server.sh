#!/bin/bash
gunicorn -b 0.0.0.0:8000 -w 2 --threads 2 --timeout 1800 main:app