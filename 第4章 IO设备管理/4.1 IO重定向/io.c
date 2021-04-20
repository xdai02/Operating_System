#include <stdio.h>

int main(int argc, char *argv[]) {
    int num;
    fscanf(stdin, "%d", &num);
    fprintf(stdout, "[stdout] num = %d\n", num);
    fprintf(stderr, "[stderr] This is an error message.\n");
    return 0;
}