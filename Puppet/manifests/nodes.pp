# The Role(s)/Collection(s) made by some specific Cookbooks
class role_namenode {
    include hadoop::namenode
    include hadoop::hbasemaster
    include hadoop::hueserver
}

class role_secondarynamenode {
    include hadoop::secondarynamenode
    include hadoop::jobtracker
    include hadoop::hiveserver
    include hadoop::gangliaserver
    include graphite::server
}

class role_datanode {
    include hadoop::datanode
    include hadoop::tasktracker
    include hadoop::zookeeper
    include hadoop::hbaseregionserver
    include hadoop::hive
    include hadoop::ganglia 
    include hadoop::hue
}

class role_zookeeperserver {
    include hadoop::zookeeperserver
}

# Default Node, has Nothing need to do
node default {
}

# The Node(s) defined by FQDN, include(s) the Role(s)
node 'ip-10-197-29-251.us-west-1.compute.internal' {
    $zookeeper_myid = '1'
    include role_namenode
    include role_datanode
    include role_zookeeperserver
}

node 'ip-10-196-9-188.us-west-1.compute.internal' {
    $zookeeper_myid = '2'
    include role_secondarynamenode
    include role_datanode
    include role_zookeeperserver
}

node 'ip-10-197-62-239.us-west-1.compute.internal' {
    $zookeeper_myid = '3'
    include role_datanode
    include role_zookeeperserver
}
