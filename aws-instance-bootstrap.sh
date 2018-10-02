sudo yum -y update
sudo yum -y install git python36 python-pip
sudo git clone https://github.com/tbriot/petstore-api.git
sudo pip install -r ./petstore-api/requirements.txt
python3 ./petstore-api/petstore_api.py
