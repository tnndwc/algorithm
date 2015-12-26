
//
// 寻找最小的K个数
//


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "random_util.h"
#include "insert_sort.h"

//选取三个数,并取其中值
int median3(int arr[], int left, int right) {

    if(left > right){
        return arr[0];
    }

    int size = 3;
    int *arr_ = (int *) malloc(sizeof(int) * size);
    int *arr_map = (int *) malloc(sizeof(int) * size);

    memset(arr_map, -1, sizeof(int) * size);

    for (int i = 0; i < size; ++i) {
        printf("map %d=%d\n", i, arr_map[i]);
    }

    //下标
    int index, lsize = right - left + 1, find;

    for (int i = 0; i < size; ++i) {

        index = (int) get_random_range(left, right);
        if(lsize >= size){
            while (1){
                find = 1;
                for (int j = 0; j < size; ++j) {
                    if(arr_map[j] == index){
                        find = 0;
                        break;
                    }
                }

                if(find == 1){
                    arr_map[i] = index;
                    break;
                } else {
                    index = (int) get_random_range(left, right);
                }
            }
        }
        arr_[i] = arr[index];
    }

    int tmp;
    for (int i = 0; i < size; ++i) {
        for (int j = i + 1; j < size; ++j) {
            if (arr_[i] > arr_[j]) {
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
    free(arr_map);
    return tmp;
}

void quick_select(int *arr, int k, int left, int right){
    int i, j, pivot, temp;
    if(left <= right){
        i = left;
        j = right - 1;
        pivot = median3(arr, left, right);
        for (;;){
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;

            if(i < j){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            } else {
                break;
            }
        }

        temp = arr[i];
        arr[i] = arr[right - 1];
        arr[right - 1] = temp;

        if(k <= i){
            quick_select(arr, k, left, i - 1);
        } else {
            quick_select(arr, k, i + 1, right);
        }

    }
}


int main() {
/*
    int a = get_random();
    printf("random=%d\n", a);

    for (int j = 0; j < 1; ++j) {
        a = (int) get_random_range(10, 20);
        printf("random-range=%d\n", a);
        if(a == 100){
            printf("random index : %d\n", j);
            break;
        } else if(a < 10 || a > 20){
            printf("random index : %d\n", j);
            break;
        }
    }


    int b = (int) get_random_max(11);
    printf("random-max=%d\n", b);
*/
    int arr[] = {1, 3, 0, 100, 9, 7, 2};
    //int m3 = median3(arr, 0, 6);
    //printf("m3=%d\n", m3);

    quick_select(arr, 4, 0, 6);

    //Insert Sort
    //insert_sort(arr, 7);

    for (int i = 0; i < 7; ++i) {
        printf("sort: arr[%d]=%d\n", i, arr[i]);
    }

    return 0;
}