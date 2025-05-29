# pytorch_workshop
This repository is for new AI-Lab members who have never used PyTorch and want to get hands-on experience quickly.

## 1 Clone the repository
```
git clone -b feature/first_base https://github.com/kawako1103/pytorch_workshop.git
cd pytorch_workshop
```

## 2 Build & run the Docker image
## You have two options. For the workshop we will use 2-a (docker-compose). If you prefer the classic workflow, see 2-b. 
## 2-a docker-compose
### Builds the image and starts the container with one command.	Recommended for anyone who finds docker build … / docker run … cumbersome.
## 2-b docker build + docker run
### Manual workflow, more explicit.Recommended for anyone who wants to practice raw Docker commands.

## 2-a With docker-compose
pytws = PyTorch WorkShop.
${USER} automatically inserts your account name, so every participant gets a unique tag.
First build takes 8~9 min.

```
# Build image & start container (background)
docker compose up -d

# Attach to the running container
docker compose exec workshop bash
```

(Skip step 3 if you used docker-compose; the container is already running.)

## 2-b Manual build & run
```
# 1) Build
docker build -t pytws_$(whoami):v1 .

# 2) Run (change 6006 if needed)
docker run --gpus all -it --rm \
  -v $(pwd):/workspace \
  -p 6006:6006 \
  --name pytws_$(whoami) \
  pytws_$(whoami):v1
```

Expected prompt:
```
root@<container_id>:/workspace#
```

Check GPU (optional):
```
nvidia-smi
```

## 3 Run the tutorial script
```
python src/train_mnist.py
```

Expected output:

```
device = cuda:0
Epoch 0 | loss 0.415 | train_acc 89.3% | val_acc 93.7%
Epoch 1 | loss 0.188 | train_acc 94.6% | val_acc 95.5%
Epoch 2 | loss 0.136 | train_acc 96.1% | val_acc 96.4%
```

## 4 Visualize with TensorBoard
```
tensorboard --logdir runs --host 0.0.0.0 --port 6006
Open http://localhost:6006 in your browser
(or whatever port you mapped).
```

## 5 Clean-up
```
# Stop & remove container (if not auto-removed)
docker stop pytws_$(whoami)
docker rm   pytws_$(whoami)

# Delete image
docker rmi pytws_$(whoami):v1
```

With docker-compose:
```
docker compose down --volumes --rmi all --remove-orphans
```

## Further reading
### PyTorch
[Beginner-friendly introductions (neural-net basics, MNIST tutorial, etc.)](https://yutaroogawa.github.io/pytorch_tutorials_jp/)

[MNIST with PyTorch](https://qiita.com/TaigaMasuda/items/24d85860ffcd724de9eb)

### Docker (aiLab internal)
[Remote Machine Learning with Docker](https://sites.google.com/g.ecc.u-tokyo.ac.jp/ailab-rcast-2020/%E7%A0%94%E7%A9%B6%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E5%8F%82%E8%80%83%E8%B3%87%E6%96%99/%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%A7%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92)

[Deep-Learning on Workstations with VS Code](https://drive.google.com/file/d/1bvb4YwqCEgtwOJi16R4lK2WclpONc0Hy/view)

[Docker Study Group slides (2022)](https://drive.google.com/drive/folders/1QVuU-Uia99oWRj9cETDFMlXFSykeNoZk)
