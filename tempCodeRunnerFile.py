def goto_add_pat(self):
        self.add_pat = add_patients.add_patient_window()
        widget.addWidget(self.add_pat)
        widget.setCurrentIndex(widget.currentIndex() + 1)
