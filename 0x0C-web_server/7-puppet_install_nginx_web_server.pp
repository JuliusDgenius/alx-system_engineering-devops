# Practice configuring a web server with puppet.
# Install Nginx with puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me https://juliusdgenius-alx.tech permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
