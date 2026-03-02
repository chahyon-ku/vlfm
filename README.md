
``` bash
git submodule update --init --recursive
mamba create -y -f env.yaml
mamba activate vlfm

# habitat sim
cd third_party/habitat-sim
rm -rf build
python setup.py install --with-bullet --headless
cd -
echo "export MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet" > $CONDA_PREFIX/etc/conda/activate.d/quiet_habitat.sh
echo "unset MAGNUM_LOG HABITAT_SIM_LOG" > $CONDA_PREFIX/etc/conda/deactivate.d/quiet_habitat.sh

# download
## hm3d
python -m habitat_sim.utils.datasets_download \
  --username $MATTERPORT_TOKEN_ID --password $MATTERPORT_TOKEN_SECRET \
  --uids hm3d_val_v0.2 \
  --data-path data
## objectnav - hm3d
wget https://dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/hm3d/v1/objectnav_hm3d_v1.zip -O objectnav_hm3d_v1.zip
unzip objectnav_hm3d_v1.zip
mkdir -p data/datasets/objectnav/hm3d
mv objectnav_hm3d_v1 data/datasets/objectnav/hm3d/v1
rm objectnav_hm3d_v1.zip
# pointnav
mkdir data/checkpoints
cp data/pointnav_weights.pth data/checkpoints
## grounding dino
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth -O data/checkpoints/groundingdino_swint_ogc.pth
## yolov7
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt -O data/checkpoints/yolov7-e6e.pt
## mobile_sam
gdown https://drive.google.com/uc?id=1dE-YAG-1mFCBmao2rHDp0n-PP4eH7SjE -O mobile_sam.zip
unzip mobile_sam.zip
mv weight data/checkpoints/mobile_sam
rm mobile_sam.zip

# eval
python scripts/01_eval.py
python scripts/01_eval.py habitat.dataset.data_path=data/datasets/objectnav/mp3d/val/val.json.gz
```
