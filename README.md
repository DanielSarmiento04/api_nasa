## Infrastructure Integration


## Resume

The aims of this repository is used the stack with python (FastApi) , PostgresSql and nginx as load balancer and server reverse proxy.

## Concept API

The API have the capability to manage the Hero, an Hero has the follow parameters

- id
- name
- secret_name
- age

> The Api has 3 endpoints

1. `/`  => health check
2. POST `/heroes/` => create a new hero
3. GET `/heroes/` => get the heroes


## Concept Infrastructure

The project has an integration with docker compose, see more in the docker-compose.yml file.

1. Postgres SQL, image.
2. ms_hero_1, api image.
3. ms_hero_2, api image.
4. server_reverse_proxys, nginx image, the nginx conf file is at the follow path `reverse_proxy/nginx.conf`.

The load balancer is configured to send a request to each ms_hero follow least connection.

## Start up

This repository used docker as container manager

```
    docker-compose build
```

```
    docker-compose up -d
```


or if you want to use a simplified command line 

```
    docker-compose up -d --build
```



## Reference 

[1] Simic, S. (2023) How to install Docker on ubuntu 20.04 and 22.04, phoenixNAP. Available at: https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04 (Accessed: 21 September 2023). 


[2] Maintainers, D. (2023) Install the compose plugin, Docker Documentation. Available at: https://docs.docker.com/compose/install/linux/ (Accessed: 21 September 2023). 

[3] taoyuan. (n.d.). Generation of a self signed certificate. Gist. https://gist.github.com/taoyuan/39d9bc24bafc8cc45663683eae36eb1a 

[4] Ramírez, S. FastAPI [Computer software]. https://github.com/tiangolo/fastapi
