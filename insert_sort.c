
//
// 插入排序
//

void insert_sort(int *arr, int size){
    int c, j;

    //start 1
    for (int i = 1; i < size; ++i) {
        c = arr[i];//arr[i]的位置会被填入新的值,所以,必须用一个临时变量先保存好arr[i]
        for (j = i - 1; j >= 0 && c < arr[j]; --j) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = c;
    }

}