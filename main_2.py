from auditoria_view import LogAuditoriaView
from view import SuspeitoView
from view_model import SuspeitoViewModel

if __name__ == "__main__":
  vm = SuspeitoViewModel()
  log_view = LogAuditoriaView(vm)  # Segunda View inscrita no mesmo ViewModel
  view = SuspeitoView(vm)
  view.iniciar()
  