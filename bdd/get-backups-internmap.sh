#!/bin/bash
# On another server, who have access to the server who host the database
# crontab -e : 0 4 * * * sh get-backups-internmap.sh

FOLDER="."
BDD_SERVER="bdd-internmap"

rm -rf $FOLDER/backup-internmap

# ssh connection with specific config file
scp -r $BDD_SERVER:backup-internmap $FOLDER