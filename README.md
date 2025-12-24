一、项目目录结构
llm_android_adv/
├─ README.md
├─ requirements.txt
├─ config.py              # 全局配置（API key、路径、模型名等）
├─ main.py                # 入口：跑整个分阶段、多轮交互流程
├─ data/
│  ├─ apks/               # 原始 APK
│  ├─ workspace/          # 每个 APK 的解包、分析、修改中间文件
│  └─ results/            # 实验结果（日志、检测结果等）
└─ src/
   ├─ __init__.py
   ├─ static_analysis/    # 阶段0：本地静态分析 & 信息压缩
   │  ├─ __init__.py
   │  ├─ decompiler.py        # 调用 apktool 等
   │  ├─ feature_extractor.py # 提取组件/方法级摘要、调用子图
   │  └─ metadata_types.py    # 各种数据结构定义
   │
   ├─ index/             # 索引 & 检索（RAG 风格）
   │  ├─ __init__.py
   │  ├─ index_store.py      # 把 MethodID→代码、调用关系落地（JSON/SQLite）
   │  └─ retriever.py        # 按组件/方法ID取摘要或源码
   │
   ├─ llm/               # LLM 调用 & 各阶段 prompt 封装
   │  ├─ __init__.py
   │  ├─ client.py           # 封装 OpenAI/其他模型
   │  ├─ prompts.py          # 各阶段的 prompt 模板
   │  ├─ stage1_module_selector.py  # 阶段1：全局模块筛选
   │  ├─ stage2_method_selector.py  # 阶段2：局部方法选取
   │  └─ stage3_code_editor.py      # 阶段3：代码修改
   │
   └─ pipeline/          # 总控和验证
      ├─ __init__.py
      ├─ orchestrator.py     # 串起各阶段：一款 APK 一次完整迭代
      └─ validator.py        # 重打包、安装、检测、结果摘要