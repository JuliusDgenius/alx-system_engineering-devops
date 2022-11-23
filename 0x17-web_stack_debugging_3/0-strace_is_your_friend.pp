# Fixes 'phpp' error to 'php' with a WordPress Website
exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin'
}
