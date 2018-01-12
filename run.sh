cd vgg16/tensorflow-vgg16/
make

ipython converter.py
cd ../

cd caltech-dataset/
bash download_parse.sh
ipython3 caltech.py

cd ../
ipython region_proposal.py
