

# ## objectnav - hm3d
# wget https://dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/hm3d/v1/objectnav_hm3d_v1.zip -O objectnav_hm3d_v1.zip
# unzip objectnav_hm3d_v1.zip
# mkdir -p data/datasets/objectnav/hm3d
# mv objectnav_hm3d_v1 data/datasets/objectnav/hm3d/v1
# rm objectnav_hm3d_v1.zip
# # pointnav
# mkdir data/checkpoints
# cp data/pointnav_weights.pth data/checkpoints
# ## grounding dino
# wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth -O data/checkpoints/groundingdino_swint_ogc.pth
# ## yolov7
# wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt -O data/checkpoints/yolov7-e6e.pt
# ## mobile_sam
# gdown https://drive.google.com/uc?id=1dE-YAG-1mFCBmao2rHDp0n-PP4eH7SjE -O mobile_sam.zip
# unzip mobile_sam.zip
# mv weight data/checkpoints/mobile_sam
# rm mobile_sam.zip


def main():
    # download
    
    pass

if __name__ == "__main__":
    main()