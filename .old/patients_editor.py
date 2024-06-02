import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
)
import sqlite3


class PatientEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Information Editor")
        self.setGeometry(
            100, 100, 800, 600
        )  # Set window geometry (x-position, y-position, width, height)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        # Create widgets
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()
        self.load_button = QPushButton("Load")
        self.save_button = QPushButton("Save")
        self.info_label = QLabel()
        self.info_label.setWordWrap(True)
        self.info_textbox = QTextEdit()

        # Create layout
        self.layout = QVBoxLayout()
        self.info_layout = QVBoxLayout()
        self.info_layout.addWidget(self.info_label)
        self.info_layout.addWidget(self.info_textbox)

        self.form_layout = QVBoxLayout()
        self.form_layout.addWidget(self.first_name_label)
        self.form_layout.addWidget(self.first_name_input)
        self.form_layout.addWidget(self.phone_label)
        self.form_layout.addWidget(self.phone_input)
        self.form_layout.addWidget(self.load_button)
        self.form_layout.addWidget(self.save_button)

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.info_layout)

        self.setLayout(self.layout)

        # Connect signals
        self.load_button.clicked.connect(self.load_patient_data)
        self.save_button.clicked.connect(self.save_patient_data)

    def load_patient_data(self):
        first_name = self.first_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not first_name or not phone:
            self.info_label.setText("Please enter first name and phone number.")
            return

        # Fetch patient data from database
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM patients WHERE f_name = ? AND phone = ?", (first_name, phone)
        )
        patient_data = cursor.fetchone()
        conn.close()

        if not patient_data:
            self.info_label.setText("Patient not found.")
            return

        # Display patient data in text boxes
        self.info_label.setText("Patient Information:")
        self.info_textbox.setText(
            "\n".join(
                [
                    f"{key}: {value}"
                    for key, value in zip(
                        [
                            "p_id",
                            "f_name",
                            "l_name",
                            "age",
                            "sex",
                            "phone",
                            "address",
                            "email",
                            "reg_date",
                            "date_of_departure",
                            "reference",
                            "complain",
                            "blood_diseases",
                            "smoker",
                            "bleeding_disorder",
                            "hepatitis",
                            "diabetes",
                            "epilepsy",
                            "kidney_cardiac_diseases",
                            "abnormal_bp",
                            "currently_medicated",
                            "respiratory_diseases",
                            "gum_bleed_brush",
                            "allergies",
                            "nervous",
                            "pregnant",
                            "breastfeeding",
                            "none_prb_above",
                            "med_find_",
                            "occupation",
                        ],
                        patient_data,
                    )
                ]
            )
        )

    def save_patient_data(self):
        first_name = self.first_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if not first_name or not phone:
            self.info_label.setText("Please enter first name and phone number.")
            return

        new_patient_data = self.info_textbox.toPlainText().split("\n")
        new_patient_data = [item.split(":") for item in new_patient_data]

        # Update patient data in database
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        # cursor.execute("UPDATE patients SET " + ", ".join([f"{item[0]} = ?" for item in new_patient_data]) + " WHERE f_name = ? AND phone = ?", ([item[1].strip() for item in new_patient_data], first_name, phone))
        placeholders = ", ".join([f"{item[0]} = ?" for item in new_patient_data])
        values = [item[1].strip() for item in new_patient_data]
        values.extend([first_name, phone])  # Add first_name and phone to values list
        query = f"UPDATE patients SET {placeholders} WHERE f_name = ? AND phone = ?"

        cursor.execute(query, values)

        conn.commit()
        conn.close()

        self.info_label.setText("Patient information updated.")


# """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = PatientEditor()
    sys.exit(app.exec_())
# """
