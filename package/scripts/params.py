from resource_management import *


config = Script.get_config()

# config['configurations']['zoomdata-env']['content']
bind_ip = config['configurations']['mongod-conf']['bind_ip']
db_path = config['configurations']['mongod-conf']['db_path']
tcp_port = config['configurations']['mongod-conf']['tcp_port']

admin_user = default('configurations/mongodb-admin/admin_user', '')
admin_pass = default('configurations/mongodb-admin/admin_pass', '')

if admin_user and admin_pass:
    auth = 'enabled'
else:
    auth = 'disabled'

mongo_host = default('/clusterHostInfo/mongodb_server_hosts', ['unknown'])[0]
