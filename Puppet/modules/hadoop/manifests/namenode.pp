class hadoop::namenode {
    # Require the params from params.pp
    require hadoop::params

    # Require the basepackages from basepackages.pp
    require hadoop::basepackages

    # Install required RPM packages
    $package_list = [ 
                    "hadoop-0.20-namenode",
                    ]
    package { $package_list: ensure => "installed" }

    # Copy the hadoop_namenode_initialization_steps.txt
    file { "hadoop_namenode_initialization_steps.txt":
        path   => "${hadoop::params::moduledir}/hadoop_namenode_initialization_steps.txt",
        mode   => "0644", owner => "root", group => "root",
        source => "puppet:///modules/hadoop/hadoop_namenode_initialization_steps.txt",
    }
}
