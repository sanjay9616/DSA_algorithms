# Quick Sort
Quicksort is a sorting algorithm based on the divide and conquer approach.

<h3> Algorithm </h3>

<b>Step 1 Divide</b> − Divide the array A[p, ..., r] by selecting a pivot element A[q], into subarray A[p, ..., q -1] and A[q + 1, ..., r] such that A[p, ..., q -1] <= A[q] <= A[q + 1, ..., r]<br/>
<b>Step 2 Conquer </b> − Sort subarray recursively <br/>
<b>Step 3 Combine </b> − Now, entire array A[p, ..., r] is sorted<br/>
Step 4 − Repeat until complete list is sorted <br/>

Best case Time complexity - O(N(log(N))) <br/>
Worst case Time complexity - O(N<sup>2</sup>) <br/>
Average case Time complexity - O(N(log(N))) <br/>

Space Complexity - O(log(N)) <br/>

