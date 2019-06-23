#!/usr/bin/env bash

export PATH=$PATH:/usr/pgsql-9.6/bin:/usr/local/bin
export DATABASE_NAME=$1
export BACKUP_PATH=$2
if [ -z "$DATABASE_NAME" ]
then
    echo "Enter database name as first argument"
    exit
elif [ -z "$BACKUP_PATH" ]
then
    echo "Enter backup path as second argument"
    exit
fi


pg_dump -Ft fennec > ${BACKUP_PATH}/database_`date +%d_%m_%Y`.tar
