function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;

    if (num % 2 === 0 || num % 3 === 0) return false;

    let i = 5;
    while (i * i <= num) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
        i += 6;
    }

    return true;
}

function findPrimesInRange(start, end) {
    const primes = [];

    for (let num = start; num <= end; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }

    return primes;
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter the start of the range: ', (start) => {
    readline.question('Enter the end of the range: ', (end) => {
        const primesInRange = findPrimesInRange(parseInt(start), parseInt(end));
        console.log('Prime numbers in the range:', primesInRange);
        readline.close();
    });
});
