# install flask from pip3
exec { 'install_flask':
  command => 'pip3 install Flask==2.1',
  path    => ['/usr/bin'],
  unless  => 'pip3 show Flask',
}
