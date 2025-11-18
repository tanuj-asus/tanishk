import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMessageBox

class AttendanceSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Attendance System')

        # Layouts
        self.main_layout = QVBoxLayout()

        # Admin Panel
        self.admin_panel = QWidget()
        self.admin_layout = QFormLayout()
        self.admin_label = QLabel('Admin Panel')
        self.admin_panel.setLayout(self.admin_layout)
        self.admin_layout.addRow(self.admin_label)

        self.add_student_btn = QPushButton('Add Student')
        self.add_student_btn.clicked.connect(self.add_student)
        self.admin_layout.addRow(self.add_student_btn)

        self.main_layout.addWidget(self.admin_panel)

        # Attendance Marking Interface
        self.attendance_panel = QWidget()
        self.attendance_layout = QFormLayout()
        self.attendance_label = QLabel('Mark Attendance')
        self.student_name = QLineEdit()
        self.attendance_btn = QPushButton('Mark Attendance')
        self.attendance_btn.clicked.connect(self.mark_attendance)

        self.attendance_panel.setLayout(self.attendance_layout)
        self.attendance_layout.addRow(self.attendance_label)
        self.attendance_layout.addRow('Student Name:', self.student_name)
        self.attendance_layout.addRow(self.attendance_btn)

        self.main_layout.addWidget(self.attendance_panel)

        self.setLayout(self.main_layout)

    def add_student(self):
        QMessageBox.information(self, 'Info', 'Add Student feature is not implemented yet!')

    def mark_attendance(self):
        name = self.student_name.text()
        if name:
            QMessageBox.information(self, 'Info', f'Attendance marked for {name}!')
            self.student_name.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a student name!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    attendance_system = AttendanceSystem()
    attendance_system.show()
    sys.exit(app.exec_())