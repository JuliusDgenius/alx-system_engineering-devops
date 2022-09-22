# kill process killmenow

exec {
  command => 'pkill killmenow',
  provider => 'shell',
}
