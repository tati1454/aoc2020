#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numberOfLines(char *fileName)
{
    FILE *fd;
    int count = 0;
    char c;

    fd = fopen(fileName, "r");

    while((c = fgetc(fd)) && c != EOF)
    {
        if(c == '\n')
        {
            count++;
        }
    }

    return count;
}

int* getPuzzleInput(char * filename, int linesCount)
{
    FILE * inputFile = fopen(filename, "r");
    if(inputFile == NULL) return 0;

    int *numbers = malloc(linesCount);
    char lineBuffer[100];
    for(int i = 0; i < linesCount; ++i)
    {
        memset(lineBuffer, 0, 100);
        fgets(lineBuffer, 100, inputFile);

        numbers[i] = atoi(lineBuffer);
    }

    return numbers;
}

void part1(int *input, int lenght)
{
    for(int i = 0; i < lenght; ++i)
    {
        int n1 = input[i];
        for(int j = 0; j < lenght; ++j)
        {
            int n2 = input[j];
            if((n1 + n2) == 2020)
            {
                printf("%d", n1 * n2);
                return;
            }
        }
    }
}

void part2(int *input)
{

}

int main()
{
    int linesCount = numberOfLines("input.txt");
    int *input = getPuzzleInput("input.txt", linesCount);

    part1(input, linesCount);

    free(input);
}