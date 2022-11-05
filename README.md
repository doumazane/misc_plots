## Gallery

(in progress)

![parametric](output/parametric_equations.svg)

![parametric](output/1d_2d_3d_arrays.svg)

![parametric](output/4d_array.gif)

![parametric](output/3D_terrain.gif)

![parametric](output/Integral.gif)

![PCA](https://user-images.githubusercontent.com/74925515/200110693-20b7f01c-bb3e-4001-a699-c2344eb6199d.png)

![UMAP](https://github.com/doumazane/doumazane/blob/main/umapTopics.gif)

Tips:
- generate 
- generate `GIF` with `PIL` 
- convert screencast movie into `GIF` with `ffmpeg` ([source and explanations](https://superuser.com/a/1502163)) 
```bash
~/programs/ffmpeg -i Integral.mov -filter_complex "[0:v] fps=12,scale=1000:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse" Integral.gif
```
