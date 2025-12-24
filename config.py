# config.py
import os
from pathlib import Path

# 路径相关
BASE_DIR = Path(__file__).resolve().parent
APK_DIR = BASE_DIR / "data" / "apks"
WORKSPACE_DIR = BASE_DIR / "data" / "workspace"
RESULTS_DIR = BASE_DIR / "data" / "results"
TOOLS_DIR = BASE_DIR / "tools"

# 输出目录 (全部放入 workspace/ 文件夹)
DECOMPILED_DIR = WORKSPACE_DIR / "decompiled"
METHODS_EXTRACTED_DIR = WORKSPACE_DIR / "methods_extracted"

# LLM 配置
OPENAI_API_KEY = "sk-KN3twIV81HwCSYGT185f8b052b61449aBa24287c7b031608"
OPENAI_BASE_URL = "https://free.v36.cm/v1"
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.2
MAX_COMPONENTS_FOR_STAGE1 = 200      # 组件级摘要最多条数
MAX_METHODS_PER_MODULE_STAGE2 = 80   # 单模块方法摘要最多条数
MAX_METHODS_PER_EDIT_CALL = 3        # 每次同时修改代码的方法数量

# 工具路径（根据你本机环境调整）
APKTOOL_PATH = TOOLS_DIR / "apktool_2.11.1.jar"  # 放在 PATH 里可直接写命令名
ZIPALIGN_PATH = r"C:\Users\yulan\AppData\Local\Android\Sdk\build-tools\36.1.0\zipalign.exe" 
APKSIGNER_PATH = r"C:\Users\yulan\AppData\Local\Android\Sdk\build-tools\36.1.0\apksigner.bat"

# 重建 & 签名配置
KEYSTORE = TOOLS_DIR / "my-release-key.jks"
KEY_ALIAS = "myapp"
KEYSTORE_PASS = "123456"

# 辅助函数：用于创建所有输出目录
def setup_directories():
    """创建所有必需的输出目录"""
    dirs_to_create = [
        DECOMPILED_DIR,
        METHODS_EXTRACTED_DIR,
        
    ]
    for dir_path in dirs_to_create:
        os.makedirs(dir_path, exist_ok=True)