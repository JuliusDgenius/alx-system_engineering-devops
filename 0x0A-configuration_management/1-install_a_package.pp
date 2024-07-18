# Ensure pip3 is installed
package { 'python3-pip':
    ensure => installed,   
}

# Install flask from pip3 using puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require => Package['python3-pip'],
}

package { 'Werkzeug':
    ensure => '2.1.1',
    provider => 'pip3',
    
}
