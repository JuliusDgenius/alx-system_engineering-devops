#!/usr/bin/env bash
# makes changes to config file using puppet
file_line {
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication yes',
    match  => 'PasswordAuthentication yes',
}
file_line {'Declare identity file':
    ensure => 'present'
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}
