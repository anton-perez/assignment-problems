# include <iostream>
# include <cassert>

int kthFibonacciNumber(int k)
{
  if(k == 0){
    return 0;
  }
  else if(k == 1){
    return 1;
  }
  else{
    return kthFibonacciNumber(k-1) + kthFibonacciNumber(k-2);
  }
}

int kthPartialSum(int k){
  int sum = 0;
  for(int i = 0; i<=k; i++){
    sum += kthFibonacciNumber(i);
  }
  return sum;
}

int metaFibonacciSum(int n)
{
  int fibs[n+1];
  for(int i = 0; i<=n; i++){
    fibs[i] = kthFibonacciNumber(i);
  }

  int sum = 0;
  for(int j = 0; j<=n; j++){
    sum += kthPartialSum(fibs[j]); 
  }
  return sum;
}

int main()
{ 
  std::cout << "Testing...\n";
  assert(metaFibonacciSum(6) == 74);

  std::cout << "Success!";

  return 0;
}