#include <stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[]) {
    int a;
    int *p;
    p = (int*)malloc(20*sizeof(int));
    for(int i = 0;i < 20 ;i++){
        p[i] = i;
        printf("%p %d\n",p+i ,*(p+i));
        //printf("%p %d\n",p[i] ,p[i]);
    }
    free(p);
    //printf("%p %d\n",p ,*p);

    return 0;
}
