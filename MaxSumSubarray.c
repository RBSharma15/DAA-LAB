#include <stdio.h>
#include <limits.h>

void printSubarray(int arr[], int start, int end) {
    printf("{ ");
    for (int i = start; i <= end; i++) {
        printf("%d ", arr[i]);
    }
    printf("}");
}
int max(int a, int b) {
    return (a > b) ? a : b;
}

int max_of_three(int a, int b, int c) {
    return max(max(a, b), c);
}

int maxCrossingSum(int arr[], int low, int mid, int high) {
    int sum = 0;
    int left_sum = INT_MIN;
    for (int i = mid; i >= low; i--) {
        sum = sum + arr[i];
        if (sum > left_sum) {
            left_sum = sum;
        }
    }

    sum = 0;
    int right_sum = INT_MIN;
    for (int i = mid + 1; i <= high; i++) {
        sum = sum + arr[i];
        if (sum > right_sum) {
            right_sum = sum;
        }
    }

    return max_of_three(left_sum + right_sum, left_sum, right_sum);
}

int maxSumRecursive(int arr[], int low, int high) {
    if (low == high) {
        printf("Individual element found: %d\n", arr[low]);
        return arr[low];
    }

    int mid = low + (high - low) / 2;

    printf("\n--- Dividing array segment ");
    printSubarray(arr, low, high);
    printf(" ---\n");
    printf("First subarray: ");
    printSubarray(arr, low, mid);
    printf("\nSecond subarray: ");
    printSubarray(arr, mid + 1, high);
    printf("\n");

    int left_max_sum = maxSumRecursive(arr, low, mid);
    int right_max_sum = maxSumRecursive(arr, mid + 1, high);

    int cross_max_sum = maxCrossingSum(arr, low, mid, high);
   
    printf("\n--- Applying Concept for segment ");
    printSubarray(arr, low, high);
    printf(" ---\n");
    printf("Max sum in left half: %d\n", left_max_sum);
    printf("Max sum in right half: %d\n", right_max_sum);
    printf("Max sum for crossing subarray: %d\n", cross_max_sum);

    int result = max_of_three(left_max_sum, right_max_sum, cross_max_sum);
    printf("=> Maximum of (%d, %d, %d) is %d\n", left_max_sum, right_max_sum, cross_max_sum, result);
   
    return result;
}

int main() {
    int originalArray[] = {2 , -4 , 3 , -1 , 5 , -6};
    int size = sizeof(originalArray) / sizeof(originalArray[0]);

    printf("Applying Maximum Sum Subarray using Divide and Conquer:\n");
    printf("Original Array: ");
    printSubarray(originalArray, 0, size - 1);
    printf("\n");

    int maxSum = maxSumRecursive(originalArray, 0, size - 1);

    printf("\n------------------------------------------------\n");
    printf("Final Maximum Sum of a Contiguous Subarray is: %d\n", maxSum);
    printf("------------------------------------------------\n");

    return 0;
}