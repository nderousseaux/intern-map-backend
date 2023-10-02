#!/usr/bin/env bash
service nginx start
uwsgi --ini build/uwsgi.ini