# pytorch_workshop
This is the repository for new members of ai-lab who have never used Pytorch and want to use it for the first time.

# 1. リポジトリ取得
```
git clone https://github.com/kawako1103/pytorch_workshop.git
cd pytorch_workshop
```

# 2. Docker イメージを “自分の名前タグ” でビルド
```
docker build -t pytws_$(whoami):v1 .
```

# 3. コンテナ起動（作業ディレクトリをマウント）
```
docker run --name pytws_$(whoami) -it --rm \
  -v $(pwd):/workspace \
  pytws_$(whoami):v1

```

# 4. 教材を実行
```
python src/train_mnist.py
```

# 5. 終了時にコンテナを削除 (--rm オプションで自動削除)
