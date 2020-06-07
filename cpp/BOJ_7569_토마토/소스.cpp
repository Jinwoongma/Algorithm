#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>

typedef struct{
	int h;
	int y;
	int x;
}tomato;

using namespace std;
int R, C, H;
int MAP[110][110][110] = { 0 };
int d[110][110][110];
int dh[6] = { -1, 1, 0, 0, 0, 0 };
int dy[6] = { 0, 0, -1, 1, 0, 0 };
int dx[6] = { 0, 0, 0, 0, -1, 1 };
queue<tomato> startPoint;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> C >> R >> H;
	memset(d, -1, sizeof(d));
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				cin >> MAP[i][j][k];
				d[i][j][k] = -1;
				if (MAP[i][j][k] == 1) {
					d[i][j][k] = 0;
					startPoint.push({ i, j, k });
				}
			}
		}
	}
	while (!startPoint.empty()) {
		int h = startPoint.front().h;
		int y = startPoint.front().y;
		int x = startPoint.front().x;
		startPoint.pop();
		for (int dir = 0; dir < 6; dir++) {
			int th = h + dh[dir], ty = y + dy[dir], tx = x + dx[dir];
			if (th < 0 || th >= H || ty < 0 || ty >= R || tx < 0 || tx >= C) continue;
			if (MAP[th][ty][tx] == 0) {
				if (d[th][ty][tx] == -1) {
					d[th][ty][tx] = d[h][y][x] + 1;
					startPoint.push({ th, ty, tx });
				}
				else {
					if (d[th][ty][tx] > d[h][y][x] + 1) {
						d[th][ty][tx] = d[h][y][x] + 1;
						startPoint.push({ th, ty, tx });
					}
				}

			}
				
		}
	}

	int ans = 0;
	bool flag = true;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				ans = max(ans, d[i][j][k]);
				if (MAP[i][j][k] == 0 && d[i][j][k] == -1) {
					flag = false;
				}
			}
		}
	}
	ans = flag ? ans : -1;
	cout << ans;
	return 0;

}