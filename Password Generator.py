from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QHBoxLayout
)
from PySide6.QtCore import Qt
import secrets
import string
import random
from cryptography.fernet import Fernet
import os
import sys

# Load or generate master key
def load_or_create_master_key():
    if not os.path.exists("master.key"):
        key = Fernet.generate_key()
  # Generate a new encryption key if not already saved
        with open("master.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("master.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

def load_encrypted_passwords():
    encrypted = set()
    if os.path.exists("encrypted_passwords.txt"):
        with open("encrypted_passwords.txt", "rb") as file:
            for line in file:
                encrypted.add(line.strip())
    return encrypted

def save_encrypted_password(enc_password):
    with open("encrypted_passwords.txt", "ab") as file:
        file.write(enc_password + b"\n")

def generate_password(key):
    user_seed = sum(ord(c) for c in key)
    secrets_gen = secrets.SystemRandom(user_seed)
  # Use seed-based secure random generator for reproducibility
    length = random.randint(12, 24)
  # Random password length between 12 and 24 characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
  # Use full character set: letters, digits, punctuation

    while True:
        password = ''.join(secrets_gen.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password



class PasswordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setMinimumSize(400, 250)

        # Encryption setup
        self.fernet = load_or_create_master_key()
        self.saved_passwords = load_encrypted_passwords()
        self.prompted_to_save_decrypted = False

        # GUI Layout
        self.layout = QVBoxLayout()
        self.key_input = QLineEdit()
        self.result_label = QLabel("")

        self.init_ui()
        self.setLayout(self.layout)

    def init_ui(self):
        self.layout.addWidget(QLabel("Enter key:"))
        self.layout.addWidget(self.key_input)

        btn_layout = QHBoxLayout()
        self.gen_btn = QPushButton("Generate Password")
        self.gen_btn.clicked.connect(self.on_generate)
        btn_layout.addWidget(self.gen_btn)

        self.save_btn = QPushButton("Save Password")
        self.save_btn.clicked.connect(self.on_accept)
        self.save_btn.setEnabled(False)
        btn_layout.addWidget(self.save_btn)

        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.copy_btn.setEnabled(False)
        btn_layout.addWidget(self.copy_btn)

        self.layout.addLayout(btn_layout)
        self.layout.addWidget(self.result_label)

    def on_generate(self):
        key = self.key_input.text().strip().replace(" ", "")
        if not key:
            QMessageBox.warning(self, "Input Error", "Please enter a valid key.")
            return

        decrypted_passwords = set()
        for enc in self.saved_passwords:
            try:
                decrypted_passwords.add(self.fernet.decrypt(enc).decode())
            except Exception:
                continue

        for _ in range(1000):
            password = generate_password(key)
            if password not in decrypted_passwords:
  # Ensure the password is not already saved
                self.current_password = password
                self.result_label.setText(f"Generated Password:\n{password}")
                self.save_btn.setEnabled(True)
                return

        QMessageBox.warning(self, "Generation Error", "Could not generate a unique password. Try a different key.")

    def on_accept(self):
        enc_password = self.fernet.encrypt(self.current_password.encode())
        if enc_password in self.saved_passwords:
            QMessageBox.information(self, "Duplicate", "This password is already saved.")
            return

        save_encrypted_password(enc_password)
        self.saved_passwords.add(enc_password)
        QMessageBox.information(self, "Saved", "Password has been saved.")
        self.copy_btn.setEnabled(True)
  # Enable clipboard copy button after saving

        if not self.prompted_to_save_decrypted:
            self.prompted_to_save_decrypted = True
            decrypted = []
            for enc in self.saved_passwords:
                try:
                    decrypted.append(self.fernet.decrypt(enc).decode())
  # Decrypt each password for plaintext viewing
                except Exception:
                    continue

            if decrypted:
                save_prompt = QMessageBox.question(
                    self, "Save Decrypted Passwords",
                    "Do you want to save all decrypted passwords to decrypted_passwords.txt?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if save_prompt == QMessageBox.Yes:
                    with open("decrypted_passwords.txt", "w") as f:
                        for pwd in decrypted:
                            f.write(pwd + "\n")

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.current_password)
  # Copy generated password to the clipboard
        QMessageBox.information(self, "Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordApp()
    window.show()
    sys.exit(app.exec())
