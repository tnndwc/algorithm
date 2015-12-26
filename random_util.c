

//
//随机数相关
//

#include <time.h>
#include <stdlib.h>

long get_random() {
    srand(time(NULL));
    return rand();
}

/*
long get_random_max(long max) {
    // max <= RAND_MAX < ULONG_MAX, so this is okay.
    unsigned long num_bins = (unsigned long) max + 1,
            num_rand = (unsigned long) RAND_MAX + 1,
            bin_size = num_rand / num_bins,
            defect = num_rand % num_bins;

    long x;
    do {
        x = random();

        // This is carefully written not to overflow
    } while (num_rand - defect <= (unsigned long) x);

    // Truncated division is intentional
    return x / bin_size;
}*/

long get_random_max(long max) {
    unsigned long divisor = (unsigned long) (RAND_MAX / (max + 1)), retval;

    do {
        retval = rand() / divisor;
    } while (retval > max);

    return retval;
}


//生成有边界的随机数:[min, max]
long get_random_range(long min, long max) {
    unsigned long divisor = (unsigned long) (RAND_MAX / (max - min + 1)), retval;

    do {
        retval = rand() / divisor;
        retval += min;
    } while (retval > max);

    return retval;
}