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

## Apis

### Api Docs and Screenshots
Open [Swagger](https://editor.swagger.io/) and paste the content of [ProductsAPIs](https://github.com/huzaifarasheedmir/tony/blob/master/web/products/api.yml) file to see the API docs.

**Below are the screenshots of working APIs tested on Postman**
- Get categories API
![image](https://user-images.githubusercontent.com/12775679/99587670-36f58900-2a0b-11eb-80be-a551b934b294.png)


- Product Search API
![image](https://user-images.githubusercontent.com/12775679/99587511-031a6380-2a0b-11eb-98b8-47b79cf10c63.png)

- Product Recommendation response
![image](https://user-images.githubusercontent.com/12775679/99587760-60161980-2a0b-11eb-8885-6bd823ebf11c.png)


Enjoy!