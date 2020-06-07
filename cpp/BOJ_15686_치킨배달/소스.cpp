#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
typedef struct {
	int y;
	int x;
} coor;
using namespace std;
const int MAX = 0xffffff;
int N, M;
int MAP[60][60];
vector<coor> chicken;
vector<coor> home;
vector<int> tempvector;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> MAP[i][j];
			if (MAP[i][j] == 2) {
				chicken.push_back({ i, j });
			}
			else if (MAP[i][j] == 1) {
				home.push_back({ i, j });
			}
		}
	}
	for (int i = 0; i < M; i++) {
		tempvector.push_back(1);
	}
	for (int i = 0; i < chicken.size() - M; i++) {
		tempvector.push_back(0);
	}
	
	int ans = MAX;

	sort(tempvector.begin(), tempvector.end());
	do {
		int distance = 0;
		for (int j = 0; j < home.size(); j++) {
			int sub_result = MAX;
			for (int i = 0; i < tempvector.size(); i++) {
				if (tempvector[i] == 1) {
					sub_result = min(sub_result, abs(chicken[i].y - home[j].y) + abs(chicken[i].x - home[j].x));
				}
			}
			distance += sub_result;
		}
		ans = min(ans, distance);
	} while (next_permutation(tempvector.begin(), tempvector.end()));

	cout << ans;
	return 0;
}