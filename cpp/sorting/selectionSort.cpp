// 선택정렬 알고리즘
#include <iostream>
#define MAX 100
using namespace std;
int Buf[MAX];
int temp[MAX] = { 0 };

bool IsNumberExist(int number, int index) {
	int i;
	for (i = 0; i < index; i++) {
		if (Buf[i] == number) {
			return true;
		}
	}
	return false;
}

void MakeRandomNumber() {
	int i, Num;
	i = 1;
	Buf[0] = 100;

	while (i < MAX) {
		Num = rand() % MAX;
		if (!IsNumberExist(Num, i)) {
			Buf[i] = Num;
			i++;
		}
	}
}

void Display() {
	int i;
	for (i = 0; i < MAX; i++) {
		if (i % 10 == 0) {
			printf("\n");
		}
		printf("%4d", Buf[i]);
	}
}

//void SelectionSort() {
//	int i, j,minIndex;
//	for (i = 0; i < MAX - 1; i++) {
//		minIndex = i;
//		for (j = i + 1; j < MAX; j++) {
//			if (Buf[j] < Buf[minIndex]) {
//				minIndex = j;
//			}
//		}
//		swap(Buf[i], Buf[minIndex]);
//	}
//}

//void InsertionSort() {
//	int i, j, temp;
//	for (i = 0; i < MAX; i++) {
//		j = i;
//		temp = Buf[i];
//		while (j > 0 && Buf[j - 1] > temp) {
//			Buf[j] = Buf[j - 1];
//			j--;
//		}
//		Buf[j] = temp;
//	}
//}

//void BubbleSort() {
//	int i, j;
//	for (i = MAX - 1; i >= 0; i--) {
//		for (j = 1; j <= i; j++) {
//			if (Buf[j-1] > Buf[j]) {
//				swap(Buf[j], Buf[j - 1]);
//			}
//		}
//	}
//}

//void ShellSort() {
//	int i, j, gap, v;
//
//	for (gap = MAX / 2; gap > 0; h /= 2) {
//		if (gap % 2 == 0) {
//			gap++;
//		}
//		for (i = gap; i < MAX; i++) {
//			v = Buf[i];
//			j = i;
//
//			while (j >= gap && Buf[j - gap] > v) {
//				Buf[j] = Buf[j - gap];
//				j -= gap;
//			}
//			Buf[j] = v;
//		}
//	}
//}

void MergeSort(int lo, int hi) {
	if (lo == hi) return;

	int i, j, k, mid;
	mid = (lo + hi) >> 1;
	MergeSort(lo, mid);
	MergeSort(mid + 1, hi);

	i = lo, j = mid + 1, k = lo;
	while (i <= mid && j <= hi) {
		if (Buf[i] < Buf[j]) {
			temp[k++] = Buf[i++];
		}
		else {
			temp[k++] = Buf[j++];
		}
	}

	while (i <= mid) {
		temp[k++] = Buf[i++];
	}
	while (j <= hi) {
		temp[k++] = Buf[j++];
	}
	for (i = lo; i <= hi; i++) {
		Buf[i] = temp[i];
	}
}

void QuickSort(int start, int end) {
	int pivot = Buf[start];
	int left = start + 1;
	int right = end;
	while (left <= right) {
		while(Buf[left] < pivot) left++;
		while (Buf[right] > pivot) right--;
		if (left <= right) swap(Buf[left], Buf[right]);
	}
	
	if (start < end) { // 한개로 쪼개질때까지
		swap(Buf[start], Buf[right]);
		QuickSort(start, right - 1);
		QuickSort(right + 1, end);
	}
}

void heapfy(int size, int mid) {
	int parent = mid;
	int left_node = parent * 2 + 1;
	int rignt_node = parent * 2 + 2;
	int largest_node = parent;
	
	if (left_node < size && Buf[left_node] > Buf[largest_node]) {
		largest_node = left_node;
	}
	if (rignt_node < size && Buf[rignt_node] > Buf[largest_node]) {
		largest_node = rignt_node;
	}
	if (parent != largest_node) {
		swap(Buf[parent], Buf[largest_node]);
		heapfy(size, largest_node);
	}
	
}

void BuildMaxHeap(int size) {
	int mid = size / 2 - 1;  // 배열의 인덱스가 0부터 시작하므로 -1을 해준다.

	for (mid; mid >= 0; mid--) {
		heapfy(size, mid);
	}
}

void HeapSort(int size) {
	BuildMaxHeap(MAX);  // 배열을 힙으로 변환
	
	while (size > 1) {
		swap(Buf[0], Buf[size - 1]); // 최대값들이 끝쪽부터 쌓임
		size--;
		heapfy(size, 0);
	}

}

int main() {
	MakeRandomNumber();
	Display();
	//SelectionSort();
	//InsertionSort();
	//BubbleSort();
	//ShellSort();
	//MergeSort(0, MAX - 1);
	//QuickSort(0, MAX - 1);
	HeapSort(MAX);
	Display();
}