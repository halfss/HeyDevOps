class hadoop::ganglia {
    # Require the params from params.pp
    require hadoop::params

    # Require the basepackages from basepackages.pp
    require hadoop::basepackages

    # Install required RPM packages
    $package_list = [ 
                    "ganglia",
                    "ganglia-gmond",
                    ]
    package { $package_list: ensure => "installed" }

    # Update /etc/ganglia/gmond.conf
    file { "gmond.conf":
        path    => "/etc/ganglia/gmond.conf",
        mode    => "0644", owner => "ganglia", group => "ganglia",
        ensure  => present,
        content => template("hadoop/gmond.conf.erb"),
        require => Package["ganglia-gmond"], # Require Package
        notify  => Service["gmond"], # Notify the service to restart when changes
    }

    # Ensure service starts on boot and running
    service { "gmond":
        enable => "true",
        ensure => "running",
        require => Package["ganglia-gmond"], # Require Package
    }
}
