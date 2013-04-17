class hadoop::hiveserver {
    # Require the params from params.pp
    require hadoop::params

    # Require the hive from hive.pp
    require hadoop::hive

    # Install required RPM packages
    $package_list = [ 
                    "hadoop-hive-metastore",
                    "hadoop-hive-server",
                    "mysql-server",
                    ]
    package { $package_list: ensure => "installed" }

    # Create required directories
    $directory_list = [
                      "/var/lib/hive",
                      "/var/lib/hive/metastore",
                      ]

    file { $directory_list:
        mode   => "0755", owner  => "hive", group  => "hive",
        ensure => directory,
        require => Package["hadoop-hive"], # Require Package
    }
    
    # Copy the hive_initialization_steps.txt
    file { "hive_initialization_steps.txt":
        path   => "${hadoop::params::moduledir}/hive_initialization_steps.txt",
        mode   => "0644", owner => "root", group => "root",
        source => "puppet:///modules/hadoop/hive_initialization_steps.txt",
    }

    # Copy the hive_mysqlserver_initialization.sql
    file { "hive_mysqlserver_initialization.sql":
        path   => "${hadoop::params::moduledir}/hive_mysqlserver_initialization.sql",
        mode   => "0644", owner => "root", group => "root",
        source => "puppet:///modules/hadoop/hive_mysqlserver_initialization.sql",
    }

    # Ensure services start on boot and running
    service { "hadoop-hive-metastore":
        enable => "true",
        ensure => "running",
        require => Package["hadoop-hive-metastore"], # Require Package
    }

    service { "hadoop-hive-server":
        enable => "true",
        ensure => "running",
        require => Package["hadoop-hive-server"], # Require Package
    }
}
