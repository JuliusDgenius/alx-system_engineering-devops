A Postmortem of Apache Error 500.

The apache server hosting a Wordpress website started returning error 500 due to a typocraphical error. The error occurred in a critical configuration file `/var/www/html/wp-settings.php, where `php` was mistakenly spelt as `phpp`.

The error was traced and corrected using `strace` and the process was automated with Puppet.
