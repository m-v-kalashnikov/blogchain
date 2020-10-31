Cleaning of docker

```shell script
docker system prune
docker rmi $(docker images -f "dangling=true" -q)
docker rmi $(docker images -a -q)
docker rm $(docker ps --filter=status=exited --filter=status=created -q)
```

```shell script
docker run --rm -it -v {PATH_TO_PROJECT}/frontend/:/usr/src/frontend node:15.0.1-alpine /bin/sh
```

Change permissions

```shell script
sudo chown -R $USER:$USER .
```

Making script executable

```shell script
sudo chmod +x backend/scripts/start.sh
```

Removing of docker-compose session

```shell script
docker-compose down -v --remove-orphans
```

Start of docker-compose session (first run will take a time)

```shell script
docker-compose up --build
```

Entering to backend console

```shell script
docker exec -it backend /bin/sh
```

Entering to frontend console

```shell script
docker exec -it frontend /bin/sh
```
