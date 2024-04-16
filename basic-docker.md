# Docker Commands

## Running a Docker Container
To run a public repository, use the following command:
```bash
docker run centos
```
Centos is an official repository.

## Keeping a Docker Container Alive
If you want to keep your Docker container running, use the following command:
```bash
docker run -it centos bash
```
You will see the command change from `root@docker:/root` to `[root@e0a1d]`.

## Checking Details
To see other details or parts of the things, use the following command:
```bash
cat /etc/*release*
```

## Listing Running Containers
To list all running containers, use the following command:
```bash
docker ps
```
This shows all running containers with their container ID, image, command, creation time, status, and ports.

## Running a Docker Container in the Background
To run a Docker container in the background, use the following command:
```bash
docker run -d centos sleep 20
```
The `-d` flag is for background running. After running this command, you can see the Docker ID. The `sleep 20` command means that if we do not do anything else, it goes to sleep after 20 seconds.

## Listing All Containers
To see all commands that have exited, use the following command:
```bash
docker ps -a
```
This shows all containers, including those that have exited.

## Stopping a Docker Container
To stop a Docker container, use the following command:
```bash
docker stop <container_id_or_name>
```

## Removing a Docker Container
To remove a Docker container, use the following command:
```bash
docker rm <container_id_or_name>
```

## Listing Docker Images
To list all Docker images, use the following command:
```bash
docker images
```

## Removing a Docker Image
To remove a Docker image, use the following command:
```bash
docker rmi <image_name>
```
Here, `i` stands for images.

## Executing a Command in a Docker Container
To execute a command in a Docker container, use the following command:
```bash
docker exec <container_id> cat /etc/*release*
```
Here, `exec` stands for execute.
```
 😊
