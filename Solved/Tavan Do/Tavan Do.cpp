#include <iostream>

using namespace std;

int main() {
    int n, a;
    cin >> n;
    a = 2;

    while (a < n) {
        a = a * 2;
    }

    cout << a << endl;
    return 0;
}
