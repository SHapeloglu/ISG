# -*- coding: utf-8 -*-
import os
import base64
from cryptography.fernet import Fernet


class EncryptionHelper:
    """KVKK-uyumlu Fernet tabanlı encryption helper"""

    def __init__(self):
        """Encryption key'i env veya default'tan oku"""
        self.key = self._load_key()
        self.cipher = Fernet(self.key)

    def _load_key(self):
        """
        Encryption key'i şu sıraya göre oku:
        1. ISG_ENCRYPTION_KEY env var
        2. ~/.isg_encryption_key dosyası
        3. Fallback: Fernet.generate_key() (dev-only)
        """
        # Env var'dan
        env_key = os.environ.get('ISG_ENCRYPTION_KEY')
        if env_key:
            return env_key.encode() if isinstance(env_key, str) else env_key

        # Dosyadan (~/.isg_encryption_key)
        key_file = os.path.expanduser('~/.isg_encryption_key')
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()

        # Fallback (geliştirme için)
        return Fernet.generate_key()

    def encrypt(self, plaintext):
        """Plaintext'i şifrele"""
        if not plaintext:
            return None
        data = plaintext.encode() if isinstance(plaintext, str) else plaintext
        encrypted = self.cipher.encrypt(data)
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, ciphertext):
        """Ciphertext'i deşifrele"""
        if not ciphertext:
            return None
        try:
            decoded = base64.b64decode(ciphertext.encode() if isinstance(ciphertext, str) else ciphertext)
            decrypted = self.cipher.decrypt(decoded)
            return decrypted.decode('utf-8')
        except Exception as e:
            # Decryption başarısız (invalid key, corrupted data)
            return f"[Decryption Error: {str(e)}]"


# Global helper instance (thread-safe değil, ama Odoo context'te sorun yok)
_encryption_helper = None


def get_encryption_helper():
    """Singleton encryption helper döndür"""
    global _encryption_helper
    if _encryption_helper is None:
        _encryption_helper = EncryptionHelper()
    return _encryption_helper
