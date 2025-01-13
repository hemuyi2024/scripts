from osgeo import gdal

def resize_tif(input_tif, output_tif, scale_factor):
    """
    将输入 TIFF 文件按比例缩放，并保存为新文件。

    参数:
    - input_tif: 输入 TIFF 文件路径。
    - output_tif: 输出 TIFF 文件路径。
    - scale_factor: 缩放比例（例如 0.1 表示缩小为原来的 10%）。
    """
    # 打开输入 TIFF 文件
    src_dataset = gdal.Open(input_tif, gdal.GA_ReadOnly)
    if src_dataset is None:
        print("无法打开输入 TIFF 文件。")
        return

    # 获取输入图像尺寸
    width = src_dataset.RasterXSize
    height = src_dataset.RasterYSize
    print(f"原始尺寸: 宽度={width}, 高度={height}")

    # 计算目标尺寸
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    print(f"目标尺寸: 宽度={new_width}, 高度={new_height}")

    # 创建输出数据集
    driver = gdal.GetDriverByName("GTiff")
    output_dataset = driver.Create(output_tif, new_width, new_height, src_dataset.RasterCount, gdal.GDT_Byte)
    if output_dataset is None:
        print("无法创建输出数据集。")
        return

    # 设置地理变换（缩放后更新像素大小）
    geotransform = src_dataset.GetGeoTransform()
    new_geotransform = (
        geotransform[0],  # 左上角 x 坐标
        geotransform[1] * (width / new_width),  # 新像素宽度
        geotransform[2],  # 旋转参数（保持不变）
        geotransform[3],  # 左上角 y 坐标
        geotransform[4],  # 旋转参数（保持不变）
        geotransform[5] * (height / new_height)  # 新像素高度
    )
    output_dataset.SetGeoTransform(new_geotransform)

    # 设置投影信息
    projection = src_dataset.GetProjection()
    output_dataset.SetProjection(projection)

    # 逐波段处理
    for band_idx in range(1, src_dataset.RasterCount + 1):
        input_band = src_dataset.GetRasterBand(band_idx)
        output_band = output_dataset.GetRasterBand(band_idx)

        # 使用 GDAL Warp API 缩放波段
        gdal.ReprojectImage(
            src_dataset, output_dataset,
            src_dataset.GetProjection(), output_dataset.GetProjection(),
            gdal.GRA_Bilinear  # 双线性插值
        )

    # 关闭数据集
    output_dataset.FlushCache()
    output_dataset = None
    src_dataset = None
    print(f"TIFF 文件已成功缩放并保存到: {output_tif}")

if __name__ == '__main__':
    input_tif = "/home/lty/data/SEU/seu_0103_cut_fix.tif"
    output_tif = "/home/lty/data/SEU/seu_resized/seu_resized_m300.tif"
    scale_x = 0.2
    scale_y = 0.5
    resize_tif(input_tif, output_tif, scale_x)
