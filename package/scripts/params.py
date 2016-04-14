from resource_management import *

bind_ip = default('configurations/mongodb/bind_ip', '0.0.0.0')
tcp_port = default('configurations/mongodb/tcp_port', '27017')
db_path = default('configurations/mongodb/db_path', '/var/lib/mongo')
db_name = default('configurations/mongodb/db_name', '')
db_user = default('configurations/mongodb/db_user', 'anadmin')
db_pass = default('configurations/mongodb/db_pass', '')
mongo_host = default('/clusterHostInfo/mongodb_master_hosts', ['unknown'])[0]
