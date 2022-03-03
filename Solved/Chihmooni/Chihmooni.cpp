#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int times[1440];

    for (int i = 0; i < 1440; i++) {
        times[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;
        string time;
        cin >> time;
        int hour, min;

        hour = ((time[0] - '0') * 10) + (time[1] - '0');
        min = ((time[3] - '0') * 10) + (time[4] - '0');

        int minutes = hour * 60 + min;
        string raftoamad;
        cin >> raftoamad;

        if (raftoamad == "+") {
            times[minutes]++;

        } else {
            times[minutes]--;
        }
    }

    for (int i = 1; i < 1440; i++) {
        times[i] += times[i - 1];
    }

    int max = -1;
    int maxIndex = -1;

    for (int i = 0; i < 1440; i++) {
        if (times[i] > max) {
            max = times[i];
            maxIndex = i;
        }
    }

    int h = maxIndex / 60;
    int m = maxIndex % 60;

    if (h < 10)
        cout << "0";

    cout << h << ":";

    if (m < 10)
        cout << "0";

    cout << m;
}