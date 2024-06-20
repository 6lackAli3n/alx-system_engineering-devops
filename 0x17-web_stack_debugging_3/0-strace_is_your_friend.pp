# This Puppet manifest ensures that the required directory for Apache is present and has the correct permissions

exec { 'create-uploads-dir':
  command => '/bin/mkdir -p /var/www/html/uploads && /bin/chown -R www-data:www-data /var/www/html/uploads',
  unless  => '/bin/test -d /var/www/html/uploads',
}
