"""Memory graph store."""

import logging

from dbgpt._private.pydantic import ConfigDict
from dbgpt.storage.graph_store.base import GraphStoreBase, GraphStoreConfig
from dbgpt.storage.graph_store.graph import MemoryGraph

logger = logging.getLogger(__name__)


class MemoryGraphStoreConfig(GraphStoreConfig):
    """Memory graph store config."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class MemoryGraphStore(GraphStoreBase):
    """Memory graph store."""

    def __init__(self, graph_store_config: MemoryGraphStoreConfig):
        """Initialize MemoryGraphStore with a memory graph."""
        self._graph_store_config = graph_store_config
        self._graph = MemoryGraph()

    def get_config(self):
        """Get the graph store config."""
        return self._graph_store_config

    def _escape_quotes(self, text: str) -> str:
        """Escape single and double quotes in a string for queries."""
        raise NotImplementedError(
            "_escape_quotes is not implemented by MemoryGraphStore"
        )
