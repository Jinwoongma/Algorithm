#include <iostream>
#define MAX 10
using namespace std;

int arr[MAX] = { 10, 4, 54, 32, 15, 75, 34, 22, 16, 7 };

void quickSort(int start, int end) {
	int pivot = arr[start];
	int left = start + 1;
	int right = end;
	
	while (left <= right) {
		while (arr[left] < pivot) left++;
		while (arr[right] > pivot) right--;
		if (left <= right) swap(arr[left], arr[right]);
	}
	if (start < end) {
		swap(arr[start], arr[right]);
		quickSort(start, right - 1);
		quickSort(right + 1, end);
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
	//quickSort(0, MAX - 1);
	HeapSort(MAX);
	for (int i = 0; i < MAX; i++) {
		printf("%3d", arr[i]);
	}
}