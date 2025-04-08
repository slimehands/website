#!/bin/bash

sleep 30

# Define the new IP address
NEW_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

# Define the Nginx configuration file path
NGINX_CONFIG_FILE="/etc/nginx/sites-available/solar-car-latest"

# Replace the IP address in both server blocks
sudo sed -i "s/server_name .*;/server_name $NEW_IP;/" $NGINX_CONFIG_FILE

# Reload Nginx to apply the changes
sudo systemctl reload nginx

sleep 3

sudo systemctl reload nginx

echo "Nginx configuration updated with new IP: $NEW_IP"

