import os
from time import sleep

import ambari_simplejson as json # simplejson is much faster comparing to Python 2.6 json module and has the same functions set.
from resource_management import *


class MongoBase(Script):
    repos_file_path = '/etc/yum.repos.d/mongodb-org.repo'
    config_file_path = '/etc/mongod.conf'
    mongo_packages = []


    def install_mongo(self, env):
        import params

        env.set_params(params)

        self.install_packages(env)

        File(self.repos_file_path,
             content=StaticFile('mongodb-org.repo'),
             mode=0644
            )

        print "Installing mongodb..."
        for pack in self.mongo_packages:
            Package(pack)


    def configure_mongod(self, env):
        import params

        env.set_params(params)

        File(self.config_file_path,
             content=Template("mongod.conf.j2"),
             mode=0644
            )


    def create_admin_user(self, env):
        import params
        env.set_params(params)

        db_name = 'admin'

        if params.auth == 'enabled':
            mongod_start_cmd = format(
                'mongod --fork --syslog --noauth --bind_ip 127.0.0.1'
                ' --port {params.tcp_port} --dbpath {params.db_path}'
                )

            create_admin_json = json.dumps(
                {
                    'user': params.admin_user,
                    'pwd': params.admin_pass,
                    'roles': [{'role': 'userAdminAnyDatabase', 'db': db_name}]
                }
            )

            create_admin_cmd = format("mongo {db_name} --eval 'db.createUser({create_admin_json})'")

            Execute(
                as_user(mongod_start_cmd, 'mongod')
                )

            sleep(1)
            Execute(create_admin_cmd)

            Execute(
                format('mongod --shutdown --dbpath {params.db_path}')
                )
