#include <iostream>
#include <cstring>
using namespace std;

int TC, C, R, K, ans;
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };
bool visited[100][100] = { false };
int MAP[100][100] = { 0 };

void dfs(int y, int x) {
	visited[y][x] = true;
	for (int i = 0; i < 4; i++) {
		int ty = y + dy[i], tx = x + dx[i];
		if (ty < 0 || ty >= R || tx < 0 || tx >= C) continue;
		if (MAP[ty][tx] == 1 and visited[ty][tx] == false) {
			dfs(ty, tx);
		}
	}
}
	
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> TC;
	for (int tc = 0; tc < TC; tc++) {
		cin >> C >> R >> K;
		for (int i = 0; i < K; i++) {
			int y, x; cin >> x >> y;
			MAP[y][x] = 1;
		}

		ans = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (MAP[i][j] == 1 && visited[i][j] == false) {
					ans++;
					dfs(i, j);
				}
			}
		}
		memset(MAP, 0, sizeof(MAP));
		memset(visited, false, sizeof(visited));

		cout << ans << "\n";
	}
	return 0;
}