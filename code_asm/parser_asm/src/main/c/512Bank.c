#include <parm.h>
#include <stdio.h>
#include <video.h>

void run() {
    BEGIN();

    PUTCHAR('P','-','A','R','M');
    PUTCHAR('\n');
    PUTCHAR('5','1','2','B','a','n','k');

    // Example of a simple loop
    int i;
    for(i = 0; i < 5; i++) {
        PUTCHAR('!');
    }
    PUTCHAR('\n');

    // Example of a condition
    int x = 10;
    PUTCHAR('x','=','1','0','\n');
    if(x > 5) {
        PUTCHAR('G','r','e','a','t','e','r',' ','t','h','a','n',' ','5','\n');
    } else {
        PUTCHAR('L','e','s','s','e','r',' ','t','h','a','n',' ','o','r',' ','e','q','u','a','l',' ','t','o',' ','5','\n');
    }

    END();
}