#include<bits/stdc++.h>

typedef std::vector<int> vi;
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int q, x;
    cin >> q;
    vi vec;

    for (int i = 0; i < q; i++) {
        cin >> x;
        vec.push_back(x);
    }

    for (int i = q; i > 0; i--) {
        if (q % i == 0) {
            int sum = 0;
            for (int j = 0; j < q / i; j++) {
                sum += vec[j];
            }

            int j = 0;
            for (; j < i; j++) {
                int temp = 0;

                for (int k = (j) * (q / i); k < (j + 1) * (q / i); k++) {
                    temp += vec[k];
                }

                if (temp != sum) {
                    break;
                }
            }

            if (j == i) {
                cout << i << endl;
                return 0;
            }
        }
    }
}
