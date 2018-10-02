sudo yum -y update
sudo yum -y install git python36 python-pip
git clone https://github.com/tbriot/petstore-api.git
python3 -m pip install -r ./petstore-api/requirements.txt --user
python3 ./petstore-api/petstore_api.py
