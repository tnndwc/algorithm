#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NUM_ELEM(x) (sizeof (x) / sizeof (*(x)))


//$#a#1#b#1#a
char *pro_process(char *s) {
    int s_len = (int) strlen(s);
    printf("s length : %d\n", s_len);

    if (s_len > 0) {
        char *s1 = s;
        s = (char *) malloc(2 * sizeof(s) + 1);//1=\0

        int j = 0;
        s[j] = '$';
        for (int i = 0; i < s_len; i++) {
            s[++j] = '#';
            s[++j] = s1[i];
        }
        s[++j] = '#';
    }
    return s;
}

int min(int a, int b) {
    if (a < b) {
        return a;
    }
    return b;
}

int max(int *num, int len){
    int max_val = num[0];

    for (int i = 1; i < len; ++i) {
        if(max_val < num[i]){
            max_val = num[i];
        }
    }
    return max_val;
}


int get_str_len(char *s) {
    int len = 0, str_len = strlen(s);
    if (str_len > 0) {
        int p[str_len], mx = 0, id = 0;
      //  memset(p, 0, str_len);
        p[0]=0;
        for (int i = 1; i < str_len; ++i) {//for (int i = 1; s[i] != '\0'; i++){
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1;
            while (s[i + p[i]] == s[i - p[i]]){
                p[i]++;
            }
            if(i + p[i] > mx){
                mx = i + p[i];
                id = i;
            }
        }

        for (int i = 0; i < str_len; ++i) {
            printf("ele %d=%d\n", i, p[i]);
        }
        len = max(p, str_len);
    }
    return len;
}

/*
int get_str_len(char *s) {
    int len = 0, str_len = strlen(s);
    if (str_len > 0) {
        int *p = (int *) malloc(sizeof(int)*(str_len - 1));// - 1 : \0
        int mx = 0, id = 0;
        memset(p, 0, str_len);
        printf("get str len s=%d\n", str_len);
        printf("get str len s1=%d\n",(int) ( sizeof(int)));
        printf("get str len p ele =%d\n", (int) (sizeof(*p)));
        printf("get str len point p=%d\n", (int) (sizeof(p)));//指针地址宽度,32bit=4,64bit=8
        printf("get str len s1=%d\n",( (int) sizeof(int)*(str_len - 1)));
        printf("get str len p=%d\n", (int) (sizeof(int) * (sizeof(*p))));
        printf("get str len p=%d\n", (int) (sizeof(p) * (sizeof(*p))));
        for (int i = 1; i < str_len; ++i) {//for (int i = 1; s[i] != '\0'; i++){
            p[i] = mx > i ? min(p[2 * id - i], mx - i) : 1;
            while (s[i + p[i]] == s[i - p[i]]){
                p[i]++;
            }
            if(i + p[i] > mx){
                mx = i + p[i];
                id = i;
            }
        }
        len = max(p);
    }
    return len;
}*/

int main() {

    printf("hello world\n");

    char *p = "1a1b1ax";

    p = pro_process(p);

    printf("p=%s\n", p);

    int rs = get_str_len(p);

    printf("p huiwen =%d\n", rs);

    return 0;

}