# WebSocket Service Project

## Overview

This project is a WebSocket service that supports both HTTP and HTTPS protocols, enabling real-time communication between clients and servers. The service is highly configurable via a JSON file or a graphical user interface (GUI). It also includes testing scripts and a demo web client to verify functionality.

## Features

- **WebSocket Support**: Operates over both HTTP and HTTPS.
- **Configurable Service**: Adjust settings through a JSON file or GUI.
- **Real-Time Messaging**: Facilitates instant message delivery to connected clients.
- **Database Logging**: Records messages and sender information using SQLite.
- **Admin GUI**: Provides a GUI for administrative tasks and configuration.
- **Cross-Platform Packaging**: Use PyInstaller to create executables for Windows and Unix-like systems.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Admin GUI Design](#admin-gui-design)
- [Packaging the Application](#packaging-the-application)
- [License](#license)

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Virtual Environment**: Recommended to use a virtual environment to manage dependencies.

### Required Python Packages

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**

```
Flask>=2.0.1
Flask-SocketIO>=5.1.0
Flask-Cors>=3.0.10
PyQt5>=5.15.4
eventlet>=0.31.0
requests>=2.25.1
```

### Additional Dependencies

- **SQLite3**: Comes bundled with Python; no separate installation needed.
- **PyInstaller**: For packaging the application (optional for development).

## Configuration

The service can be configured using the `socket_config.json` file located in the `config/` directory.

### Configuration File: `/config/socket_config.json`

```json
{
  "http": "http",
  "socketport": "5000",
  "certpath": "",
  "keypath": ""
}
```

#### Configuration Options

- **http**: Set to `"http"` for HTTP connections or `"https"` for HTTPS connections.
- **socketport**: The port number on which the WebSocket service will run. Ensure this port is not occupied by another service. Default is `"5000"`.
- **certpath** and **keypath**: (Mandatory if using HTTPS) Provide the absolute paths to your SSL certificate and key files.

#### Example for HTTPS Configuration

```json
{
  "http": "https",
  "socketport": "5000",
  "certpath": "/absolute/path/to/your/certificate.crt",
  "keypath": "/absolute/path/to/your/private.key"
}
```

### GUI Configuration

Alternatively, use the graphical user interface to configure the service:

- Run the GUI script:

  ```bash
  python /project_files/zhuliu.py
  ```

- After making changes, **restart the program** to apply new settings.

## Running the Application

### Starting the WebSocket Service

Choose one of the following scripts to start the service:

- **With GUI Configuration:**

  ```bash
  python /project_files/zhuliu.py
  ```

- **Without GUI (Pure Python Script):**

  ```bash
  python /project_files/pure_zhuliu.py
  ```

**Note:** The script `/project_files/admin_gui.py` is only for UI demonstration and does not start the WebSocket service.

### Icon Configuration

- **Icon File:** Customize the application's icon by replacing `favicon.ico` located in the `img/` directory.

## Testing

**Important:** Follow these steps to test the WebSocket service functionality.

### 1. Start the WebSocket Service

Run either of the scripts:

- With GUI:

  ```bash
  python /project_files/zhuliu.py
  ```

- Without GUI:

  ```bash
  python /project_files/pure_zhuliu.py
  ```

### 2. Run the Web Client

- Open `index.html` located in the `/ui/` directory in your web browser.

  ```bash
  # Example for opening in default browser
  open /ui/index.html          # macOS
  xdg-open /ui/index.html      # Linux
  start /ui/index.html         # Windows
  ```

- This web page attempts to connect to the WebSocket service and receive messages.

### 3. Verify Connection

- Open the browser's developer console:

  - **Windows/Linux:** Press `Ctrl + Shift + I`
  - **macOS:** Press `Command + Option + I`

- Navigate to the **Console** tab to check if the connection to the service is successful.

### 4. Send a Test Message

- Run the `server2.py` script located in the `test1/` directory:

  ```bash
  python /test1/server2.py
  ```

- **Outcome:**

  - A message should spontaneously appear on the bottom right corner of the `index.html` web page.
  - The content of the message can be modified by editing `server2.py`.

### 5. Verify Database Logging

- The `server2.py` script logs the message, sender, and timestamp to a SQLite database in the `test1/` directory.
- Use the provided SQL script in the same directory to view logs:

  ```bash
  sqlite3 test_database.db
  sqlite> SELECT * FROM messages;
  ```

## Admin GUI Design

The administrative GUI is built using PyQt5 and designed with Qt Designer.

### Workflow

1. **Design Interface with Qt Designer:**

   - Create the GUI layout and save it as a `.ui` file.

2. **Convert `.ui` to Python Code:**

   - Use `pyuic5` to convert the `.ui` file to a Python module:

     ```bash
     pyuic5 -o pyqt_ui2.py pyqt_ui2.ui
     ```

3. **Integrate with `admin_gui.py`:**

   - The generated `pyqt_ui2.py` serves as a framework for `admin_gui.py`.

**Note:** `admin_gui.py` is for UI demonstration purposes and does not start the WebSocket service.

## Packaging the Application

Use PyInstaller to package the application into executables for distribution.

### Steps

1. **Install PyInstaller:**

   ```bash
   pip install pyinstaller
   ```

2. **Package the Application:**

   - **For Windows:**

     ```bash
     pyinstaller --onefile --windowed /project_files/zhuliu.py
     ```

   - **For Unix-like Systems:**

     ```bash
     pyinstaller --onefile /project_files/zhuliu.py
     ```

   - **Options Explained:**

     - `--onefile`: Packages the application into a single executable.
     - `--windowed`: (Windows only) Hides the console window when running the GUI application.

3. **Find the Executable:**

   - The packaged executable will be located in the `dist/` directory.

### Notes

- **Dependencies:** Ensure all required packages are included.
- **Testing:** Test the executable on the target platform to verify functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** Replace placeholder paths and adjust commands as necessary based on your environment and operating system. Ensure you have the appropriate permissions and have secured your SSL certificates when configuring HTTPS.

**Contact:** For questions or contributions, please open an issue or submit a pull request on the project's repository.
