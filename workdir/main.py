from View.applicationView import ApplicationView
from ViewModel.appViewModel import ApplicationViewModel

viewModel = ApplicationViewModel()
app = ApplicationView(viewModel)
viewModel.delegate = app
viewModel.refreshDisplays()
viewModel.updateProjection()
app.startMainLoop()