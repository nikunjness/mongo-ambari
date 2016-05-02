from resource_management import *
from mongo_base import MongoBase


class MongoClient(MongoBase):
    client_config_path = '/etc/mongoclient.conf'
    mongo_packages = ['mongodb-org-shell', 'mongodb-org-tools']


    def install(self, env):
        import params

        env.set_params(params)
        self.install_mongo(env)
        self.configure(env)


    def configure(self, env):
        import params

        env.set_params(params)

        File(self.client_config_path,
             content=Template('mongoclient.conf.j2'),
             mode=0644
            )

        File('/usr/local/bin/mongok',
             content=StaticFile('mongok'),
             mode=0755
            )


if __name__ == "__main__":
    MongoClient().execute()
