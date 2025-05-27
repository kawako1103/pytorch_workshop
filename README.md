# pytorch_workshop
This is the repository for new members of ai-lab who have never used Pytorch and want to use it for the first time.

# 1. リポジトリ取得
```
git clone https://github.com/kawako1103/pytorch_workshop.git
cd pytorch_workshop
```

# 2. Docker イメージを “自分の名前タグ” でビルド(pytwsはpytorch workshopの短縮形のつもり。whoamiはユーザによって自動的に変わるので特に変更せずともわかりやすい。8~9分ほどかかるかと。。)
```
docker build -t pytws_$(whoami):v1 .
```

# ※build後にimagesが作成される(例えば:ユーザ名:rkawaguchiの場合以下のように名前が付く)
```
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker images
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
pytws_rkawaguchi                   v1        36097820484b   51 seconds ago   6.14GB
```


# 3. コンテナ起動（作業ディレクトリをマウント）(--gpus allをつけると gpuが使える/ --rmをつけるとdocker stopをした時に自動的にコンテナが削除される/-v　リポジトリを/workspaceにマウント)
```
docker run --gpus all --name pytws_$(whoami) -it --rm \
  -v $(pwd):/workspace \
  pytws_$(whoami):v1

```

# ※コンテナ起動後にユーザ名が付されたコンテナが確認できる(例えば:ユーザ名:rkawaguchiなら↓)
```
rkawaguchi@ailab-SYS-7039A-I:~/pytorch_workshop$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                NAMES
ee30f085af11   pytws_rkawaguchi:v1           "/bin/bash"              7 seconds ago   Up 6 seconds                        pytws_rkawaguchi
```

# ※gpuが利用できるか確認する(nvidia-smiで下のように何か出てくればOK)
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

# 4. 教材を実行
```
python src/train_mnist.py
```

# 5. 終了時にコンテナを削除 (--rm オプションで自動削除)
```
# 動作中のコンテナ一覧を確認(docker外で)
docker ps

# 例：コンテナ名が pytws_rkawaguchi の場合
docker stop pytws_rkawaguchi     # 停止
docker rm   pytws_rkawaguchi     # （--rm で作っていなければ）削除
```