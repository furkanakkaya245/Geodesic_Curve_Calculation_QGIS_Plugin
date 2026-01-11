from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSignal

class FlowMapGeneratorDialog(QDialog):
    signal_paths_selected = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(FlowMapGeneratorDialog, self).__init__(parent)
        self.setWindowTitle("Jeodezik Akış Haritası")
        self.resize(400, 150)
        layout = QVBoxLayout(self)

        # UI Elemanları
        self.air_input = QLineEdit()
        self.rot_input = QLineEdit()
        
        btn_air = QPushButton("Havalimanı Seç")
        btn_air.clicked.connect(lambda: self.get_path(self.air_input))
        
        btn_rot = QPushButton("Rota Seç")
        btn_rot.clicked.connect(lambda: self.get_path(self.rot_input))

        btn_run = QPushButton("HARİTAYI OLUŞTUR")
        btn_run.clicked.connect(self.submit)

        # Yerleşim
        l1 = QHBoxLayout(); l1.addWidget(self.air_input); l1.addWidget(btn_air)
        l2 = QHBoxLayout(); l2.addWidget(self.rot_input); l2.addWidget(btn_rot)
        layout.addLayout(l1); layout.addLayout(l2); layout.addWidget(btn_run)

    def get_path(self, widget):
        path, _ = QFileDialog.getOpenFileName(self, "Excel Seç", "", "Excel (*.xlsx)")
        if path: widget.setText(path)

    def submit(self):
        if self.air_input.text() and self.rot_input.text():
            self.signal_paths_selected.emit(self.air_input.text(), self.rot_input.text())
            self.accept()
        else:
            QMessageBox.warning(self, "Hata", "Dosyaları seçmedin!")