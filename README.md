# spatialdata-mcmicro

Build docker image:
```
docker build --tag spatialdata - < Dockerfile
```

(Optional) tag image with username account
```
docker tag spatialdata <user-name>/spatialdata
docker image rm spatialdata
```

Create and run a container from an image 
```
docker run -it <user-name>/spatialdata
```

To list images or containers use
```
docker image ls
docker container ls -a  # -a lists also stopped containers
```

To start/stop a container
```
docker container start <contaier_hash>
docker container stop <contaier_hash>
```

Enter a running container
```
docker exec -it <container_hash> bash
```

Copy file from host to running container
```
docker cp <path_in_host> <container_hash>:/home/<path_in_container>

Commit the changes to a new image
```
docker commit <container_hash> <user-name>/spatialdata:<new_tag> 
```

Push image
```
docker push <user-name>/spatialdata
```

Pull Image
```
docker pull <user-name>/spatialdata_mcmicro:latest

# valid images:
docker pull niksto/spatialdata_mcmicro:latest
docker pull lucamarconato/spatialdata_mcmicro:latest
```
