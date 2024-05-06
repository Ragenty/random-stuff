include "stdlib.hhc"
include "stdio.hhc"

const UPPER_LIMIT = 1000000;

int is_prime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    int i = 5;
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
        i += 6;
    }
    return 1;
}

void main() {
    int count = 0;
    for (int i = 2; i <= UPPER_LIMIT; ++i) {
        if (is_prime(i)) {
            // Print the prime number to stress the CPU
            printf("%d\n", i);
        }
    }
}
