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
