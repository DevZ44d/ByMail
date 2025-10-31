<p align="center">
  <img align="center" width="300" src="https://github.com/user-attachments/assets/4e40fe85-d745-4827-bfd6-97a981cdd78e" />
  <h3 align="center"></h3>
</p>


<p align="center">

<a href="https://pypi.org/project/ByMail/">
    <img src="https://img.shields.io/pypi/v/ByMail?color=red&logo=pypi&logoColor=red">
  </a>

  <a href="https://t.me/Pycodz">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram">
  </a>
  
  <a href="https://t.me/DevZ44d" target="_blank">
    <img alt="Telegram Owner" src="https://img.shields.io/badge/Telegram-Owner-red.svg?logo=telegram" />
  </a>
</p>




>📬 **ByMail** is a lightweight Python library to fetch inbox messages from temporary email providers. It validates domains and supports both one-shot and continuous (looping) fetching.

### 🚀 Features

- *Multiple domains:* Works with a curated set of temp-mail domains.

- *Simple API:* Pass a full email string (e.g., `name@mailto.plus`).

- *Looping mode:* Print incoming emails continuously (`Loop=True`).

- *One-shot mode:* Get a list of emails to iterate yourself (`Loop=False`).


### ⚙️ Installation
```shell
pip install ByMail -U
```

### 🧠 Usage Example
```python
from ByMail import Mail

# One-shot: you iterate
m = Mail(Email="your-user@mailto.plus", Loop=False)
for mail in m.get_inboxes():
    print(mail)

# Looping: prints internally and blocks (Ctrl+C to stop)
m = Mail("your-user@mailto.plus", Loop=True)
m.get_inboxes()
# ✅ Supported Domains (
# mailto.plus, fexpost.com, fexbox.org
# mailbox.in.ua, rover.info, chitthi.in
# fextemp.com, any.pink, merepost.com
# )
```

### 📦 Version

- **v2.0.0** – Full email API, domain validation, loop/non-loop modes

> ⚠️ *Note:* Early version; improvements and more providers planned.


### 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.

