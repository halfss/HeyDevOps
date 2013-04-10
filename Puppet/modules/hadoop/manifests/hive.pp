class hadoop::hive {
    # Require the params from params.pp
    require hadoop::params

    # Require the basepackages from basepackages.pp
    require hadoop::basepackages

    # Require the zookeeper from zookeeper.pp
    require hadoop::zookeeper

    # Install required RPM packages
    $package_list = [ 
                    "hadoop-hive",
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
    
    # Copy mysql-connector-java-5.1.24-bin.jar  
    file { "mysql-connector-java-5.1.24-bin.jar":
        path   => "/usr/lib/hive/lib/mysql-connector-java-5.1.24-bin.jar",
        mode   => "0644", owner => "hive", group => "hive",
        source => "puppet:///modules/hadoop/mysql-connector-java-5.1.24-bin.jar",
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
    
    # Update /etc/hive/conf/hive-site.xml
    file { "hive-site.xml":
        path    => "/etc/hive/conf/hive-site.xml",
        mode    => "0644", owner => "hive", group => "hive",
        ensure  => present,
        content => template("hadoop/hive-site.xml.erb"),
        require => Package["hadoop-hive"], # Require Package
    }
}
