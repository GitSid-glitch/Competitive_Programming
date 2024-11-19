  
#include <iostream>  
#include <vector>  
#include <algorithm>  
  
using namespace std;  
  
const int N = 405;  
  
int n, m, p, s[N], u[N], v[N], w[N], f[N][N], g[N][N], ans[N];  
vector<int> e[N];  
  
void dfs(int u, int fa) {  
   for (int v : e[u]) {  
      if (v != fa) {  
        dfs(v, u);  
        for (int i = 1; i <= n; i++) {  
           f[u][i] = max(f[u][i], f[v][i]);  
        }  
      }  
   }  
   for (int i = 1; i <= n; i++) {  
      f[u][i] = max(f[u][i], g[u][i]);  
   }  
   for (int i = n; i > 0; i--) {  
      f[u][i] = min(f[u][i], f[u][i + 1]);  
   }  
}  
  
void solve() {  
   cin >> n >> m >> p;  
   for (int i = 1; i <= p; i++) {  
      cin >> s[i];  
   }  
   for (int i = 1; i <= m; i++) {  
      cin >> u[i] >> v[i] >> w[i];  
      e[u[i]].push_back(v[i]);  
      e[v[i]].push_back(u[i]);  
   }  
   for (int i = 1; i <= n; i++) {  
      for (int j = 1; j <= n; j++) {  
        f[i][j] = g[i][j] = 0;  
      }  
   }  
   for (int i = 1; i <= m; i++) {  
      for (int j = 1; j <= n; j++) {  
        g[u[i]][j] = max(g[u[i]][j], w[i]);  
        g[v[i]][j] = max(g[v[i]][j], w[i]);  
      }  
   }  
   dfs(1, 0);  
   for (int i = 1; i <= n; i++) {  
      ans[i] = 0;  
   }  
   for (int i = 1; i <= p; i++) {  
      for (int j = 1; j <= n; j++) {  
        ans[j] += f[s[i]][j];  
      }  
   }  
   for (int i = 1; i <= n; i++) {  
      cout << ans[i] << " ";  
   }  
   cout << endl;  
   for (int i = 1; i <= n; i++) {  
      e[i].clear();  
   }  
}  
  
int main() {  
   int t;  
   cin >> t;  
   while (t--) {  
      solve();  
   }  
   return 0;  
}
