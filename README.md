# WebSocket Service Project

## Overview

This project is a WebSocket service that supports both HTTP and HTTPS protocols, enabling real-time communication between clients and servers. The service is highly configurable via a JSON file or a graphical user interface (GUI). It includes security controls to prevent server overload and unauthorized access. The project also provides testing scripts and a demo web client to verify functionality.

## Features

- **WebSocket Support**: Operates over both HTTP and HTTPS.
- **Configurable Service**: Adjust settings through a JSON file or GUI.
- **Real-Time Messaging**: Facilitates instant message delivery to connected clients.
- **Database Logging**: Records messages and sender information using SQLite.
- **Security Controls**:
  - **Connection Limiting**: Restrict the maximum number of connections per IP address.
  - **API Key Authentication**: Secure message sending with API key verification.
  - **Detailed Logging**: Outputs connection IDs, IP addresses, and real-time user counts.
- **Admin GUI**: Provides a GUI for administrative tasks and configuration.
- **Cross-Platform Packaging**: Use PyInstaller to create executables for Windows and Unix-like systems.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
  - [Service Configuration](#service-configuration)
  - [Security Settings](#security-settings)
  - [GUI Configuration](#gui-configuration)
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
gevent>=21.1.2
```

### Additional Dependencies

- **SQLite3**: Comes bundled with Python; no separate installation needed.
- **PyInstaller**: For packaging the application (optional for development).

## Configuration

### Service Configuration

The service can be configured using the `socket_config.json` file located in the `config/` directory.

#### Configuration File: `/config/socket_config.json`

```json
{
  "http": "http",
  "socketport": "5000",
  "certpath": "",
  "keypath": ""
}
```

##### Configuration Options

- **http**: Set to `"http"` for HTTP connections or `"https"` for HTTPS connections.
- **socketport**: The port number on which the WebSocket service will run. Ensure this port is not occupied by another service. Default is `"5000"`.
- **certpath** and **keypath**: _(Mandatory if using HTTPS)_ Provide the absolute paths to your SSL certificate and key files.

##### Example for HTTPS Configuration

```json
{
  "http": "https",
  "socketport": "5000",
  "certpath": "/absolute/path/to/your/certificate.crt",
  "keypath": "/absolute/path/to/your/private.key"
}
```

### Security Settings

Both `zhuliu.py` and `pure_zhuliu.py` include security controls to enhance the robustness and safety of the WebSocket service.

#### Maximum Connections per IP

- **Variable:** `MAX_CONNECTIONS_PER_IP`
- **Location:** Top of `zhuliu.py` and `pure_zhuliu.py`
- **Purpose:** Restricts the maximum number of connections allowed per IP address to prevent server overload.
- **Default Value:** `2000`

**Adjusting the Limit:**

You can modify the `MAX_CONNECTIONS_PER_IP` variable to limit the number of simultaneous connections from a single IP address.

```python
MAX_CONNECTIONS_PER_IP = 100  # Example: Limit to 100 connections per IP
```

#### API Key Authentication

- **Variable:** `API_KEY`
- **Location:** Top of `zhuliu.py` and `pure_zhuliu.py`
- **Purpose:** Secures message sending by requiring an API key for authentication.
- **Default Placeholder:** `'your_encrypt_key_here'`

**Setting Your API Key:**

Replace the placeholder with your actual API key. Ensure that the sender uses the same API key to encrypt messages. Unauthorized messages without the correct API key will be rejected, preventing unauthorized access.

```python
API_KEY = 'your_actual_api_key_here'  # Replace with your actual API key
```

#### Detailed Logging

The backend logs detailed information about client connections:

- **Connection Events:**
  - **Connection Established:**
    - Outputs the client's session ID (`request.sid`), IP address (`client_ip`), and total connections from that IP.
  - **Connection Terminated:**
    - Logs when a client disconnects, along with the remaining connections from that IP.
- **Real-Time User Count:**
  - Keeps track of connected clients and updates counts in real-time.

**Example Log Output:**

```
Client connected: Session ID: abc123, IP: 192.168.1.10 (Total: 1)
Client disconnected: Session ID: abc123, IP: 192.168.1.10 (Remaining: 0)
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

---

**Key Points:**

- **Connection Limiting:**

  - Uses the `connections` dictionary to track the number of connections per IP.
  - Disconnects clients exceeding `MAX_CONNECTIONS_PER_IP`.

- **API Key Verification:**

  - Checks the `X-API-KEY` header in incoming POST requests.
  - Rejects requests with incorrect or missing API keys.

- **Logging:**
  - Prints connection and disconnection events with session IDs and IP addresses.
  - Helps monitor real-time user activity and detect potential issues.

---

**Security Recommendations:**

- **Keep Your API Key Secure:**

  - Do not share your actual API key publicly.
  - Consider storing it securely using environment variables or a secure vault.

- **Adjust `MAX_CONNECTIONS_PER_IP` Appropriately:**

  - Set a reasonable limit based on expected traffic to prevent denial-of-service attacks.

- **Monitor Logs Regularly:**
  - Keep an eye on the logs to detect unusual activity or potential security threats.

---

By incorporating these security measures, the WebSocket service becomes more robust and secure against common threats, such as unauthorized access and server overload.
