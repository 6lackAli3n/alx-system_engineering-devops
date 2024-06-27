# This Puppet manifest configures Nginx to handle more simultaneous requests by adjusting worker connections and worker processes.

exec {'modify max open files limit setting':
command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
