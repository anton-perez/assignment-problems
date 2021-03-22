# include <iostream>
# include <cassert>

// write your function calcSum here
int calcSum(int row1[], int row2[], int rowSum [], int numCols){
  for(int i = 0; i < numCols; i++){
    rowSum[i] = row1[i] + row2[i];
  };
}

int main() {
    std::cout << "Testing...\n";

    int matrix[2][3] = {
        { 1, 2, 3 },
        { 4, 5, 6 }
    };

    int numRows = sizeof(matrix) / sizeof(matrix[0]);
    int numCols = sizeof(matrix[0]) / sizeof(matrix[0][0]);
    // calculate numRows and numCols using a general method.
    // DO NOT just set numRows = 2 and numCols = 3.
    // hint: use the size of the variable

    assert(numRows == 2);
    assert(numCols == 3);

    int rowSum[numCols];
    calcSum(matrix[0], matrix[1], rowSum, numCols);

    assert(rowSum[0] == 5);
    assert(rowSum[1] == 7);
    assert(rowSum[2] == 9);

    std::cout << "Success!";

    return 0;
}