# To create a Puppet manifest that kills a process named "killmenow" using the exec resource and pkill,

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}
