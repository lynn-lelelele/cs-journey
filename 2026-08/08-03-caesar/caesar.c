#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // 第1步：检查参数个数（只要 key 一个）
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // 第2步：字符串 "3" → 数字 3
    int key = atoi(argv[1]);

    // 第3步：读明文
    string s = get_string("plaintext: ");

    // 第4步：遍历每个字符，是字母就加密
    for (int i = 0; i < strlen(s); i++)
    {
        if (isalpha(s[i]))
        {
            if (islower(s[i]))
            {
                s[i] = (s[i] - 'a' + key) % 26 + 'a';
            }
            else
            {
                s[i] = (s[i] - 'A' + key) % 26 + 'A';
            }
        }
        // 非字母（空格、数字、标点）不动
    }

    // 第5步：输出密文
    printf("ciphertext: %s\n", s);
    return 0;
}
