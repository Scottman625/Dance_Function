# 專案說明 / Project Description

這是一個利用AI影像辨識套件來開發的可讓用戶上傳舞者影片並遊玩的舞姿評分遊戲。此專案結合了先進的影像識別技術，能夠分析用戶上傳的舞蹈影片，評分其舞姿表現，並提供即時反饋，讓用戶能夠提升舞蹈技巧。

This is a dance pose scoring game developed using AI image recognition packages, allowing users to upload dancer videos and play. The project integrates advanced image recognition technology to analyze uploaded dance videos, score dance performances, and provide real-time feedback, enabling users to improve their dancing skills.

- [繁體中文](#繁體中文)
- [English](#english)

## 繁體中文

歡迎使用本專案！以下是設定與運行本專案的詳細步驟。如果在過程中遇到任何問題，請參考本說明或聯繫開發者。

### 目錄
- [環境設置](#環境設置)
  - [1. 建立虛擬環境](#1-建立虛擬環境)
  - [2. 啟動虛擬環境](#2-啟動虛擬環境)
  - [3. 安裝依賴套件](#3-安裝依賴套件)
- [資料庫遷移](#資料庫遷移)
  - [4. 創建遷移文件](#4-創建遷移文件)
  - [5. 應用遷移](#5-應用遷移)
- [創建管理員帳戶](#創建管理員帳戶)
  - [6. 創建超級用戶](#6-創建超級用戶)
- [啟動開發伺服器](#啟動開發伺服器)
  - [7. 運行伺服器](#7-運行伺服器)

## 環境設置

### 1. 建立虛擬環境

首先，使用 Python 的 `venv` 模組來建立一個虛擬環境，以隔離專案的依賴包。

```bash:path/to/ReadMe.md
python -m venv venv
```

### 2. 啟動虛擬環境

在 Windows 系統上，使用以下命令啟動虛擬環境：

```bash:path/to/ReadMe.md
.\venv\Scripts\Activate
```

在啟動後，您的終端機提示符應該會顯示 `(venv)`，表示虛擬環境已啟動。

### 3. 安裝依賴套件

確保您已經準備好 `requirements.txt` 文件，該文件列出了專案所需的所有 Python 套件。使用以下命令安裝所有依賴：

```bash:path/to/ReadMe.md
pip install -r requirements.txt
```

## 資料庫遷移

### 4. 創建遷移文件

在進行資料庫操作之前，需先生成遷移文件，這些文件描述了資料庫模型的變更。

```bash:path/to/ReadMe.md
python app/manage.py makemigrations
```

### 5. 應用遷移

將遷移應用到資料庫，實際更新資料庫結構。

```bash:path/to/ReadMe.md
python app/manage.py migrate
```

## 創建管理員帳戶

### 6. 創建超級用戶

為了能夠登入 Django 的管理後台，需創建一個超級用戶。執行以下命令：

```bash:path/to/ReadMe.md
python app/manage.py createsuperuser
```

執行後，系統會提示您輸入相關資訊：

```
Username: admin
Email address: admin@example.com
Phone number: 你的電話號碼
Password: ************
Password (again): ************
```

請依照提示輸入您的使用者名稱、電子郵件、電話號碼及密碼。確保密碼安全且牢固。

## 啟動開發伺服器

### 7. 運行伺服器

完成上述步驟後，您可以啟動 Django 的開發伺服器，開始運行專案：

```bash:path/to/ReadMe.md
python app/manage.py runserver
```

啟動後，您可以打開瀏覽器，訪問 [http://127.0.0.1:8000/web/home](http://127.0.0.1:8000/web/home) 來查看您的應用程式。若要登入管理後台，請訪問 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) 並使用剛剛創建的超級用戶帳戶登入。

## 注意事項

- **虛擬環境**：請確保每次開發前都啟動虛擬環境，以避免依賴衝突。
- **敏感資訊**：不要將 `settings.py` 或其他包含敏感資訊的文件提交至版本控制系統。
- **資料庫備份**：定期備份您的資料庫，以防止意外資料丟失。
- **依賴更新**：當更新 `requirements.txt` 後，記得重新安裝依賴。

## 常見問題

### 問題：`python` 命令在 PowerShell 無法使用

請參考[這裡](#如何解決在-power-shell-中無法運行-python-命令)的解決方案。

### 問題：無法創建超級用戶

確保所有遷移已正確應用，並且資料庫連接正確配置。

## 貢獻

歡迎任何形式的貢獻！請提交 Issue 或 Pull Request 來協助改進專案。

## 授權

本專案遵循 [MIT 授權](LICENSE)。

## 聯絡方式

如有任何問題，請聯繫 [your.email@example.com](mailto:your.email@example.com)。

---

## English

Welcome to this project! Below are the detailed steps to set up and run this project. If you encounter any issues during the process, please refer to this documentation or contact the developer.

### Table of Contents
- [Setup](#setup)
  - [1. Create Virtual Environment](#1-create-virtual-environment)
  - [2. Activate Virtual Environment](#2-activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
- [Database Migration](#database-migration)
  - [4. Create Migration Files](#4-create-migration-files)
  - [5. Apply Migrations](#5-apply-migrations)
- [Create Admin Account](#create-admin-account)
  - [6. Create Superuser](#6-create-superuser)
- [Start Development Server](#start-development-server)
  - [7. Run Server](#7-run-server)

## Setup

### 1. Create Virtual Environment

First, use Python's `venv` module to create a virtual environment to isolate the project's dependencies.

```bash:path/to/ReadMe.md
python -m venv venv
```

### 2. Activate Virtual Environment

On Windows, use the following command to activate the virtual environment:

```bash:path/to/ReadMe.md
.\venv\Scripts\Activate
```

After activation, your terminal prompt should display `(venv)`, indicating that the virtual environment is active.

### 3. Install Dependencies

Ensure you have the `requirements.txt` file ready, which lists all the Python packages required for the project. Install all dependencies using the following command:

```bash:path/to/ReadMe.md
pip install -r requirements.txt
```

## Database Migration

### 4. Create Migration Files

Before performing any database operations, generate migration files that describe the changes to the database models.

```bash:path/to/ReadMe.md
python app/manage.py makemigrations
```

### 5. Apply Migrations

Apply the migrations to the database to update the database structure.

```bash:path/to/ReadMe.md
python app/manage.py migrate
```

## Create Admin Account

### 6. Create Superuser

To log in to Django's admin backend, you need to create a superuser. Execute the following command:

```bash:path/to/ReadMe.md
python app/manage.py createsuperuser
```

After running the command, the system will prompt you to enter the following information:

```
Username: admin
Email address: admin@example.com
Phone number: Your phone number
Password: ************
Password (again): ************
```

Please follow the prompts to enter your username, email, phone number, and password. Ensure that your password is secure and strong.

## Start Development Server

### 7. Run Server

After completing the above steps, you can start Django's development server to run the project:

```bash:path/to/ReadMe.md
python app/manage.py runserver
```

Once the server is running, you can open your browser and visit [http://127.0.0.1:8000/web/home](http://127.0.0.1:8000/web/home) to view your application. To access the admin backend, visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the superuser account you just created.

## Important Notes

- **Virtual Environment**: Ensure you activate the virtual environment before each development session to avoid dependency conflicts.
- **Sensitive Information**: Do not commit `settings.py` or any other files containing sensitive information to version control systems.
- **Database Backup**: Regularly back up your database to prevent accidental data loss.
- **Dependency Updates**: After updating `requirements.txt`, remember to reinstall dependencies.

## Frequently Asked Questions

### Issue: `python` command does not work in PowerShell

Please refer to [this section](#how-to-fix-python-command-not-working-in-power-shell) for solutions.

### Issue: Unable to create superuser

Ensure all migrations have been applied correctly and that the database connection is properly configured.

## Contributing

All forms of contributions are welcome! Please submit an Issue or Pull Request to help improve the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions, please contact [scottman608@gmail.com](mailto:scottman608@gmail.com).


