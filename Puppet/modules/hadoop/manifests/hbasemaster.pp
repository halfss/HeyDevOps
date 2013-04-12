class hadoop::hbasemaster {
    # Require the params from params.pp
    require hadoop::params

    # Require the hbasecommon from hbasecommon.pp
    require hadoop::hbasecommon

    # Install required RPM packages
    $package_list = [ 
                    "hadoop-hbase-master",
                    "hadoop-hbase-thrift",
                    ]
    package { $package_list: ensure => "installed" }
    
    # Copy the hbasemaster_initialization_steps.txt
    file { "hbasemaster_initialization_steps.txt":
        path   => "${hadoop::params::moduledir}/hbasemaster_initialization_steps.txt",
        mode   => "0644", owner => "root", group => "root",
        source => "puppet:///modules/hadoop/hbasemaster_initialization_steps.txt",
    }

    # Ensure services start on boot and running
    service { "hadoop-hbase-master":
        enable => "true",
        ensure => "running",
        require => Package["hadoop-hbase-master"], # Require Package
    }

    service { "hadoop-hbase-thrift":
        enable => "true",
        ensure => "running",
        require => Package["hadoop-hbase-thrift"], # Require Package
    }
}
