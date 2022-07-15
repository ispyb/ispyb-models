from typing import Dict, Any


class CustomBase:
    @property
    def _metadata(self) -> Dict[str, Any]:
        if not hasattr(self, "_additional_metadata"):
            self._additional_metadata: Dict[str, Any] = {}
        return self._additional_metadata
