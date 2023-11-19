# Shell Sort
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left.

<h3> Algorithm </h3>

Step 1 − Initialize the value of h <br/>
Step 2 − Divide the list into smaller sub-list of equal interval h <br/>
Step 3 − Sort these sub-lists using insertion sort <br/>
Step 3 − Repeat until complete list is sorted <br/>

Best case Time complexity - O(N(log(N))) <br/>
Worst case Time complexity - O(N * log(N<sup>2</sup>)) <br/>
Average case Time complexity - O(N<sup>2</sup>) <br/>
Space Complexity - O(1) <br/>
