#include "stdio.h"
main(void) {
    int x;
    for(x=1;x<101;x++) {
        if (x%3==0) printf("Fizz");
        if (x%5==0) printf("Buzz");
        else if (x%3) printf("%d", x);
        printf("\n");
    }
}
