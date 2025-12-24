# main.py
import src.static_analysis.decompiler as decompiler_module
import config  # 确保config模块可被正确导入

if __name__ == "__main__":
    decompiler_module.extract_methods()