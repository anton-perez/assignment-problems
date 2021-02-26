#include <iostream>
#include <cassert>

int calcSum(int m, int n){
  int ascending[m][n];
  int descending[n][m];

  for(int i1=0; i1<n; i1++){
    for(int i2=0; i2<m; i2++){
      ascending[i2][i1] = 1 + i1 + i2*n;
      descending[i1][i2] = m*n - i2 - i1*m ;
    };
  };

  int product[m][m]; 
  int sum = 0;

  for(int i=0; i<m; i++){
    for(int j=0; j<m; j++){
      int dotProduct = 0;
      for(int k=0; k<n; k++){
        dotProduct += ascending[i][k]*descending[k][j];
      }; 
      product[i][j] = dotProduct;
      sum += product[i][j];
    };
  };

  return sum;
}

int main() {
  std::cout << "Testing...\n";
  assert(calcSum(2,3)==131);
  std::cout << "Success!";
}