# Use official PHP with Apache
FROM php:8.2-apache

# Install mysqli extension (if not already available)
RUN docker-php-ext-install mysqli

# Copy current directory contents into the web root
COPY . /var/www/html/

# Make sure Apache listens on 80 (default)
EXPOSE 80

# Use default apache entrypoint; no CMD needed unless you want custom behaviour
