#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#define MAX 987654321
using namespace std;
int TC, N, n;
int nums[11] = { 0 };
bool visited[11] = { false };
int ans = MAX;
vector<int> G[11];
vector<int> A;
vector<int> B;

void dfs(int idx, bool visited[], vector<int> V) {
	visited[idx] = true;
	for (int i = 0; i < G[idx].size(); i++) {
		int next = G[idx][i];
		auto it = find(V.begin(), V.end(), next);
		if (visited[next] == false && it != V.end()) {
			dfs(next, visited, V);
		}
	}
}

bool allConnected(vector<int> V) {
	memset(visited, false, sizeof(visited));
	if (V.size() == 0) {
		return false;
	}
	int start = V.front();
	dfs(start, visited, V);
	
	for (int i = 0; i < V.size(); i++) {
		if (visited[V[i]] == false) {
			return false;
		}
	}
	return true;
}

void makeSubset(int n) {
	int i, j, diff, A_sum, B_sum;
	for (i = 0; i < (1 << n); i++) {
		A.clear();
		B.clear();
		A_sum = 0, B_sum = 0;
		for (j = 0; j < n; j++) {
			if (i & (1 << j)) {
				A.push_back(j + 1);
				A_sum += nums[j];
			}
			else {
				B.push_back(j + 1);
				B_sum += nums[j];
			}
		}
		if (allConnected(A) && allConnected(B)) {
			diff = abs(A_sum - B_sum);
			if (diff < ans) ans = diff;
		}
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> nums[i];
	}
	for (int u = 1; u <= N; u++) {
		cin >> n;
		for (int j = 0; j < n; j++) {
			int v; cin >> v;
			G[u].push_back(v);
			G[v].push_back(u);
		}
	}

	makeSubset(N);
	ans = (ans == MAX) ? -1 : ans;
	cout << ans;
	return 0;
}