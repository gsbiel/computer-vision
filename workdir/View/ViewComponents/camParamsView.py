
import tkinter
from .mySlider import MySlider

STYLING_PARAMETERS = {
  "masterFrame_pady":20,
  "slider_pady":1,
  "labelView_width":16,
}

CONFIG_PARAMS = {
  "f_minimum_value":0,
  "f_maximum_value":1000,
  "f_step":2,
  "initial_f":2,

  "sx_minimum_value":0,
  "sx_maximum_value":10,
  "sx_step":0.1,
  "initial_sx":4.7,

  "sy_minimum_value":0,
  "sy_maximum_value":10,
  "sy_step":0.1,
  "initial_sy":6.5,

  "stheta_minimum_value":0,
  "stheta_maximum_value":10,
  "stheta_step":0.1,
  "initial_stheta":0.0,

  "ox_minimum_value":0,
  "ox_maximum_value":640,
  "ox_step":10,
  "initial_ox":60,

  "oy_minimum_value":0,
  "oy_maximum_value":480,
  "oy_step":10,
  "initial_oy":60,
}

class CameraParamsView:

  def __init__(self, parentView, viewModel):

    # STATE VARIABLES
    self._f_value = tkinter.IntVar()
    self._f_value.set(CONFIG_PARAMS["initial_f"])

    self._sx_value = tkinter.DoubleVar()
    self._sx_value.set(CONFIG_PARAMS["initial_sx"])

    self._sy_value = tkinter.DoubleVar()
    self._sy_value.set(CONFIG_PARAMS["initial_sy"])

    self._stheta_value = tkinter.DoubleVar()
    self._stheta_value.set(CONFIG_PARAMS["initial_stheta"])

    self._ox_value = tkinter.IntVar()
    self._ox_value.set(CONFIG_PARAMS["initial_ox"])

    self._oy_value = tkinter.IntVar()
    self._oy_value.set(CONFIG_PARAMS["initial_oy"])

    # Container
    self.masterFrame = tkinter.Frame(parentView)
    self.masterFrame.pack(pady=STYLING_PARAMETERS["masterFrame_pady"])

    # Label
    intrinsic_params_label = tkinter.Label(
                                            self.masterFrame, 
                                            text="Intrinsic Params", 
                                            width=STYLING_PARAMETERS["labelView_width"])
    intrinsic_params_label.pack()

    # f slider
    f_slider = MySlider(
                          self.masterFrame, 
                          self._f_value, 
                          "f", 
                          CONFIG_PARAMS["f_minimum_value"], 
                          CONFIG_PARAMS["f_maximum_value"], 
                          CONFIG_PARAMS["f_step"]
                        )
    f_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # sx slider
    sx_slider = MySlider(
                          self.masterFrame, 
                          self._sx_value,
                          "sx",
                          CONFIG_PARAMS["sx_minimum_value"], 
                          CONFIG_PARAMS["sx_maximum_value"], 
                          CONFIG_PARAMS["sx_step"]
                        )
    sx_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # sy slider
    sy_slider = MySlider(
                          self.masterFrame, 
                          self._sy_value,
                          "sy",
                          CONFIG_PARAMS["sy_minimum_value"], 
                          CONFIG_PARAMS["sy_maximum_value"], 
                          CONFIG_PARAMS["sy_step"]
                        )
    sy_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # stheta slider
    s_theta_slider = MySlider(
                                self.masterFrame, 
                                self._stheta_value,
                                "s_theta",
                                CONFIG_PARAMS["stheta_minimum_value"], 
                                CONFIG_PARAMS["stheta_maximum_value"], 
                                CONFIG_PARAMS["stheta_step"] 
                              )
    s_theta_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # ox slider
    ox_slider = MySlider(
                          self.masterFrame, 
                          self._ox_value, 
                          "ox", 
                          CONFIG_PARAMS["ox_minimum_value"], 
                          CONFIG_PARAMS["ox_maximum_value"], 
                          CONFIG_PARAMS["ox_step"]
                        )
    ox_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    # oy slider
    oy_slider = MySlider(
                          self.masterFrame, 
                          self._oy_value, 
                          "oy", 
                          CONFIG_PARAMS["oy_minimum_value"], 
                          CONFIG_PARAMS["oy_maximum_value"], 
                          CONFIG_PARAMS["oy_step"]
                        )
    oy_slider.pack(pady=STYLING_PARAMETERS["slider_pady"])

    self.__registerForEvents(viewModel)

    return

  def __registerForEvents(self, viewModel):
    self._f_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    self._sx_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    self._sy_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    self._stheta_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    self._ox_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    self._oy_value.trace("w", lambda *args: viewModel.intrinsincParamsChanged(
                                                                              self._f_value.get(), 
                                                                              self._sx_value.get(), 
                                                                              self._sy_value.get(), 
                                                                              self._stheta_value.get(), 
                                                                              self._ox_value.get(), 
                                                                              self._oy_value.get()
                                                                            ))
    return

