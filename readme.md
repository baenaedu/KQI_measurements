# KQI measurements
For FTP

Just run python file ftpKQI.py and it will save a json file with the result.
The configuration is made in hardcoded way


For Video

Before running KQI Video Measurement code please install the following:

apt-get update -q

apt-get install -q -y dstat

export DEBIAN_FRONTEND=noninteractive

apt-get install -q -y pciutils

apt-get update -q

apt-get install -y libblas-dev liblapack-dev liblapacke-dev gfortran

apt-get install -y python-pip

pip install numpy

pip install psutil

pip install selenium


Then

COPY files/* to a folder named /opt/monroe/

COPY yomo_config to a /monroe/config file


Then execute opt/monroe/setup.sh
