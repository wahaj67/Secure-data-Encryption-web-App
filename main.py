import streamlit as st
import sqlite3 as sql
import hashlib
import os
from cryptography.fernet import Fernet


KEY_FILE = 'key.key'


def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return key


cipher = Fernet(load_key())


def init_db():
    connect = sql.connect('data.db')
    con = connect.cursor()
    con.execute("""
        CREATE TABLE IF NOT EXISTS data (
            label TEXT PRIMARY KEY,
            encrypted_text TEXT,
            passkey TEXT
        )
    """)
    connect.commit()
    connect.close()


def hash_key(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


def encrypt(text):
    return cipher.encrypt(text.encode()).decode()


def decrypt(text):
    return cipher.decrypt(text.encode()).decode()


init_db()



st.title('🔐 Secure Data Encryption App')
menu = ['Store Secret', 'Retrieve Secret', 'About']
choice = st.sidebar.selectbox('Select Action', menu)


if choice == 'Store Secret':
    st.header('Store a New Secret')
    label = st.text_input('Label (Unique ID):')
    secret = st.text_area('Enter your Secret:')
    passkey = st.text_input('Enter Passkey:', type='password')

    if st.button('Encrypt and Save'):
        if label and secret and passkey:
            conn = sql.connect('data.db')
            c = conn.cursor()
            encrypted = encrypt(secret)
            hashed_key = hash_key(passkey)
            try:
                c.execute(
                    """INSERT INTO data (label, encrypted_text, passkey) VALUES (?, ?, ?)""",
                    (label, encrypted, hashed_key)
                )
                conn.commit()
                st.success('✅ Secret Saved Successfully!')
            except sql.IntegrityError:
                st.error('❌ Secret with this label already exists!')
            conn.close()
        else:
            st.warning('⚠️ Please fill all the fields!')


elif choice == 'Retrieve Secret':
    st.header('Retrieve a Secret')
    label = st.text_input('Label (Unique ID):')
    passkey = st.text_input('Enter Passkey:', type='password')

    if st.button('Retrieve Secret'):
        if label and passkey:
            conn = sql.connect('data.db')
            c = conn.cursor()
            try:
                c.execute("""SELECT encrypted_text, passkey FROM data WHERE label = ?""", (label,))
                result = c.fetchone()
                conn.close()

                if result:
                    encrypted_text, stored_hashed_key = result
                    if hash_key(passkey) == stored_hashed_key:
                        decrypted = decrypt(encrypted_text)
                        st.success('✅ Secret Retrieved Successfully!')
                        st.code(decrypted)
                    else:
                        st.error('❌ Incorrect Passkey!')
                else:
                    st.error('❌ Secret not found!')
            except sql.IntegrityError:
                st.error('❌ Database error occurred.')
        else:
            st.warning('⚠️ Please fill all the fields!')


elif choice == 'About':
    st.subheader("🔐 Secure Data Encryption App")
    st.markdown("""
        This app securely stores and retrieves secrets using:
        - Fernet symmetric encryption (AES 128)
        - SQLite for local data storage
        - SHA256 hashing for passkey verification
        
        Developed by Wahaj Ali 🧠
    """)
