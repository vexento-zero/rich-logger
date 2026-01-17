import sys
from loguru import logger
import logging
import warnings

# 禁用其他库的日志输出
logging.disable(logging.CRITICAL)
warnings.filterwarnings("ignore")

# 配置自定义格式
logger.remove()
custom_format = (
    "<bold><light-green><level>[{level: ^4}]</level> | </light-green></bold>"
    "<bold><light-cyan>[{function: ^4}] | </light-cyan></bold>"
    "<bold><light-white>{message: <20}</light-white></bold>"
)

logger.add(
    sys.stdout,
    format=custom_format,
    colorize=True,
)

# 导出 logger 供外部直接使用
__all__ = ["logger"]
