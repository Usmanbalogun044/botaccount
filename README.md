
# BotAccount 🛡️

**BotAccount** is a Python-based automation tool designed for ethical hacking training and penetration testing labs. Its core purpose is to simulate large-scale account creation and stress-test SMTP-based signup endpoints — helping developers and security professionals uncover potential abuse vectors in their systems.

> ⚠️ **For Educational and Authorized Security Testing Only.**

---

## 🚀 Features

- Generates random names, emails, and passwords using **Faker**
- Handles CSRF tokens automatically
- Multithreaded for faster account creation
- Logs results (success, failure, error) to `created_accounts.csv`
- Colored terminal output for status messages

---

## 📦 Requirements

- Python 3.11+
- See [requirements.txt](requirements.txt) for dependencies:
  - `requests`
  - `beautifulsoup4`
  - `faker`
  - `colorama`

---

## 🔧 Installation

```bash
git clone https://github.com/Usmanbalogun044/botaccount.git
cd botaccount
pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python bot.py --target https://example.com/signup --smtp smtp.example.com --threads 50
```

### Optional Flags

| Flag        | Description                           |
| ----------- | ------------------------------------- |
| `--proxy`   | Rotate proxies for requests           |
| `--delay`   | Delay between each request            |
| `--threads` | Number of concurrent account requests |
| `--payload` | Custom email or data payload          |

---

## 📚 Use Cases

- CEH training labs
- Red team simulations
- Anti-bot stress testing
- Secure development lifecycle validation

---

## 🧠 Ethical Notice

This tool is intended for **educational use**, **authorized testing**, and **responsible disclosure** scenarios only.

> **Do not use** this script on systems or networks without **explicit written permission**. Misuse can be illegal.

---

## 🛠 Roadmap

- [ ] CAPTCHA bypass integration (with user-supplied solver)
- [ ] UI for live simulation visualization
- [ ] Add proxy rotation and IP throttling logic
- [ ] Module for testing other spam vectors (SMS, push notifications)

---

## 🤝 Contribution

Pull requests are welcome. Please open an issue first to discuss major changes or feature suggestions.

---

## 📄 License

MIT License – Use responsibly. See [`LICENSE`](LICENSE) file for details.

---

## 📬 Author

**Usman Balogun**  
[GitHub](https://github.com/Usmanbalogun044)
