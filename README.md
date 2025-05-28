🔐 Secure Data Encryption App
A simple yet powerful Streamlit-based application to securely store and retrieve sensitive information using Fernet symmetric encryption (AES 128) and passkey hashing via SHA256. Built with Python and SQLite, this app is ideal for managing personal secrets like passwords, notes, or confidential data locally.

🚀 Features
🔐 Encrypt & Save sensitive text data locally

🔓 Retrieve secrets using a hashed passkey

🔑 Fernet encryption (AES 128-bit) ensures end-to-end security

🧠 Passkey hashed using SHA256 for integrity

💾 SQLite backend – simple, fast, and offline

🧩 Clean, minimal Streamlit UI

📦 Tech Stack
Python 3.12

Streamlit

SQLite3

Cryptography (Fernet)

hashlib (SHA256)

📸 App UI
Store Secret	Retrieve Secret

⚙️ How to Run Locally
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/secure-data-encryption.git
cd secure-data-encryption

# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py

💡 Use Cases
Store personal notes or passwords securely

Share secrets with a passkey over a secure channel

Build a proof-of-concept for local encrypted data storage

🧑‍💻 Author
Made with ❤️ by Wahaj Ali
