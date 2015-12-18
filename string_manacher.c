#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* pro_process(char *s) {
    int s_len = (int) strlen(s);
    printf("s length : %d\n", s_len);

    if(s_len > 0){
        char *s1 = s;
        s = (char *) malloc( 2 * sizeof(s) + 2);

        int j=0;
        s[j]='$';
        for (int i = 0; i < s_len; i++) {
            s[++j]='#';
            s[++j]=s1[i];
        }
    }
    return s;
}

int main() {

    printf("hello world\n");

    char *p = "a1b1a";

    p = pro_process(p);

    printf("p=%s", p);
    return 0;

}