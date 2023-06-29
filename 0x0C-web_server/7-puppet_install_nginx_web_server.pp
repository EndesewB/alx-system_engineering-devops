# Installs a Nginx server
package { 'nginx':
  ensure => 'installed',
}
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      server_name _;
      root /var/www/html;
      location / {
        return 200 "Hello World!\n";
      }
      location /redirect_me {
        return 301 https://example.com/new_page;
      }
    }
  ',
  notify  => Service['nginx'],
}
