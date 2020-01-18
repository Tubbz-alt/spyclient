# Download SpyServer
wget https://airspy.com/?ddownload=4262
tar -xvzf spyserver-linux-x64.tgz.gz -C spyserver
cd spyserver
chmod +x ./spyserver
./spyserver &

# Build and install package
#pip install -r requirements.txt
make install
