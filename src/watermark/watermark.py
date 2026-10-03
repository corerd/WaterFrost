"""
Wrapper: Expose a controlled API from a stable layer
instead of letting callers import deep internal modules directly, 
"""
from .lib._watermark_impl import watermark_apply, watermark_extract  # pyright: ignore[reportMissingImports]

__all__ = ["watermark_apply", "watermark_extract"]
