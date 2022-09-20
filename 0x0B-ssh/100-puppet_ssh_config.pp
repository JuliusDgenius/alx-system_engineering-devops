# makes changes to config filr using puppet
file_line {'Turn off passwd auth':
  ensure => 'present',
  path 	 => '/etc/ssh/ssh_config',
  line	 => '	PasswordAuthentication no',
  match	 => 'PasswordAuthentication yes'
}
file_line {'Declare identify file':
  ensure => 'present',
  path	 => '/etc/ssh/ssh_config',
  line	 => '	IdentifyFile ~/.ssh.school',
}
