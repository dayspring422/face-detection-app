import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'gui':
        from gui_app import FaceDetectionApp
        from PyQt5.QtWidgets import QApplication
        app = QApplication(sys.argv)
        ex = FaceDetectionApp()
        ex.show()
        sys.exit(app.exec_())
    else:
        from app import app
        app.run(debug=True)
