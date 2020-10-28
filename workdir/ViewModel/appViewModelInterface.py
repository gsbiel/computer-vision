from abc import ABC, abstractmethod

class ApplicationViewModelInterface(ABC):
  """
  This interface is intended to refresh figures in ApplicationView
  """
  @abstractmethod
  def objectViewShouldUpdate(self) -> None:
    pass
  
  @abstractmethod
  def cameraViewShouldUpdate(self) -> None:
    pass

  @abstractmethod
  def projectionPlotShouldUpdate(self) -> None:
    pass