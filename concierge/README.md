# concierge
AI Concierge


## Getting Started

### Prerequisites
#### Anaconda
1. Download
```
https://www.anaconda.com/download
```

### Running with Ubuntu
1. Install Ubuntu via Windows WSL2
2. Install Anaconda via https://repo.continuum.io/archive/
   1. $ wget https://repo.continuum.io/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
   2. $ bash Anaconda3-2024.02-1-Linux-x86_64.sh
3. You can access Windows files via the mount drive when you are in a Ubuntu prompt. I.e.
   1. ls -l /mnt/c/Users/tonyl/Code/
4. You can access the Ubuntu files via wsl protocol
   1. ls -l \\wsl.localhost\Ubuntu
5. To test that it worked, run `$ which python`. It should print a path that has anaconda in it. If it doesn't add this line to the end of ~/.bashrc
   1. `export PATH=/home/tmai/anaconda3/bin:$PATH
6. Made a symlink between `C:/Users/tonyl/Code/waai/JupyterNotebooks to Ubuntu's notebook: In the WSL terminal:
    ```cd ~
    ln -s /mnt/c/Users/tonyl/Code/waai/JupyterNotebooks/ notebooks
    ```
7. Test Jupyter `$ jupyter notebook --no-browser`
8. Add an alias in .bash_aliases: `alias jup='cd /home/tmai/notebooks && jupyter notebook --no-browser`. From now on, just type `jup` to launch

### Installing

## To build Docker image
```
docker build . -f concierge/Dockerfile -t concierge
```

## Running
```
```docker run -p 127.0.0.1:50051:50051/tcp concierge
```

## Creating proxy
```
docker network create microservices
```

And
```
docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name concierge concierge
```

## MyPy
In most cases, missing type hints in third-party packages is not something we want to be bothered with so we can silence these messages:
```
 mypy --ignore-missing-imports .
```
