## **RGB to TIR Image Translation Based on Generative Adversarial Network**

 - [ ] ****Introduction****
This work proposes an image generator, which generates TIR images from given RGB images by Generative Adversarial Network (GAN). The effectiveness is quantitatively and qualitatively demonstrated on classic image generation metrics and the downstream RGBT tasks-- visual object tracking with RGB and TIR modalites.
 - [ ] ****Contribution****
1. A GAN-based image generator, which generates TIR images from RGB images.
2. To generate high-quality TIR data, the perceptual loss is utilised in the training process 76
of generator for content consistency and multi-scale discriminators are employed for 77
clearer textures.
3. We demonstrate the effectiveness of this work quantitatively and qualitatively.

![pp](https://github.com/user-attachments/assets/a639ee27-0bec-42a1-819b-7939c626a3dd)


Because of the limitation of data size, the whole code can be found [here](https://pan.baidu.com/s/16tLL_LJWNFJPK8qAnE-i7g) with code:6rt8

- [ ] ****Prerequisites****
 - Linux
 - NVIDIA GPU
 - [ ] ****Create conda environment****
```bash
conda create -n rgb2tir python=3.8
conda activate rgbt2tir
```

```bash
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
pip install opencv-python pyYAML scipy matplotlib numpy pillow
conda install -y tqdm
pip install visdom tensorboradX dominate easydict cython pandas lmdb
```

 - [ ] ****Train****

```bash
python train.py --label_nc 0 --no_instance --continue_train --batchSize 64 --name RGB_T234_step5 --dataroot ./datasets/step_5_of_top100/ --loadSize 256 --fineSize 128 --netG local --n_blocks_global 3 --n_blocks_local 1 --gpu_ids 0,2
```

 - [ ] ****Test****

```bash
python test.py --label_nc 0 --no_instance --name RGB_T234_step5 --dataroot ./datasets/step_5_of_top100/ --loadSize 256 --fineSize 128 --netG local --n_blocks_global 3 --n_blocks_local 1 --gpu_ids 0,2
```

This work is now submitted to The Visual Computer

```bash
@article{rgb2tir,
  title={RGB to TIR Image Translation Based on Generative Adversarial Network},
  author={Huijie Zhu, Qingyuan Zhu, Kai Ding, Hao Tang, and, Yuchen Li},  
  journal={The Visual Computer},
  year={2025}
}
```
