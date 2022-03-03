#include <bits/stdc++.h>

using namespace std;
#define ll int
#define K ((ll)3010)
#define M ((ll)1010)
#define N ((ll)100*1000+10)
#define Q ((ll)1000*1000+10)

ll n, m, k, q, id[N], l[Q], r[Q], ans[Q];
bitset<K> a[M], b[N];
vector<ll> qu;

void solve(ll xl, ll xr) {
    if (xr - xl == 1) {
        ll res = a[id[xl]].count();
        for (auto u:qu)ans[u] = res;
        return;
    }

    ll mid = (xl + xr) / 2;
    b[mid] = a[id[mid]];

    for (int i = mid + 1; i < xr; i++)b[i] = (b[i - 1] | a[id[i]]);
    b[mid - 1] = a[id[mid - 1]];

    for (int i = mid - 2; i >= xl; i--)b[i] = (b[i + 1] | a[id[i]]);
    vector<ll> lft, rght;

    for (auto u:qu) {
        if (l[u] < mid && mid <= r[u])ans[u] = (b[l[u]] | b[r[u]]).count();
        if (r[u] < mid)lft.push_back(u);
        if (mid <= l[u])rght.push_back(u);
    }

    qu.swap(lft);
    solve(xl, mid);
    qu.swap(rght);
    solve(mid, xr);
}

int main() {
    scanf("%d%d%d", &n, &m, &k);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < k; j++) {
            char c;
            scanf(" %c", &c);
            if (c == '1')a[i][j] = 1;
        }

        ll x, ex;
        scanf("%d", &x);

        for (int j = 0; j < x; j++) {
            scanf("%d", &ex);
            ex--;
            id[ex] = i;
        }
    }

    scanf("%d", &q);

    for (int i = 0; i < q; i++) {
        scanf("%d%d", &l[i], &r[i]);
        l[i]--;
        r[i]--;
        qu.push_back(i);
    }

    solve(0, n);

    for (int i = 0; i < q; i++)printf("%d\n", ans[i]);

    return 0;
}