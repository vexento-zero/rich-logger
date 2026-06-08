import sys
from loguru import logger
import logging
import warnings
from rich.console import Console
from rich.live import Live
from rich.text import Text

# --- 原有配置保持不变 ---
logging.disable(logging.CRITICAL)
warnings.filterwarnings("ignore")

logger.remove()
custom_format = (
    "<bold><light-green><level>[{level: ^8}]</level> | </light-green></bold>"
    "<bold><light-cyan>[{function: ^10}] | </light-cyan></bold>"
    "<bold><light-white>{message}</light-white></bold>"
)
logger.add(sys.stdout, format=custom_format, colorize=True)

# --- 新增：支持流式输出的类 ---
class StreamPrinter:
    def __init__(self, level="INFO", function="STREAM"):
        self.console = Console()
        self.level = level.upper()
        self.function = function
        self.text = Text()
        self._setup_prefix()
        self.live = Live(self.text, console=self.console, refresh_per_second=12, transient=False)

    def _setup_prefix(self):
        # 模拟 loguru 的配色方案
        self.text.append(f"[{self.level: ^8}]", style="bold light_green")
        self.text.append(" | ", style="bold light_green")
        self.text.append(f"[{self.function: ^10}]", style="bold light_cyan")
        self.text.append(" | ", style="bold light_cyan")

    def __enter__(self):
        self.live.start()
        return self

    def update(self, chunk: str, style="bold white"):
        """追加新字符并刷新界面"""
        self.text.append(chunk, style=style)
        self.live.update(self.text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.live.stop()
        # 结束后打印一个换行，确保下一条日志正常
        # self.console.print()

# 导出方便调用
logger.stream = StreamPrinter
