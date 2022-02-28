// خر در چمن فراوونه
// ID : 9774
// https://quera.ir/problemset/contest/4065/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AE%D8%B1-%D8%AF%D8%B1-%DA%86%D9%85%D9%86-%D9%81%D8%B1%D8%A7%D9%88%D9%88%D9%86%D9%87
// https://b2n.ir/627599

#include <iostream>

using namespace std;

int main() {
    int a, b, l;
    cin >> a >> b >> l;
    int sums = 0;
    int count = 1;

    while (count <= l) {
        if (count % 2 != 0) {
            sums += a;

        } else {
            sums += b;
        }

        count += 1;
    }

    cout << sums;
    return 0;
}