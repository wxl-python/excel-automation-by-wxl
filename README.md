# 🐍 Excel 文件批量合并工具

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-green)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

一个简单高效的 Python 脚本，用于自动合并多个 Excel 文件。专为财务、人事、销售等需要处理大量表格的岗位设计，可一键将多个 `.xlsx` 文件合并为一个，并自动去除空行、重置索引。

> 💡 **适用场景**：月度报表汇总、多部门数据合并、客户信息整合等重复性工作。

---

## ✨ 核心功能

- ✅ **批量合并**：自动读取指定文件夹下的所有 `.xlsx` 文件。
- ✅ **智能处理**：自动去除空行、重置索引，保持数据整洁。
- ✅ **灵活输出**：可自定义输出文件名和路径。
- ✅ **进度提示**：在终端实时显示处理进度。

---

## 🚀 快速开始

### 1. 环境准备
确保已安装 Python 3.8+，并安装所需依赖：
bash
pip install pandas openpyxl

### 2. 准备文件
将需要合并的 Excel 文件放入项目根目录的 `excels` 文件夹中（如果没有该文件夹，请手动创建）。

### 3. 运行脚本
在项目根目录下，执行以下命令：
bash
python "01-合并多个Excel文件.py"

### 4. 查看结果
运行后，会在项目根目录生成 `merged.xlsx` 文件，即合并后的结果。

---

## 📁 项目结构说明
excel-automation-by-wxl/      # 项目根目录
├── 01-合并多个Excel文件.py   # 主程序
├── excels/                   # 存放待合并的Excel文件
│   ├── 销售数据_1月.xlsx
│   └── 销售数据_2月.xlsx
├── merged.xlsx              # 程序运行后生成的合并结果
└── README.md                # 本说明文件
---

## ⚙️ 自定义配置
如需修改默认设置，可打开 `01-合并多个Excel文件.py` 文件，修改以下变量：
python
folder_path = "./excels"    # 输入文件夹路径，默认为当前目录下的 excels 文件夹
output_file = "merged.xlsx" # 输出文件名，可自定义
---

## ❓ 常见问题

**Q：支持 `.xls` 格式的Excel文件吗？**  
A：默认不支持。如需支持，请安装 `xlrd` 库：`pip install xlrd`，并修改代码中的读取逻辑。

**Q：合并后的表格顺序是？**  
A：按照文件在文件夹中的字母顺序依次合并。

**Q：如何保留空行？**  
A：默认会删除空行。如需保留，请删除代码中的 `dropna()` 方法。

---

## 📞 联系与支持

如有问题或需要定制功能，可通过以下方式联系：

- **邮箱**：1102103919@qq.com
- **微信**：13664693814

---

## 📄 开源协议

本项目基于 MIT 协议开源，可自由使用、修改和分发。
