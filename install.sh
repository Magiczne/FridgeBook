#!/usr/bin/env bash

printf "===================================\n"
printf "      FridgeBook installation\n"
printf "===================================\n"
printf "\n\n"

# Migrate database
printf "====== Database ======\n"
python manage.py migrate
printf "\n\n"

# Create superuser with
printf "====== Administrator ======\n"
printf "Please specify password for admin\n"
python manage.py createsuperuser --username=admin --email ""
printf "\n\n"

# Application successfully installed
printf "====== Installation successful ======\n"
printf "Application successfully installed\n"
