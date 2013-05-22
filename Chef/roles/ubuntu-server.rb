name "ubuntu_server"
description "The base role for all Ubuntu Linux server nodes."
run_list(
  "adsstorm::role_ubuntu-server"
)
override_attributes(
    "authorization" => {
      "sudo" => {
        "groups" => ["admin"],
        "passwordless" => true,
        "users" => ["zabbix"]
      }
    },

    "users" => [ "baina","kunli","dongguo","qchen","wywu","qpwang"],
    "openssh" => {
        "PasswordAuthentication" => "no"
    },
    :zabbix => {
        :server_addr => "10.1.4.56"
    },
    "chef_client" =>{
      "server_url"  =>  "10.1.4.55"
    }
)
