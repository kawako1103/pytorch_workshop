# pytorch_workshop
This is the repository for new members of ai-lab who have never used Pytorch and want to use it for the first time.

## 1. リポジトリ取得
```
git clone https://github.com/kawako1103/pytorch_workshop.git
cd pytorch_workshop
```

## 2. Docker イメージを “自分の名前タグ” でビルド(pytwsはpytorch workshopの短縮形のつもり。whoamiはユーザによって自動的に変わるので特に変更せずともわかりやすい。8~9分ほどかかるかと。。)
```
docker build -t pytws_$(whoami):v1 .
```

## ※build後にimagesが作成される(例えば:ユーザ名:rkawaguchiの場合以下のように名前が付く)
```
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker images
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
pytws_rkawaguchi                   v1        36097820484b   51 seconds ago   6.14GB
```


## 3. コンテナ起動（作業ディレクトリをマウント）(--gpus allをつけると gpuが使える/ --rmをつけるとdocker stopをした時に自動的にコンテナが削除される/-v　リポジトリを/workspaceにマウント)
```
docker run --gpus all -it --rm -v $(pwd):/workspace \
-p 6006:6006 --name pytws_$(whoami) pytws_$(whoami):v1
```

### #以下のような感じになるかと。
```
#root@41038ac225ec:/workspace# 
```

### ※コンテナ起動後にユーザ名が付されたコンテナが確認できる(例えば:ユーザ名:rkawaguchiなら↓)
```
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                         NAMES
41038ac225ec   pytws_rkawaguchi:v2           "/bin/bash"              4 seconds ago   Up 4 seconds   0.0.0.0:6006->6006/tcp, [::]:6006->6006/tcp   pytws_rkawaguchi
```

### ※gpuが利用できるか確認する(nvidia-smiで下のように何か出てくればOK)
```
root@22ed2f8a6c05:/workspace# nvidia-smi
Tue May 27 14:52:51 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.05              Driver Version: 560.35.05      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A6000               Off |   00000000:AF:00.0 Off |                  Off |
| 30%   33C    P8             17W /  300W |     233MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
+-----------------------------------------------------------------------------------------+
```

## 4. 教材を実行
```
root@41038ac225ec:/workspace# python src/train_mnist.py 
python src/train_mnist.py
```

### #期待される出力
```
device = cuda:0
Epoch 0 | loss 0.415 | train_acc 89.3% | val_acc 93.7%
Epoch 1 | loss 0.188 | train_acc 94.6% | val_acc 95.5%
Epoch 2 | loss 0.136 | train_acc 96.1% | val_acc 96.4%
```

## 5. tensorboardで可視化 #ポート経由でブラウザで閲覧(SSH接続でWSを扱っている前提)

```
root@41038ac225ec:/workspace# tensorboard --logdir runs --host 0.0.0.0 --port 6006
```

### #期待される出力(urlをクリックすると飛んでみれる。。はず。。)
```
TensorFlow installation not found - running with reduced feature set.

NOTE: Using experimental fast data loading logic. To disable, pass
    "--load_fast=false" and report issues on GitHub. More details:
    https://github.com/tensorflow/tensorboard/issues/4784

TensorBoard 2.19.0 at http://0.0.0.0:6006/ (Press CTRL+C to quit)
```

## 6. 終了時にコンテナ・docker imageを削除
```
# 動作中のコンテナ一覧を確認(docker外で)
docker ps

#例
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                                         NAMES
41038ac225ec   pytws_rkawaguchi:v1          "/bin/bash"              4 seconds ago   Up 4 seconds   0.0.0.0:6006->6006/tcp, [::]:6006->6006/tcp   pytws_rkawaguchi

# 例：コンテナ名が pytws_rkawaguchi の場合
docker stop pytws_rkawaguchi     # 停止
docker rm   pytws_rkawaguchi     # （--rm で作っていなければ）削除
```

```
# docker imageの一覧を確認(docker外で)
docker images

# 例
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker images
REPOSITORY                         TAG       IMAGE ID       CREATED              SIZE
pytws_rkawaguchi                   v1        567510fe9770   About a minute ago   6.19GB
```

```
# 例：image名がpytws_rkawaguchi, TAGが v1 の場合
docker rmi pytws_rkawaguchi:v1

# 例：image idが 567510fe9770 の場合
docker image rm 567510fe9770
```