class hadoop::datanode {
    # Require the params from params.pp
    require hadoop::params

    # Require the basepackages from basepackages.pp
    require hadoop::basepackages

    # Install required RPM packages
    $package_list = [ 
                    "hadoop-0.20-datanode",
                    ]
    package { $package_list: ensure => "installed" }
}
