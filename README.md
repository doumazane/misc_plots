## Gallery

(in progress)

![parametric](output/parametric_equations.svg)

![parametric](output/1d_2d_3d_arrays.svg)

![parametric](output/4d_array.gif)

![parametric](output/3D_terrain.gif)

![parametric](output/Integral.gif)

![PCA](https://user-images.githubusercontent.com/74925515/200110693-20b7f01c-bb3e-4001-a699-c2344eb6199d.png)

![UMAP](https://github.com/doumazane/doumazane/blob/main/umapTopics.gif)

💡Tips:
- generate 
- generate `GIF` with `PIL` 
- convert MOV file to a GIF filter (typically a screencast movie) 👉 [source and explanations](https://superuser.com/a/1502163)

```bash
ffmpeg -i Integral.mov -filter_complex "[0:v] fps=12,scale=1000:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse" Integral.gif
```

- resize a GIF that's too big 👉 [source and explanations](https://superuser.com/questions/1362352/how-do-i-resize-an-animated-gif-and-keep-transparency) 

```bash
~/programs/ffmpeg -hide_banner -i resampled-top-view_v01.gif -filter_complex "[0:v] scale=320:-1:flags=lanczos,split [a][b]; [a] palettegen=stats_mode=single [p]; [b][p] paletteuse=new=1" resampled-top-view_v02.gif
```
