#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "random_util.h"

/*

void quick_select(int s[], int k, int left, int right){
    int i, j, pivot;

    if(left <= right){



    }

}
*/

int main(){

    int a = get_random();
    printf("random=%d\n", a);

    int b = get_random_max(11);
    printf("random-max=%d\n", b);


    return 0;
}