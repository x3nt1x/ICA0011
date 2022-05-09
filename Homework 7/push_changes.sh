#!/bin/bash

# Dump local database
sudo mysqldump -u root -p local_database_name > db_dump.sql

# Fix dump to match Heroku's database formatting
sed -i 's/utf8mb4_0900_ai_ci/utf8_general_ci/g' db_dump.sql
sed -i 's/CHARSET=utf8mb4/CHARSET=utf8/g' db_dump.sql

# Push local database to Heroku
sudo mysql -h heroku_host -u heroku_database_username -pheroku_database_password heroku_database_name < db_dump.sql

# Delete dump
rm db_dump.sql

# Push changes to GitHub
git add .
git commit -m "Comment"
git push