#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
int R, C, ans, y, x, ty, tx;
int MAP[1010][1010];
int d[1010][1010];
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };
typedef pair<int, int> P;
queue<P> startPoint;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> C >> R;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> MAP[i][j];
			d[i][j] = -1;
			if (MAP[i][j] == 1) {
				startPoint.push({ i, j });
				d[i][j] = 0;
			}
		}
	}
	while (!startPoint.empty()) {
		y = startPoint.front().first;
		x = startPoint.front().second;
		startPoint.pop();
		for (int dir = 0; dir < 4; dir++) {
			ty = y + dy[dir];
			tx = x + dx[dir];
			if (ty < 0 || ty >= R || tx < 0 || tx >= C) continue;
			if (MAP[ty][tx] == 0 && d[ty][tx] == -1) {
				d[ty][tx] = d[y][x] + 1;
				startPoint.push({ ty, tx });
			}
		}
	}

	bool flag = true;
	ans = 0;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			ans = max(ans, d[i][j]);
			if (MAP[i][j] == 0 && d[i][j] == -1) {
				flag = false;
			}
		}
	}
	
	ans = flag ? ans : -1;
	cout << ans;
	
	return 0;
}