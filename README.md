#### An Ambari Stack for MongoDB
Ambari stack for easily installing and managing Mongo DB on HDP cluster


###Assumptions

- Ambari is installed and running. If not, you can use sandbox VM Image provided by [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- No previous installations of Mongo DB exist. If there any, you can either remove it or rename it.

Follow given step to install and manage Mongo DB using Ambari.

####Connect to the VM via SSH (password hadoop for sandbox image) and start Ambari server
```
ssh root@ambari.machine
```

####To deploy the Mongo DB, run below
```
on HDP 2.2
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
on HDP 2.3
cd /var/lib/ambari-server/resources/stacks/HDP/2.3/services
git clone https://github.com/nikunjness/mongo-ambari.git
```

####Restart Ambari
#####on sandbox
```sudo service ambari restart```

#####on non-sandbox
```sudo service ambari-server restart```


####Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:

On bottom left -> Actions -> Add service -> check MongoDB -> Next -> Next -> Next -> Deploy

![Image](../master/screenshots/addservice.png?raw=true)
![Image](../master/screenshots/assignmaster.png?raw=true)
![Image](../master/screenshots/assingnslave.png?raw=true)
![Image](../master/screenshots/customize.png?raw=true)
![Image](../master/screenshots/review.png?raw=true)
![Image](../master/screenshots/installed.png?raw=true)


####On successful deployment you will see the MongoDB as part of Ambari stack and will be able to start/stop the service from here:

![Image](../master/screenshots/mongosummary.png?raw=true)
 
####You can see the parameters you configured under 'Configs' tab 
![Image](../master/screenshots/mongoconfig.png?raw=true)

 
- One benefit to wrapping the component in Ambari service is that you can now monitor/manage this service remotely via REST API

```
export SERVICE=MONGODB
export PASSWORD=admin
export AMBARI_HOST="your_ambari_hostname"
export CLUSTER="your_ambari_cluster_name"

#get service status
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X GET http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#start service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Start $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "STARTED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE

#stop service
curl -u admin:$PASSWORD -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop $SERVICE via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://$AMBARI_HOST:8080/api/v1/clusters/$CLUSTER/services/$SERVICE
```

#### Remove Mongo service

- To remove the MongoDB: 
  - Stop the service via Ambari
  - Delete the service
  
    ```
    curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://replace_with_your_ambari_hostname.com:8080/api/v1/clusters/ambari_cluster_name/services/MONGODB
    ```
  - Remove artifacts 
  
    ```
    rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.2/services/mongo-ambari
    ```
  - Restart Ambari
    ```
    service ambari restart
    ```
    
###References:
https://github.com/abajwa-hw/ntpd-stack


    
