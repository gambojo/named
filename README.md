# named

## Пример заполнения плейбука для запуска роли
```
---
- name: Install NameD Cluster
  hosts:
    - bind_masters
    - bind_slaves
  become: true
  roles:
    - role: named
```

## Пример заполнения inventory
### Инсталляция только мастера
```
[bind_masters]
192.168.20.31
```
### Инсталляция мастера и реплик
```
[bind_masters]
192.168.20.31

[bind_slaves]
192.168.20.32
192.168.20.33
```

## Пример заполнения переменных
### Секция "Main" - defaults/main/main.yml
```
bind_pri_domain_name: "example.com"
bind_self_log: true
```

### Секция "Forward zone" - defaults/main/forward_zone.yml
```
bind_forward_zones:
  - zone: "example.com"
    records:
      - { name: "@", address: "192.168.20.20", type: "A" }
      - { name: "ns1", address: "192.168.20.21", type: "A" }
      - { name: "ns2", address: "192.168.20.32", type: "A" }
      - { name: "master", address: "ns1.example.com.", type: "CNAME" }
      - { name: "slave", address: "ns2.example.com.", type: "CNAME" }
```

### Секция "Reverse zone" - defaults/main/reverse_zone.yml
```
bind_reverse_zones:
  - zone: "192.168.20"
    records:
      - { address: "30", name: "ns1.example.com" }
      - { address: "31", name: "ns2.example.com" }
```

## Описание переменных

| Имя | Описание | Тип |
|---|---|---|
| # [ Main ] |  |  |
| bind_conf_dir | Конфигурационная директория. По умолчанию - `"/etc/bind"`. | string |
| bind_work_dir | Рабочая директория. По умолчанию - `"/var/lib/bind"`. | string |
| bind_cache_dir | Директория для хранения кеша зон. По умолчанию - `"/var/cache/bind"`. | string |
| bind_zones_dir | Директория с файлами зон. По умолчанию - `"/var/lib/bind"`. | string |
| bind_log_dir | Директория с файлами логов. По умолчанию - `"{{ bind_work_dir }}/log"`. | string |
| bind_conf | Конфигурационный файл. По умолчанию - `"{{ bind_dir }}/named.conf"`. | string |
| bind_log | Файл логов. По умолчанию - `"{{ bind_log_dir }}/named.log"`. | string |
| bind_self_log | Включить логирование в отдельный файл. По умолчанию - `true`. | bool |
| bind_log_level | Уровень логирования. Возможны варианты - critical, error, warning, notice, info, debug, dynamic. По умолчанию - `"info"`. | string |
| bind_pri_domain_name | Имя обслуживаемого домена. По умолчанию - `"example.com"`. | string |
| bind_all_soa_pri | Основной сервер. По умолчанию - `"{{ hostvars[groups.bind_masters]['ansible_hostname'] }}.{{ bind_pri_domain_name }}"`. | string |
| bind_forwarders | Адреса хостов перессылки запросов. По умолчанию - `["8.8.8.8", "8.8.4.4"]`. | list |
| bind_nameservers_list | TRUE, если количество мастеров больше одного. По умолчанию - `-`. | list |
| bind_all_zone_hostmaster | Ответственный за зону. По умолчанию - `"hostmaster.{{ bind_pri_domain_name }}"`. | string |
| bind_all_zone_ttl | Время хранения кэша в секундах. По умолчанию - `"3600"`. | string |
| bind_all_zone_refresh | Интервал обновления данных между серверами. По умолчанию - `"3600"`. | string |
| bind_all_zone_retry | Интервал между попытками обновления данных. По умолчанию - `"600"`. | string |
| bind_all_zone_expire | Срок жизни зоны. По умолчанию - `"1209600"`. | string |
| bind_all_zone_neg_ttl | Минимальное время хранения кеша в секундах. По умолчанию - `"600"`. | string |
| bind_all_zone_serial | Серийный номер зоны. По умолчанию - `"{{ ansible_timestamp }}"`. | string |
|  |  |  |
| # [ Forward zone ] |  |  |
| bind_forward_zones | Переменная хранящая в себе список вложенных словарей конфигурации (zone, records(name, address, type)) для зоны прямого просмотра. По умолчанию - `[]`. | list |
| zone | Зона прямого просмотра. По умолчанию - `"example.com"`. | string |
| records.name | Имя dns-записи. По умолчанию - `"ns1"`. | string |
| records.address | Адрес хоста для записи. По умолчанию - `"192.168.20.30"`. | string |
| records.type | Тип dns-записи. По умолчанию - `"A"`. | string |
|  |  |  |
| # [ Reverse zones ] |  |  |
| bind_reverse_zones | Переменная хранящая в себе список вложенных словарей конфигурации (zone, records(address, name)) для зоны обратного просмотра. По умолчанию - `[]`. | list |
| zone | Зона обратного просмотра. По умолчанию - `"192.168.20"`. | string |
| records.address | Адрес хоста для записи. По умолчанию - `"30"`. | string |
| records.name | Имя хоста. По умолчанию - `"ns1.example.com"`. | string |
|  |  |  |
| # [ Special ] |  |  |
| bind_master_group | Служебная переменная для определения имени мастер-группы. По умолчанию - `"{{ groups.bind_masters \| default('') }}"`. | string |
| bind_slave_group | Служебная переменная для определения имени слейв-группы. По умолчанию - `"{{ groups.bind_slaves \| default('') }}"`. | string |
