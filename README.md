# 🗑️ python-filetime-del

A simple Python script to delete files older than a specified number of days across multiple directories.

---

## 📄 Description

This script reads a list of directories and age limits from a configuration file (`config.txt`) and deletes files older than the specified number of days.

---

## ⚙️ How to Use

1. Clone this repository or download the script.
2. Open the `config.txt` file.
3. Add one line per directory in the following format:

```
C:/Users/yoshi -3
```

This will delete all files in `C:/Users/yoshi` that are older than **3 days**.

> ⚠️ **IMPORTANT:**  
> Use `/` or double backslashes (`\\`) in file paths.  
> A single backslash (`\`) will cause an error.

---

## ✅ Example Config

```
D:/Downloads -7
C:/Temp -2
E:/Logs -30
```

Each line defines:
- A folder path
- A negative number of days (e.g. `-7`)  
Files older than the given number of days will be deleted.

---

## ▶️ Running the Script

Make sure you have Python installed. Then run:

```bash
python main.py
```

Or if using `python3`:

```bash
python3 main.py
```

---

## 📦 Requirements

- Python 3.x  
No external dependencies required.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
