# main.py
from pathlib import Path
from config import APK_DIR
from src.pipeline.orchestrator import PipelineRunner


def main():
    # 简单起见：对 apks/ 里前几个 APK 跑一遍
    apk_paths = sorted(APK_DIR.glob("*.apk"))[:3]

    for apk in apk_paths:
        print(f"=== Processing {apk.name} ===")
        runner = PipelineRunner(apk)
        runner.run_once()


if __name__ == "__main__":
    main()