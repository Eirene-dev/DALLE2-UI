import os
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog,
                             QListWidget, QHBoxLayout, QAbstractItemView)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


# 이미지 생성 함수
def generate_image(prompt, api_key):
    url = f'https://api.openai.com/v1/images/generations'
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'num_images': 1,
        'size': '512x512'
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['data'][0]['url']

class Dalle2App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # API Key QLabel and QLineEdit
        self.api_key_label = QLabel("OpenAI API Key:", self)
        self.api_key_input = QLineEdit(self)
        self.api_key_input.setPlaceholderText("Enter your API key here")
        main_layout.addWidget(self.api_key_label)
        main_layout.addWidget(self.api_key_input)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setText('생성된 이미지가 여기에 표시됩니다.')
        main_layout.addWidget(self.image_label)

        history_layout = QHBoxLayout()

        self.history_list = QListWidget(self)
        self.history_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.history_list.itemDoubleClicked.connect(self.load_prompt_from_history)
        history_layout.addWidget(self.history_list)

        self.text_edit = QTextEdit(self)
        history_layout.addWidget(self.text_edit)

        main_layout.addLayout(history_layout)

        generate_button = QPushButton('이미지 생성', self)
        generate_button.clicked.connect(self.generate_and_display_image)
        main_layout.addWidget(generate_button)

        save_button = QPushButton('이미지 저장', self)
        save_button.clicked.connect(self.save_image)
        main_layout.addWidget(save_button)

        self.setLayout(main_layout)
        self.setWindowTitle('DALL-E 2 PyQt 애플리케이션')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def generate_and_display_image(self):
        prompt = self.text_edit.toPlainText()
        self.add_prompt_to_history(prompt)
        api_key = self.api_key_input.text()

        if not api_key:
            self.image_label.setText("Please enter your OpenAI API key.")
            return

        image_url = generate_image(prompt, api_key)

        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(image_url).content)
        self.image_label.setPixmap(pixmap.scaled(512, 512, Qt.KeepAspectRatio))

    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(self, '이미지 저장', '', 'Images (*.png *.jpg)')
        if file_name:
            self.image_label.pixmap().save(file_name)

    def add_prompt_to_history(self, prompt):
        if not prompt.strip():
            return

        for index in range(self.history_list.count()):
            if self.history_list.item(index).text() == prompt:
                self.history_list.takeItem(index)
                break

        self.history_list.insertItem(0, prompt)
        self.history_list.setCurrentRow(0)

    def load_prompt_from_history(self, item):
        self.text_edit.setPlainText(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dalle2App()
    sys.exit(app.exec_())

