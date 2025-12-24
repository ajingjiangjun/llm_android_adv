import pandas as pd
from datetime import datetime, timedelta

# ====== 参数区：根据自己需求修改 ======
META_FILE = "androzoo_2024-10-01.csv.gz"   # AndroZoo metadata 文件路径
OUTPUT_FILE = "filtered_5y_small_apks.csv" # 筛选结果输出文件

YEARS = 5                     # 近多少年
MAX_SIZE_MB = 10              # “较小” 的 apk 上限（MB），例如 10MB
CHUNK_SIZE = 200_000          # 每次读多少行，视内存情况可调
# ================================

# 计算时间下界：最近 YEARS 年
cutoff_date = datetime.today() - timedelta(days=365 * YEARS)
max_size_bytes = MAX_SIZE_MB * 1024 * 1024

# 只读取我们关心的列
usecols = ["sha256", "apk_size", "dex_date", "pkg_name"]

# 先写表头
with open(OUTPUT_FILE, "w", encoding="utf-8") as fout:
    fout.write("sha256,apk_size,dex_date,pkg_name\n")

# 分块读取 & 过滤
reader = pd.read_csv(
    META_FILE,
    compression="infer",  # 自动识别 gzip
    sep=";",              # AndroZoo 的 CSV 通常是分号分隔
    usecols=usecols,
    chunksize=CHUNK_SIZE,
    low_memory=True,
)

for i, chunk in enumerate(reader, start=1):
    # 解析日期
    chunk["dex_date"] = pd.to_datetime(chunk["dex_date"], errors="coerce")

    # 构造筛选条件：近 YEARS 年 & 体积小于阈值
    mask = (
        (chunk["dex_date"] >= cutoff_date) &
        (chunk["apk_size"] <= max_size_bytes)
    )

    sub = chunk.loc[mask, usecols]

    # 追加写入结果文件
    with open(OUTPUT_FILE, "a", encoding="utf-8") as fout:
        sub.to_csv(fout, header=False, index=False)

    print(f"Chunk {i} done, selected {len(sub)} rows.")