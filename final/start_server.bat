@echo off
start python https_server.py
timeout /t 3
start chrome https://localhost:5500/index2.html
