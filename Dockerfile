# ベース：公式 PyTorch CUDA 12.4 ランタイム
FROM pytorch/pytorch:2.4.1-cuda12.4-cudnn9-runtime

# 必要に応じ apt 追加
RUN apt-get update && apt-get install -y git nano && \
    rm -rf /var/lib/apt/lists/*

# ワークディレクトリ
WORKDIR /workspace

# 依存ライブラリ（最小限）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# デフォルト CMD（対話用）
CMD ["/bin/bash"]
