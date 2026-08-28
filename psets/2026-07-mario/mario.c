#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        // 空格
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        // 左金字塔
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }
        // 中间空格
        printf("  ");
        // 右金字塔
        for (int l = 0; l < i + 1; l++)
        {
            printf("#");
        }
        // 换行
        printf("\n");
    }
}
