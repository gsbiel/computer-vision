from View.applicationView import ApplicationView
from ViewModel.appViewModel import ApplicationViewModel

viewModel = ApplicationViewModel()
app = ApplicationView(viewModel)

app.startMainLoop()