# Download latest SpyServer
wget https://airspy.com/downloads/spyserver-linux-x64.tgz
tar -xvzf spyserver-linux-x64.tgz -C spyserver
cd spyserver
chmod +x ./spyserver
./spyserver &

# Build and install package
#pip install -r requirements.txt
make install
