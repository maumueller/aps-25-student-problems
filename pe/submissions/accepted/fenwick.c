#include <stdio.h>
#define N 1000000
#define lsb(x) 1 << __builtin_ctz(x)

int n, bit[N + 1];
void update(int i) {
    for (; i <= n; i += lsb(i))
        ++bit[i];
}

int query(int i) {
    int ans = 0;
    for (; i; i ^= lsb(i))
        ans += bit[i];

    return ans;
}

int v[N + 1];
int main(void) {
    scanf("%d", &n);

    int i, x;
    for (i = 1; i <= n; ++i) {
        scanf("%d", &x);
        v[x] = i;
    }

    long long ans = (1ll * n * (n - 1)) >> 1ll;
    for (i = 1; i <= n; ++i) {
        scanf("%d", &x);
        ans -= query(v[x]);
        update(v[x]);
    }

    printf("%lld\n", ans);
    return 0;
}
