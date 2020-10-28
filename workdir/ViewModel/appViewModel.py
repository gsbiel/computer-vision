

class ApplicationViewModel:

  def __init__(self):

    return

  
  # GUI EVENTS #################################################################
  
  def onKeyboardPressed(self, key):
    print('Key pressed: {value}'.format(value=key))
    return

  def selectedObjectChanged(self, currentObject):
    print('Object changed to: {value}'.format(value=currentObject))
    return