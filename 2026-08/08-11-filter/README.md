# Filter · PSet 4 学习笔记 · 2026.08.11-14

CS50 Problem Set 4：图片滤镜。输入 BMP 图片，输出处理后的图片。

## 运行方式

```
./filter -g 原图.bmp 输出.bmp   # 黑白
./filter -s 原图.bmp 输出.bmp   # 复古
./filter -r 原图.bmp 输出.bmp   # 翻转
./filter -b 原图.bmp 输出.bmp   # 模糊
```

## 核心知识

- 图片 = 二维数组 `image[height][width]`，每个元素是 `RGBTRIPLE`（红绿蓝）
- `image[i][j].rgbtRed` 访问第 i 行 j 列像素的红色值
- 只需写 helpers.c 里 4 个函数，其他文件（filter.c/bmp.h/helpers.h/Makefile）是题目给的

## 1️⃣ Grayscale 黑白

思路：红绿蓝取平均值，三个值都设为平均值。

```c
for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width; j++)
    {
        int avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;
        image[i][j].rgbtRed = avg;
        image[i][j].rgbtGreen = avg;
        image[i][j].rgbtBlue = avg;
    }
}
```

## 2️⃣ Sepia 复古

思路：按公式重新算 RGB，结果四舍五入，不能超过 255。

```c
int r = image[i][j].rgbtRed;
int g = image[i][j].rgbtGreen;
int b = image[i][j].rgbtBlue;

int sr = round(0.393 * r + 0.769 * g + 0.189 * b);
int sg = round(0.349 * r + 0.686 * g + 0.168 * b);
int sb = round(0.272 * r + 0.534 * g + 0.131 * b);

image[i][j].rgbtRed   = fmin(255, sr);   // 不能超过 255
image[i][j].rgbtGreen = fmin(255, sg);
image[i][j].rgbtBlue  = fmin(255, sb);
```

`fmin(a,b)` = 返回较小的那个（压住上限）。

## 3️⃣ Reflect 翻转

思路：每行左右对调，用临时变量交换。

```c
for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width / 2; j++)   // 只走左半边
    {
        RGBTRIPLE tmp = image[i][j];               // 左边存起来
        image[i][j] = image[i][width - 1 - j];     // 右边搬过来
        image[i][width - 1 - j] = tmp;             // 左边放右边
    }
}
```

- 数组最后一个 = 长度 - 1（索引从 0 开始）
- 交换三步曲：存 → 搬 → 放

## 4️⃣ Blur 模糊 ⭐ 最难

思路：每个像素 = 自己和周围邻居（3×3 区域）的平均值。必须**先复制原图**，不能边算边改。

```c
// 第1步：复制原图（底片）
RGBTRIPLE copy[height][width];
for (int i = 0; i < height; i++)
    for (int j = 0; j < width; j++)
        copy[i][j] = image[i][j];

// 第2-4步：遍历像素，算周围平均
for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width; j++)
    {
        int totalR = 0, totalG = 0, totalB = 0, count = 0;

        for (int di = -1; di <= 1; di++)      // 行偏移
        {
            for (int dj = -1; dj <= 1; dj++)  // 列偏移
            {
                int ni = i + di;              // 邻居行号
                int nj = j + dj;              // 邻居列号

                // 边界检查：邻居必须在图片内
                if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                {
                    totalR += copy[ni][nj].rgbtRed;
                    totalG += copy[ni][nj].rgbtGreen;
                    totalB += copy[ni][nj].rgbtBlue;
                    count++;                  // 数合法邻居个数
                }
            }
        }

        image[i][j].rgbtRed   = round((float) totalR / count);
        image[i][j].rgbtGreen = round((float) totalG / count);
        image[i][j].rgbtBlue  = round((float) totalB / count);
    }
}
```

## 踩过的坑 / 知识点

- 文件名 helper.c → 应该是 helpers.c（少了 s 编译报错）
- 角落像素的邻居 = 自己 + 3 个 = 4 个（自己也算）
- 数组索引从 0 开始，最后一个是 长度-1
- `ni >= 0` 允许 0，因为 0 是第一行；负数才是越界
- 三目运算符 `(x > 255) ? 255 : x` 和 `fmin(255, x)` 效果一样

## 状态

- [x] 思路学习（代码看得懂）
- [ ] cs50.dev 编译 + check50 验证（待网好）
