#!/bin/bash

#rm *.tar.gz bugzilla.sql appdb.sql

c_date="$(date +%Y%m%d)"
c_date=$((date - 1))
c_date="20130606"

#wget ftp://ftp.winehq.org/pub/wine/wine-appdb-${c_date}.tar.gz
#wget ftp://ftp.winehq.org/pub/wine/wine-bugzilla-${c_date}.tar.gz

#tar -xzvf ./wine-appdb-${c_date}.tar.gz
#tar -xzvf ./wine-bugzilla-${c_date}.tar.gz

echo "Flushing DB"
mysql -u root -p appdb < flush_db.sql
echo $?

echo "Importing DB"
mysql -u root -p appdb < appdb.sql
echo $?
mysql -u root -p appdb < bugzilla.sql
echo $?

echo "Cleanup..."
mysql -u root -p appdb < cleanup_db.sql 
echo $?
