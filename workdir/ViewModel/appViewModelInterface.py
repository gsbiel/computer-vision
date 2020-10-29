from abc import ABC, abstractmethod

class ApplicationViewModelInterface(ABC):
  """
  This interface is intended to refresh figures in ApplicationView
  """
  @abstractmethod
  def worldViewShouldUpdate(self) -> None:
    pass

  @abstractmethod
  def projectionViewShouldUpdate(self) -> None:
    pass