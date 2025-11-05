<p align="center">
    <img align="center" width="300" src="https://github.com/user-attachments/assets/4e40fe85-d745-4827-bfd6-97a981cdd78e" />
    <h3 align="center"></h3>
  </p>
  
<p align="center">
  <a href="https://pypi.org/project/ByMail/">
    <img src="https://img.shields.io/pypi/v/ByMail.svg?logo=python&logoColor=%23959DA5&label=pypi&labelColor=%23282f37">
  </a>
  
  <a href="https://t.me/PyCodz">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue.svg?logo=telegram">
  </a>
    
  <a href="https://t.me/DevGit" target="_blank">
    <img alt="Telegram-Discuss" src="https://img.shields.io/badge/Telegram-Discuss-blue.svg?logo=telegram" />
  </a>
</p>

<p align="center">

  <a href="https://pepy.tech/projects/ByMail/">
    <img src="https://static.pepy.tech/badge/ByMail">
  </a>

  <a href="https://github.com/DevZ44d/ByMail?tab=MIT-1-ov-file">
    <img src="https://camo.githubusercontent.com/30aa09995ff273a3a2a8abf7c116c6fadfb4737b6aac74fe8dcb03e93d855fef/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f7a3434642f79746d757369632d626f74">
  </a>
</p>




>📬 **ByMail** is a lightweight Python library to fetch inbox messages from temporary email providers. It validates domains and supports both one-shot and continuous (looping) fetching.

### 🚀 Features

- *Multiple domains:* Works with a curated set of temp-mail domains.

- *Simple API:* Pass a full email string (e.g., `name@mailto.plus`).

- *Looping mode:* Print incoming emails continuously (`Loop=True`).

- *One-shot mode:* Get a list of emails to iterate yourself (`Loop=False`).

- *Send emails:* Use `SendMail` to send messages via the tempmail.plus API.

- *Flexible imports:* `from ByMail import SendMail` or `from ByMail.send import SendMail`.

- *Status & response:* `SendMail.status()` to check success; `.response()` for raw response.


### ⚙️ Installation
```shell
pip install ByMail -U
```

### 🧠 Usage Example
```python
from ByMail import Mail, SendMail

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

### ✉️ Send email example
```python
from ByMail import SendMail
def main():
  mail = SendMail(
    from_="your-user@merepost.com",
    to="to-user@fexpost.com",
    subject="Hello from ByMail",
    text="<b>Hi!</b> This is a test.",   # default content_type is "text/html"
    # content_type="text/plain",        # optionally switch to plain text
  )
  
  print(mail.status())   # True if sent successfully
# Inspect raw response if needed:
# print(mail.response().status_code, mail.response().text)

if __name__ == '__main__':
  main()
```

### 📦 Version

- **v3.0.0** – Full email API, domain validation, loop/non-loop modes, SendMail

### 💬 Help & Support .
- Follow updates via the **[Telegram Channel](https://t.me/Pycodz)**.
- For general questions and help, join our **[Telegram chat](https://t.me/PyChTz)**.
