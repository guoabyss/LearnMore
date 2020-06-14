import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":

    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    w.resize(400, 150)
    w.move(300, 300)
    # 设置标题
    w.setWindowTitle("第一个GUI")
    w.show()

    sys.exit(app.exec_())
