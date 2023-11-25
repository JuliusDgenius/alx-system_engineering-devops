# Creating a file with puppet in /tmp directory

file { '0-create_a_file':
  path     => '/tmp/school',
  owner    => 'www-data',
  group    => 'www-data',
  mode     => '0744',
  content  => 'I love Puppet',
}
