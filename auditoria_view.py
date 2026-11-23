from datetime import datetime


class LogAuditoriaView:

  def __init__(self, view_model, arquivo_log="auditoria.log"):
    self.vm = view_model
    self.arquivo_log = arquivo_log
    self.vm.registrar_observador(self.registrar_evento)

  def registrar_evento(self):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = (
        f"[{agora}] Casos: {self.vm.total_casos} | "
        f"Risco Médio: {self.vm.media_periculosidade:.1f}/10 | "
        f"Status: {self.vm.status_sistema}\n"
    )
    with open(self.arquivo_log, "a", encoding="utf-8") as f:
      f.write(linha)