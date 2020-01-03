import ssim.ssimlib as pyssim

img1='images/breast_img1.png'
img2='images/breast_img3.png'
cw_ssim_value=pyssim.SSIM(img1).cw_ssim_value(img2)
print(cw_ssim_value)
