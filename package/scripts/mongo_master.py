from resource_management import *
from mongo_base import MongoBase


class MongoServer(MongoBase):
    mongo_packages = ['mongodb-org']


    def install(self, env):
        import params

        env.set_params(params)

        self.install_mongo(env)
        self.create_admin_user(env)
        self.configure_mongod(env)


    def configure(self, env):
        import params

        env.set_params(params)

        self.configure_mongod(env)


    def start(self, env):
        print "start mongodb"
        self.configure(env)
        Execute('service mongod start')


    def stop(self, env):
        print "stop mongodb"
        Execute('service mongod stop')


    def restart(self, env):
        print "restart mongodb"
        self.configure(env)
        Execute('service mongod restart')


    def status(self, env):
        print "checking status..."
        Execute('service mongod status')


if __name__ == "__main__":
    MongoServer().execute()
