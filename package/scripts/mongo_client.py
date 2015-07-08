import os

from resource_management import *
from mongo_base import MongoBase

class MongoClient(MongoBase):
    client_config_path="/etc/mongoclient.conf"
    mongo_packages=['mongodb-org-shell', 'mongodb-org-tools']

    def install(self, env):
        import params
        env.set_params(params)
        self.installMongo(env)
        self.configure(env)
        File('/usr/local/bin/mongok',
             content=Template("mongok"),
             mode=0755
             )

    def configure(self,env):
        import params
        env.set_params(params)
        self.configureMongo(env)
        File(self.client_config_path,
             content=Template("mongoclient.conf.j2"),
             mode=0644
             )


if __name__ == "__main__":
    MongoClient().execute()
