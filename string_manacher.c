#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void pro_process(char *s) {
    int s_len = (int) strlen(s);
    printf("s length : %d\n", s_len);

    if(s_len > 0){
        char *s1 = s;
        s = (char *) malloc(sizeof(s) + 1);

        strcat(s, "$");
        strcat(s, s1);
        printf("s=%s\n", s);

        for (int i = 1; i < s_len; ++i) {
            printf("s%d=%c\n", i, s[i]);
        }
    }
}

int main() {

    printf("hello world\n");

    char *p = "a1b1a";

    pro_process(p);

    return 0;

}