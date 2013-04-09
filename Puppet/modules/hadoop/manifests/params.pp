class hadoop::params {
    # The Puppet workdir
    $workdir = "/opt/puppet-workdir"

    # The module workdir
    $moduledir = "$workdir/hadoop"
    file { [ "$workdir", "$moduledir" ]:
        ensure => "directory",
    }
}
