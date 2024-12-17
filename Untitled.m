img=imread('E:\python_project\pix2pixHD-master\results\RGB_T234_g2nospace\test_latest\images\00001_1_1_synthesized_image.jpg');
[height, width, channels]=size(img);
dims=ndims(img);
disp([height, width, channels]);
disp(dims);