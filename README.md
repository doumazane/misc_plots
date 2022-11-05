## Gallery

![parametric](output/parametric_equations.svg)

![parametric](output/1d_2d_3d_arrays.svg)

![parametric](output/4d_array.gif)

![parametric](output/3D_terrain.gif)

![parametric](output/Integral.gif)

Tips:
- generate `GIF` with `PIL` 
- convert screencast movie into `GIF` with `ffmpeg` ([source and explanations](https://superuser.com/a/1502163)) 
```bash
~/programs/ffmpeg -i Integral.mov -filter_complex "[0:v] fps=12,scale=1000:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse" Integral.gif
```
