#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "random_util.h"


int median3(int arr[], int left, int right){
    int max = right - left;

    int size = 3;
    int *arr_ = (int *) malloc(sizeof(int) * size);
    int *hash = (int *) malloc(sizeof(int) * (max + 1));

    memset(hash, 0, sizeof(int) * (max + 1));

    int index;
    for (int i = 0; i < size; ++i) {

        while ( hash[(index = (int) get_random_max(max))] > 0 ){
            index = (int) get_random_max(max);
        }

        hash[index] = 1;
        arr_[i] = arr[index];

    }

    int tmp;
    for (int i = 0; i < size; ++i) {
        for (int j = i + 1; j < size; ++j) {
            if(arr_[i] > arr_[j]){
                tmp = arr_[i];
                arr_[i] = arr_[j];
                arr_[j] = tmp;
            }
        }
    }

   /* for (int i = 0; i < size; ++i) {
        printf("arr_ %d = %d\n", i, arr_[i]);
    }*/

    tmp = arr_[size / 2];
    free(arr_);
    free(hash);
    return tmp;
}

/*void quick_select(int s[], int k, int left, int right){
    int i, j, pivot;

    if(left <= right){



    }

}*/


int main(){

    int a = get_random();
    printf("random=%d\n", a);

    int b = get_random_max(11);
    printf("random-max=%d\n", b);

    int arr[] = {1, 3, 0, 100, 9, 7, 999};
    int m3 = median3(arr, 0, 6);
    printf("m3=%d\n", m3);

    return 0;
}