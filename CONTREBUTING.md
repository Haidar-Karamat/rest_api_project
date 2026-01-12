# CONTRIBUTING
## HOW TO RUN DOCKERFILE LOCALLY

```
docker run -dp 5000:5000 -w/app "$(pwd):/app" hadi_restapi_python sh -c
"flask run"
```

```
"Gerenal from" - docker run -dp <host_port>:<container_port> -w /app -v "$(pwd):/app" <image_name> sh -c "<command>"
``