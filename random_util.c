
#include <time.h>
#include <stdlib.h>

int get_random(){
    srand(time(NULL));
    return rand();
}