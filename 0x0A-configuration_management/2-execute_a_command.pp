# Puppet manifest to kill a process named "killmenow"

exec { 'pkill':
  command     => 'pkill -9 -f killmenow || true',
  path        => ['/usr/bin', '/usr/sbin', '/bin'],
  refreshonly => true,
}
