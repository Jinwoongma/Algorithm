#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

typedef struct {
	int y, x;
}coor;

int R, C, T, ans;
int MAP[60][60];
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

vector<coor> cleaner;
vector<int> temp;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> R >> C >> T;
	vector<coor> dust;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> MAP[i][j];
			if (MAP[i][j] > 0) {
				dust.push_back({ i, j });
			}
			else if (MAP[i][j] == -1) {
				cleaner.push_back({ i, j });
			}
		}
	}

	while (T--) {
		int newMAP[60][60] = { 0 };
		for (int i = 0; i < dust.size(); i++) {
			int y = dust[i].y, x = dust[i].x;
			int cnt = 0;
			for (int dir = 0; dir < 4; dir++) {
				int ty = y + dy[dir], tx = x + dx[dir];
				if (ty < 0 or ty >= R or tx < 0 or tx >= C) continue;
				if (MAP[ty][tx] == -1) continue;
				cnt++;
				newMAP[ty][tx] += (MAP[y][x] / 5);
			}
			newMAP[y][x] += (MAP[y][x] - (cnt * (MAP[y][x] / 5)));
		}
		for (int i = 0; i < cleaner.size(); i++) {
			int y = cleaner[i].y, x = cleaner[i].x;
			newMAP[y][x] -= 1;
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				MAP[i][j] = newMAP[i][j];
			}
		}

		// 윗방향 이동
		int y = cleaner[0].y, x = cleaner[0].x, d = 3, temp = 0;
		while (1) {
			int ty = y + dy[d], tx = x + dx[d];
			if (d == 3 && tx >= C) {
				d = 0; ty = y + dy[d]; tx = x + dx[d];
			}
			else if (d == 0 && ty < 0) {
				d = 2; ty = y + dy[d]; tx = x + dx[d];
			}
			else if (d == 2 && tx < 0) {
				d = 1; ty = y + dy[d]; tx = x + dx[d];
			}

			if (MAP[ty][tx] != -1) {
				swap(MAP[ty][tx], temp);
				y = ty; x = tx;
			}
			else {
				break;
			}
		}

		// 아랫방향 이동
		y = cleaner[1].y, x = cleaner[1].x, d = 3, temp = 0;
		while (1) {
			int ty = y + dy[d], tx = x + dx[d];
			if (d == 3 && tx >= C) {
				d = 1; ty = y + dy[d]; tx = x + dx[d];
			}
			else if (d == 1 && ty >= R) {
				d = 2; ty = y + dy[d]; tx = x + dx[d];
			}
			else if (d == 2 && tx < 0) {
				d = 0; ty = y + dy[d]; tx = x + dx[d];
			}

			if (MAP[ty][tx] != -1) {
				swap(MAP[ty][tx], temp);
				y = ty; x = tx;
			}
			else {
				break;
			}
		}

		ans = 0;
		dust.clear();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (MAP[i][j] > 0) {
					dust.push_back({ i, j });
					ans += MAP[i][j];
				}
			}
		}
	}

	cout << ans << ' ';
	return 0;

}