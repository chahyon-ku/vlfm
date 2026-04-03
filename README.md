# vlfm

## environment setup
```bash
git submodule update --init --recursive
# mamba (for compiling habitat and grounding dino)
mamba create -f env-cu128.yaml
mamba activate cu128
# uv
uv venv --python 3.11
uv pip install -r torch.txt
uv pip install --no-build-isolation -r requirements.txt
. .venv/bin/activate
# habitat
cd third_party/habitat-sim
rm -rf build
python setup.py install --with-bullet --headless
cd -

# run after downloading data
python scripts/01_eval.py  # habitat broken
```

## download data
```bash
## hm3d
python -m habitat_sim.utils.datasets_download \
  --username $MATTERPORT_TOKEN_ID \
  --password $MATTERPORT_TOKEN_SECRET \
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
```