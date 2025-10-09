from abc import ABC, abstractmethod

from common.files import get_latest_version_file


class BaseModel(ABC):
    """Abstract base class for ML models."""

    def __init__(self, model_dir: str = "app/artifacts"):
        self.model = None
        self.model_dir = model_dir

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def get_latest_model_path(self) -> str:
        """
        Find the latest model file based on version number (e.g., model_v2.pkl).
        """
        latest_file = get_latest_version_file(self.model_dir, self.name, "pkl")
        return latest_file
