#!/usr/bin/env python3
"""
抓取 Google Scholar 数据并保存到 results/ 目录
"""

import os
import sys
import time
import random
import json
from datetime import datetime

from scholarly import scholarly, ProxyGenerator, MaxTriesExceededException

# --------------------------- 代理初始化 ---------------------------------
def init_scholar_session() -> None:
    """初始化 ProxyGenerator；若一种方式失败则自动尝试下一种。"""
    pg = ProxyGenerator()

    # 1) 免费轮换代理
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
        print("✅ 使用 FreeProxies() 轮换代理")
        return

    # 2) 本地 Tor
    if pg.Tor_Internal(tor_cmd="tor"):        # 需本机已安装 & 运行 tor
        scholarly.use_proxy(pg)
        print("✅ 使用本地 Tor 代理")
        return

    # 3) ScraperAPI（或你自己的付费代理）
    key = os.getenv("SCRAPERAPI_KEY")
    if key and pg.ScraperAPI(key):
        scholarly.use_proxy(pg)
        print("✅ 使用 ScraperAPI 代理")
        return

    raise RuntimeError("❌ 所有代理方式均失败，请检查网络或代理配置")

# --------------------------- 抓取函数 -----------------------------------
def fetch_author(author_id: str, max_retries: int = 4) -> dict:
    """抓取指定作者信息；失败时自动换代理并重试。"""
    for attempt in range(1, max_retries + 1):
        try:
            author = scholarly.search_author_id(author_id)
            scholarly.fill(
                author,
                sections=["basics", "indices", "counts", "publications"],
            )
            return author

        except MaxTriesExceededException as e:
            print(f"[{attempt}/{max_retries}] 请求被封：{e}")
        except Exception as e:
            print(f"[{attempt}/{max_retries}] 其他异常：{e}")

        # 若未返回，说明抓取失败，进行退避并刷新代理
        wait = 10 * attempt + random.uniform(0, 5)
        print(f"⏳ {wait:.1f}s 后重试…")
        time.sleep(wait)        # 指数退避
        init_scholar_session()  # 重新挂代理

    raise RuntimeError(f"❌ 重试 {max_retries} 次后仍无法抓取 {author_id}")

# --------------------------- 主流程 -------------------------------------
def main() -> None:
    author_id = os.getenv("GOOGLE_SCHOLAR_ID")
    if not author_id:
        sys.exit("🌟 请先设置环境变量 GOOGLE_SCHOLAR_ID")

    # 第一次初始化代理
    init_scholar_session()

    # 抓数据
    author = fetch_author(author_id)
    author["updated"] = datetime.now().isoformat(timespec="seconds")
    # 把 publications 从 list 转成 dict，key=author_pub_id
    author["publications"] = {p["author_pub_id"]: p for p in author["publications"]}

    # 输出到终端
    print(json.dumps(author, indent=2, ensure_ascii=False))

    # 保存文件
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(author, f, ensure_ascii=False)

    # shields.io 小徽章数据
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, ensure_ascii=False)

    print("✅ 抓取完成，结果已写入 results/")

# --------------------------- 入口 ---------------------------------------
if __name__ == "__main__":
    main()
