#!/bin/bash
# On server who host the database
# crontab -e : 0 3 * * * cd backup-internmap && sh backup-local.sh

FOLDER="."

# Make a backup of the database
mysqldump internmap > $FOLDER"backup-internmap-"`date +"%d-%m-%Y"`.sql

# Delete backups older than 30 days
find $FOLDER -name "backup-internmap-*.sql" -mtime +30 -exec rm {} \;