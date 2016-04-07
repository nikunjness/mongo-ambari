from resource_management import *

config = Script.get_config()

db_path = default('configurations/mongodb/db_path', '/var/lib/mongo')
bind_ip = default('configurations/mongodb/bind_ip', '0.0.0.0')
# The web status page is always accessible at a port number that is 1000 greater than the port determined by tcp_port.
tcp_port = default('configurations/mongodb/tcp_port', '27017')
mongo_host = default('/clusterHostInfo/mongodb_master_hosts', ['unknown'])[0]
