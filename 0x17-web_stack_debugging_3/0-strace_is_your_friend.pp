# 0-strace_is_your_friend.pp

# Declare the exec resource to fix the issue
exec { 'fix-apache':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y php-module-name',
  onlyif  => '/usr/bin/dpkg --compare-versions $(/usr/bin/dpkg-query --showformat=\'${Version}\' --show php-module-name) ne desired_version',
}

# Notify the service to restart if the package is updated
service { 'apache2':
  ensure  => 'running',
  require => Exec['fix-apache'],
}
