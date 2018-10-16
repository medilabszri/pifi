cat > /etc/apt/sources.list <<EOF
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ jessie main contrib non-free rpi
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ jessie main contrib non-free rpi
EOF

cat > /etc/apt/sources.list.d/raspi.list <<EOF
deb http://mirror.tuna.tsinghua.edu.cn/raspberrypi/ jessie main ui
deb-src http://mirror.tuna.tsinghua.edu.cn/raspberrypi/ jessie main ui
EOF

apt-get update
