"""
Maintain version for CropMl.
"""

MAJOR = 0
"""(int) Version major component."""

MINOR = 0
"""(int) Version minor component."""

POST = 2
"""(int) Version post or bugfix component."""

__version__ = ".".join([str(s) for s in (MAJOR, MINOR, POST)])
