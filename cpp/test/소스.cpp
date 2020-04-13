#include <stdio.h>
#define MAX 15
int arr[MAX] = { 10, 30, 23, 2, 4, 5, 43, 33, 6, 9, 15, 12, 14, 26, 37 };
int temp[MAX] = { 0 };

void heapfy(int size, int mid) {
	int parent = mid;
	int left_node = mid * 2 + 1;
	int right_node = mid * 2 + 2;
	int largest_node = parent;
	int temp;

	if (left_node < size && arr[left_node] > arr[largest_node]) {
		largest_node = left_node;
	}
	if (right_node < size && arr[right_node] > arr[largest_node]) {
		largest_node = right_node;
	}
	if (largest_node != parent) {
		temp = arr[largest_node];
		arr[largest_node] = arr[parent];
		arr[parent] = temp;
		heapfy(size, largest_node);
	}
}

void BuildMaxheap(int size) {
	int mid = size / 2 - 1;
	for (mid; mid >= 0; mid--) {
		heapfy(size, mid);
	}
}

void heapSort(int size) {
	int temp;
	BuildMaxheap(MAX);
	while (size > 1) {
		temp = arr[0];
		arr[0] = arr[size - 1];
		arr[size - 1] = temp;
		size--;
		heapfy(size, 0);
	}
}

void quickSort(int start, int end) {
	int pivot = arr[start];
	int left = start + 1;
	int right = end;
	int temp;
	while (left <= right) {
		while (arr[left] < pivot) left++;
		while (arr[right] > pivot) right--;
		if (left <= right) {
			temp = arr[left];
			arr[left] = arr[right];
			arr[right] = temp;
		}
	}
	if (start < end) {
		temp = arr[start];
		arr[start] = arr[right];
		arr[right] = temp;

		quickSort(start, right - 1);
		quickSort(right + 1, end);
	}
}

void mergeSort(int lo, int hi) {
	if (lo == hi) return;
	int mid;
	mid = (lo + hi) / 2;
	mergeSort(lo, mid);
	mergeSort(mid + 1, hi);

	// merge
	int i, j, k;
	i = lo, j = mid + 1, k = lo;
	while (i <= mid && j <= hi) {
		if (arr[i] < arr[j]) {
			temp[k++] = arr[i++];
		}
		else {
			temp[k++] = arr[j++];
		}
	}
	while (i <= mid) {
		temp[k++] = arr[i++];
	}
	while (j <= hi) {
		temp[k++] = arr[j++];
	}
	for (i = lo; i <= hi; i++) {
		arr[i] = temp[i];
	}
}

void InsertionSort() {
	int i, j, temp;
	for (i = 0; i < MAX; i++) {
		temp = arr[i];
		j = i;
		while (j > 0 && arr[j - 1] > temp) {
			arr[j] = arr[j - 1];
			j--;
		}
		arr[j] = temp;
	}
}

void selectionSort() {
	int i, j, minIndex, temp;
	for (i = 0; i < MAX; i++) {
		minIndex = i;
		for (j = i; j < MAX; j++) {
			if (arr[j] < arr[minIndex]){
				minIndex = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[minIndex];
		arr[minIndex] = temp;
	}
}

void shellSort() {
	int i, j, k, gap, temp;
	for (gap = MAX / 2; gap > 0; gap /= 2) {
		if (gap % 2 == 0) {
			gap++;
		}
		for (i = gap; i < MAX; i++) {
			temp = arr[i];
			j = i;
			while (j >= gap && arr[j - gap] > temp) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			arr[j] = temp;
		}
	}
}

void bubbleSort() {
	int i, j, temp;
	for (i = MAX - 1; i >= 0; i--) {
		for (j = 1; j <= i; j++) {
			if (arr[j - 1] > arr[j]) {
				temp = arr[j];
				arr[j] = arr[j - 1];
				arr[j - 1] = temp;
			}
		}
	}
}

int main() {
	//mergeSort(0, MAX - 1);
	//InsertionSort();
	//selectionSort();
	//shellSort();
	//bubbleSort();
	//quickSort(0, MAX - 1);
	heapSort(MAX);
	for (int i = 0; i < MAX; i++) {
		printf("%4d", arr[i]);
	}

}