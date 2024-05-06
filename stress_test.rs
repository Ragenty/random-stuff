use std::thread;
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, Ordering};

const NUM_THREADS: usize = 4;
const UPPER_LIMIT: u64 = 10_000_000;

fn is_prime(n: u64) -> bool {
    if n <= 1 {
        return false;
    }
    if n <= 3 {
        return true;
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false;
    }
    let mut i = 5;
    while i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}

fn find_primes(start: u64, end: u64, running: Arc<AtomicBool>) {
    let mut n = start;
    while n <= end && running.load(Ordering::Relaxed) {
        if is_prime(n) {
            // Print the prime number
            println!("{}", n);
        }
        n += 1;
    }
}

fn main() {
    let running = Arc::new(AtomicBool::new(true));
    let mut handles = vec![];

    for _ in 0..NUM_THREADS {
        let running_clone = running.clone();
        let handle = thread::spawn(move || {
            find_primes(2, UPPER_LIMIT, running_clone);
        });
        handles.push(handle);
    }

    // Let it run for a while
    thread::sleep(std::time::Duration::from_secs(10));

    // Stop the threads
    running.store(false, Ordering::Relaxed);

    // Wait for all threads to finish
    for handle in handles {
        handle.join().unwrap();
    }
}
