# To create a Puppet manifest that kills a process named\
# "killmenow" using the exec resource and pkill,

exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
