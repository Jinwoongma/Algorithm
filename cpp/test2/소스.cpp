#include <iostream>
//#include <cstdlib>
#include <ctime>
#define MAX 10
using namespace std;

int arr[MAX] = { 10, 4, 54, 32, 15, 75, 34, 22, 16, 7 };

int Partition(int start, int end) {
	srand(time(NULL));
	int rnum = start + (rand() % (end - start + 1));
	swap(arr[end], arr[rnum]);
	int pivot = arr[end];
	int rose = start;

	for (int i = start; i < end; i++) {
		if (arr[i] <= pivot) {
			swap(arr[rose], arr[i]);
			rose++;
		}
	}
	swap(arr[end], arr[rose]);
	return rose;
}
void quickSort(int start, int end) {
	if (start < end) {
		int index = Partition(start, end);
		quickSort(start, index - 1);
		quickSort(index + 1, end);
	}
}

void heapfy(int size, int mid) {
	int parent = mid;
	int left = mid * 2 + 1;
	int right = mid * 2 + 2;
	int largest = parent;

	if (arr[left] > arr[largest] && left < size) { largest = left; }
	if (arr[right] > arr[largest] && right < size) { largest = right; }
	if (largest != parent) {
		swap(arr[largest], arr[parent]);
		heapfy(size, largest);
	}
}

void BuildHeap(int size) {
	int mid = size / 2 + 1;
	for (mid; mid >= 0; mid--) {
		heapfy(size, mid);
	}
}

void HeapSort(int size) {
	BuildHeap(size);
	while(size > 1) {
		swap(arr[0], arr[size - 1]);
		size--;
		heapfy(size, 0);
	}
}

int main() {
	for (int i = 0; i < MAX; i++) {
		printf("%3d", arr[i]);
	}
	cout << endl;
	quickSort(0, MAX - 1);
	//HeapSort(MAX);
	for (int i = 0; i < MAX; i++) {
		printf("%3d", arr[i]);
	}
}