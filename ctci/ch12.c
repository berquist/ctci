#include <stddef.h> /* size_t */
#include <stdlib.h> /* malloc, free */
#include <stdio.h> /* printf */

/* Write a function C called =my2DAlloc= which allocates a
 * two-dimentional array. Minimize the number of calls to malloc and
 * make sure that the memory is accessible by the notation
 * =arr[i][j]=.
 */
void ch12_11(size_t nr, size_t nc) {
    const size_t nelem = nr * nc;
    double * arr = malloc(nelem * sizeof(size_t));
    if (arr != NULL) {
        /* initialize */
        for (size_t i = 0; i < nr; i++) {
            for (size_t j = 0; j < nc; j++) {
                size_t idx = (i * nc) + j;
                arr[idx] = idx;
            }
        }
        /* print */
        for (size_t i = 0; i < nr; i++) {
            for (size_t j = 0; j < nc; j++) {
                size_t idx = (i * nc) + j;
                printf("arr[%i] = %lf\n", idx, arr[idx]);
            }
        }
        free(arr);
    }
}

int main() {
    const size_t nr = 5;
    const size_t nc = 3;
    ch12_11(nr, nc);
    return 0;
}
