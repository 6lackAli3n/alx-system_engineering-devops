# This Puppet manifest ensures that the required directory for Apache is present and has the correct permissions

exec { 'fix-wordpress':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => '/usr/local/bin/:/bin/'
}
