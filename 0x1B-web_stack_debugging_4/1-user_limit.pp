# This Puppet manifest changes the OS configuration to increase the file descriptor limit for the holberton user.

exec {'OS security config':
command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
