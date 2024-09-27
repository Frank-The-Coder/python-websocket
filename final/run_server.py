import http.server
import ssl
import os

# 设置当前工作目录
web_dir = os.path.join(os.path.dirname(__file__))
os.chdir(web_dir)

# 创建服务器地址和处理程序
server_address = ('localhost', 5500)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# 配置 SSL
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='../ssl/cert.pem',  # 替换为你的证书路径
                               keyfile='../ssl/key.pem',  # 替换为你的密钥路径
                               ssl_version=ssl.PROTOCOL_TLS)

print(f"Serving on https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
