## Infrastructure Integration


## Resume

The aims of this repository is used the stack with python (FastApi) , PostgresSql and nginx as load balancer and server reverse proxy. Finally the project used apache camel to use server discovery 


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
