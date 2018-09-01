from __future__ import absolute_import

from .client import StatsClient
from .client import TCPStatsClient


VERSION = (3, 2, 2, 3)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['StatsClient', 'ConsistentHashingStatsClient', 'TCPStatsClient']
