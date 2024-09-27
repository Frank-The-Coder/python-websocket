# 基于 CentOS 7 的镜像
FROM centos:7

# 安装必要的依赖
RUN yum install -y epel-release && \
    yum install -y python36 python36-pip gcc gcc-c++ zlib-devel python36-devel file make glibc-devel libffi-devel libev-devel libtool libtool-ltdl libtool-ltdl-devel

    sudo yum groupinstall -y "Development Tools"

    sudo yum install libffi-devel openssl-devel
    sudo pip3 install greenlet==0.4.17
    sudo yum install centos-release-scl
    sudo yum install devtoolset-8
    scl enable devtoolset-8 bash

# 安装 wheel 包
RUN pip3 install wheel

# 设置环境变量以启用 C++11 编译选项
ENV CFLAGS="-std=c++11" CXXFLAGS="-std=c++11"

# 安装项目所需的依赖项
RUN pip3 install flask flask_cors flask_socketio gevent

# 安装其他可能需要的开发库
RUN yum install -y openssl-devel bzip2-devel xz-devel

# 安装 libc6-dev 和 symlink 以确保 libdl.so.2 在正确的路径中
RUN yum install -y glibc-devel.i686 glibc.i686
RUN [ ! -e /usr/lib/libdl.so ] && ln -s /lib/libdl.so.2 /usr/lib/libdl.so || echo "libdl.so already exists"

# 复制并运行编译引导程序的脚本
COPY compile_bootloader.sh /tmp/compile_bootloader.sh
RUN sed -i 's/\r$//' /tmp/compile_bootloader.sh && chmod +x /tmp/compile_bootloader.sh && /tmp/compile_bootloader.sh

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装 PyInstaller
RUN pip3 install pyinstaller

# 打包命令
CMD ["pyinstaller", "--onefile", "--name", "service", "service.py"]
