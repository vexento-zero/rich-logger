# 📝 Rich-Logger

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/vexento-zero/rich-logger.svg?style=social)](https://github.com/vexento-zero/rich-logger/stargazers)

**Rich-Logger** 是一个基于 `loguru` 封装的极简、美观且专业的 Python 日志库。它专为追求终端输出美感的开发者设计，预设了高对比度的配色方案，并自动过滤冗余的系统警告。

---

## ✨ 特性

- 🚀 **即插即用**：无需繁琐配置，一行代码即可获得精美日志。
- 🎨 **精美配色**：采用 `bold` + `light-green/cyan` 配色方案，信息层级分明。
- 🧹 **纯净输出**：自动屏蔽 `logging` 库的冗余信息和 `warnings` 警告，让控制台只关注核心业务。
- 🛠️ **基于 Loguru**：继承了 `loguru` 的所有强大功能（线程安全、异步支持、日志回滚等）。

---

## 📸 预览

在终端中，输出将带有加粗和亮丽的色彩：

```text
[ INFO ] | [ main ] | Starting application...
[SUCCESS] | [utils] | Data processed successfully.
[WARNING] | [logic] | This is a warning message.
[ ERROR ] | [ api  ] | Connection failed: Timeout.
```

---

## 📦 安装

由于该项目目前托管在 GitHub，你可以通过以下命令直接安装：

```bash
pip install git+https://github.com/vexento-zero/rich-logger.git
```

或者将其添加到你的 `requirements.txt`：

```text
rich-logger @ git+https://github.com/vexento-zero/rich-logger.git
```

---

## 🚀 快速开始

使用非常简单，只需从 `rich_logger` 导入预配置好的 `logger`：

```python
from rich_logger import logger

def main():
    logger.info("这是一条普通信息")
    logger.success("这是一条成功信息")
    logger.warning("这是一条警告信息")
    logger.error("这是一条错误信息")
    logger.critical("这是一条严重错误信息")

if __name__ == "__main__":
    main()
```

---

## 🛠️ 核心逻辑

**Rich-Logger** 在初始化时自动执行了以下优化：

1. **全局静默**：调用 `logging.disable(logging.CRITICAL)` 以隐藏第三方库（如 `requests`, `urllib3`, `boto3`）产生的杂乱日志。
2. **警告过滤**：自动执行 `warnings.filterwarnings("ignore")`，屏蔽 Python 原生的 DeprecationWarning 等干扰。
3. **自定义格式化**：
   - **Level**: 居中对齐，使用高亮色彩标识。
   - **Function**: 自动捕获并显示调用日志的函数名。
   - **Message**: 核心消息内容使用清晰的白色加粗显示。

---

## 🤝 贡献

如果你有更好的配色方案或功能建议，欢迎提交 **Issue** 或 **Pull Request**！

如果这个项目对你有帮助，请给一个 **⭐ Star**，这是对我最大的支持！

---

## 📄 开源协议

本项目采用 [MIT](LICENSE) 协议。