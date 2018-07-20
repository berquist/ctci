#include <assert.h>
#include <stddef.h> /* size_t */
#include <stdlib.h> /* malloc/calloc, free */
#include <stdio.h> /* printf */

/* Write a method to print the last K lines of an input file using
 * C.
 */
int ch12_1(size_t k) {
    int ret;
    const char filename[] = "CMakeCache.txt";
    /* printf("filename: %s\n", filename); */
    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
        perror("Error opening file");
    size_t counter = 0;
    char buf[BUFSIZ];
    /* Count the number of lines in the file. */
    while (fgets(buf, BUFSIZ, fp) != NULL) {
        counter++;
    }
    rewind(fp);
    assert(k < counter);
    const size_t diff = counter - k;
    for (size_t i = 0; i < diff; i++) {
        fgets(buf, BUFSIZ, fp);
    }
    while (fgets(buf, BUFSIZ, fp) != NULL) {
        ret = puts(buf);
    }
    ret = fclose(fp);
    return ret;
}

/* Write an aligned malloc and free function that supports allocating
 * memory such that the memory address returned is divisible by a
 * specific power of two.
 *
 * EXAMPLE
 *
 * =align_malloc(1000, 128)= will return a memory address that is a
 * multiple of 128 and that points to a memory of size 1000 bytes.
 *
 * =aligned_free()= will free the memory allocated by =align_malloc=.
 */
void ch12_10() {
}

/* Write a function C called =my2DAlloc= which allocates a
 * two-dimentional array. Minimize the number of calls to malloc and
 * make sure that the memory is accessible by the notation
 * =arr[i][j]=.
 */
void ch12_11(size_t nr, size_t nc) {
    const size_t nelem = nr * nc;
    /* The trick is that we allocate memory for pointers to 1D
     * arrays. See
     * https://stackoverflow.com/questions/13105056/allocate-contiguous-memory. */
    double (*arr)[nc] = calloc(nr, sizeof(*arr));
    if (arr != NULL) {
        /* initialize */
        for (size_t i = 0; i < nr; i++) {
            for (size_t j = 0; j < nc; j++) {
                size_t idx = (i * nc) + j;
                arr[i][j] = idx;
            }
        }
        /* print */
        for (size_t i = 0; i < nr; i++) {
            for (size_t j = 0; j < nc; j++) {
                size_t idx = (i * nc) + j;
                /* printf("arr[%d][%d] = %lf\n", i, j, arr[i][j]); */
            }
        }
        free(arr);
    }
}

int main(int argc, char **argv) {
    const size_t k = 20;
    ch12_1(k);
    ch12_10();
    const size_t nr = 5;
    const size_t nc = 3;
    ch12_11(nr, nc);
    return 0;
}
