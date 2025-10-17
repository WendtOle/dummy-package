"""Console output utilities for server startup."""

import sys
from datetime import datetime


def print_startup_message():
    """Print a startup message to the console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
{'=' * 60}
    STARTUP UTILS PACKAGE LOADED SUCCESSFULLY
{'=' * 60}
    Timestamp: {timestamp}
    Package: startup_utils
    Status: ✓ Ready
{'=' * 60}
"""

    print(message, file=sys.stdout, flush=True)
