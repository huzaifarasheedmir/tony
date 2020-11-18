# Tony 
### The AI Based product recommender

### Steps to run the app
**The app is fully containerized so you need to have docker and docker-compose installed**

- **Install dokcer and docker-compose**
- Clone the repo
- Inside the main dir of repo run

```angular2
docker-compose up -d --build --f
```
- Wait for above command to build and spin up the containers
- That's it the app is up and running
- You can access the apis on server
```angular2
http://your-host:8081
```

### Custom configs
The app has two main services 
**etl** and **web**

- For changing the config or Web service you can change ```web/config.py```
- For changing the config or ETL service you can change ```etl/config.py```


Enjoy!