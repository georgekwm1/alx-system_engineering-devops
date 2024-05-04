#Create a custom HTTP header response with Puppet

class nginx_custom_header {
    $hostname = $facts['hostname']

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
if (\$::nginx::params::realip_remote_addr) {
    set_real_ip_from \$::nginx::params::realip_remote_addr;
}

# Custom header
add_header X-Served-By \"$hostname\";
",
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure => running,
        enable => true,
    }
}

# Apply the class
include nginx_custom_header

