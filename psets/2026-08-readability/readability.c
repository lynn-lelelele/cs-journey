#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    string s = get_string("Text: ");

    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(s); i++)
    {
        if (isalpha(s[i]))
        {
            letters++;
        }
        if (s[i] == ' ')
        {
            words++;
        }
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            sentences++;
        }
    }

    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }

    return 0;
}
