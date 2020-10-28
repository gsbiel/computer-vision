import tkinter
from .mySlider import MySlider

STYLING_PARAMETERS = {
  "masterFrame_pady":20,
  "slider_pady":1,
  "labelView_width":16,
  "buttons_width": 15,
}

CONFIG_PARAMS = {
  "slider_minimum_angle":0,
  "slider_maximum_angle":360,
  "slider_steps":2
}

class RotationControlsView:

  def __init__(self, parentView, viewModel):

    # STATE VARIABLES
    self._x_rotation_value = tkinter.IntVar()
    self._x_rotation_value.set(0)

    self._y_rotation_value = tkinter.IntVar()
    self._y_rotation_value.set(0)

    self._z_rotation_value = tkinter.IntVar()
    self._z_rotation_value.set(0)

    # Container
    self._masterFrame = tkinter.Frame(parentView)
    self._masterFrame.pack(pady=STYLING_PARAMETERS["masterFrame_pady"])

    # Label
    self._selectorLabel = tkinter.Label(
                                        self._masterFrame, 
                                        text="Rotation Controls", 
                                        width=STYLING_PARAMETERS["labelView_width"]
                                      )
    self._selectorLabel.pack()

    # X axis slider
    self._x_rotation_slider = MySlider(  
                                        self._masterFrame, 
                                        self._x_rotation_value, 
                                        "X", 
                                        CONFIG_PARAMS["slider_minimum_angle"], 
                                        CONFIG_PARAMS["slider_maximum_angle"], 
                                        CONFIG_PARAMS["slider_steps"]
                                      )
    self._x_rotation_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # Y axis slider
    self._y_rotation_slider = MySlider(
                                        self._masterFrame, 
                                        self._y_rotation_value, 
                                        "Y", 
                                        CONFIG_PARAMS["slider_minimum_angle"], 
                                        CONFIG_PARAMS["slider_maximum_angle"], 
                                        CONFIG_PARAMS["slider_steps"]
                                      )
    self._y_rotation_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # Z axis slider
    self._z_rotation_slider = MySlider(
                                        self._masterFrame, 
                                        self._z_rotation_value, 
                                        "Z", 
                                        CONFIG_PARAMS["slider_minimum_angle"], 
                                        CONFIG_PARAMS["slider_maximum_angle"], 
                                        CONFIG_PARAMS["slider_steps"]
                                      )
    self._z_rotation_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    self.__registerForEvents(viewModel)
    return

  def __registerForEvents(self, viewModel):
    self._x_rotation_value.trace("w", lambda *args: viewModel.xOrientationChanged(self._x_rotation_value.get()))
    self._y_rotation_value.trace("w", lambda *args: viewModel.yOrientationChanged(self._y_rotation_value.get()))
    self._z_rotation_value.trace("w", lambda *args: viewModel.zOrientationChanged(self._z_rotation_value.get()))
    return
