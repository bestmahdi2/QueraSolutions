#include <iostream>

using namespace std;

int main() {
    int n, m, n1, m1, b;
    cin >> n >> m;
    if (n > m){
        int temp = m;
        m = n;
        n = temp;
    }

    n1 = n;
    m1 = m;

    while (m > 0) {
        b = n % m;
        n = m;
        m = b;
    }

    cout << n << " " << (n1 * m1) / n;
    return 0;
}
