#include <stdio.h>

// 递归函数，导致栈溢出
void causeStackOverflow(int count) {
    char largeArray[100000];  // 大数组，增加栈使用
    printf("Count: %d\n", count);

    // 递归调用自己，没有退出条件，将导致栈溢出
    causeStackOverflow(count + 1);
}

int main() {
    printf("hello world!\n");

    // 调用导致栈溢出的函数
    causeStackOverflow(0);

    return 0;
}
