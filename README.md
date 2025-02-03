# named

## Variables
| Name | Description | Type | Default |
|---|---|---|---|
| named_service | Name of systemd unit | | |
| named_pri_domain_name | The name of the domain being served. | string | example.com |
| named_self_log | Enable logging in a separate file. | bool | true |
| named_log_level | The logging level. | string | info |
| named_package | Bind's package name that will be installed | string | bind9 |
| named_forwarders | Addresses of request forwarding hosts. | list | 8.8.8.8, 8.8.4.4 |
| named_conf_dir | Configuration Directory. | string | /etc/bind |
| named_work_dir | Working directory. | string | /var/lib/bind |
| named_cache_dir | Directory for storing the zone cache. | string | /var/cache/bind |
| named_zones_dir | Directory with zone files. | string | /var/lib/bind |
| named_log_dir | The directory with the log files. | string | {{ named_work_dir }}/log |
| named_conf | The configuration file. | string | {{ named_conf_dir }}/named.conf |
| named_log | Log file. | string | {{ named_log_dir }}/named.log |
| named_all_zone_hostmaster | Responsible for the zone. | string | hostmaster.{{ named_pri_domain_name }} |
| named_all_zone_ttl | Cache storage time in seconds. | string | 3600 |
| named_all_zone_refresh | Data update interval between servers. | string | 3600 |
| named_all_zone_retry | The interval between attempts to update the data. | string | 600 |
| named_all_zone_expire | The lifetime of the zone. | string | 1209600 |
| named_all_zone_neg_ttl | Minimum cache storage time in seconds. | string | 600 |
| named_forward_zones | The zone that will be created, as well as its records. | list | - |

## The installation of only the master
```
[bind_masters]
192.168.10.10
```
## Installation of the master and replica
```
[bind_masters]
192.168.10.10

[bind_slaves]
192.168.10.11
192.168.10.12
```

## The "Forward zone" section - defaults/main/forward_zone.yml
The reverse zone will be created automatically.
```
named_forward_zones:
  - zone: "example.com"
    records:
      - { name: "ns1", address: "192.168.10.11", type: "A" }
      - { name: "ns2", address: "192.168.10.12", type: "A" }
      - { name: "master", address: "ns1.example.com.", type: "CNAME" }
      - { name: "slave", address: "ns2.example.com.", type: "CNAME" }
```
