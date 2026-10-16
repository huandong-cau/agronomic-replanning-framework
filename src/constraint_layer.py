agronomic-replanning-framework/
├── README.md                # ⭐ 核心！必须包含下方模板内容
├── LICENSE                  # 推荐 MIT 或 Apache-2.0
├── CITATION.cff             # ⭐ 用于生成 Zenodo 引用元数据
├── data/
│   ├── raw/                 # 原始数据（不可修改）
│   ├── processed/           # 预处理后数据
│   └── README.md            # 说明数据来源、格式、字段含义
├── src/                     # 核心代码
│   ├── constraint_layer.py  # §3.2 Hard Constraint Enforcement
│   ├── bayesian_adapt.py    # §3.3 Bayesian Threshold Adaptation
│   ├── structured_handoff.py# §3.4 Structured Handoff Protocol
│   └── utils/
├── notebooks/               # Jupyter Notebook 示例/复现脚本
│   └── reproduce_fig3.ipynb # 对应论文图3的完整复现
├── docs/                    # 补充文档（可选）
│   └── agronomic_rules.md   # 农艺约束谓词列表（从正文移至此处）
└── requirements.txt         # Python 依赖版本锁定
  commit message
