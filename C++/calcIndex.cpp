# include <iostream>
# include <cassert>

int nthFibonacci(int n){
  if(n<2){
    return n;
  };
  return nthFibonacci(n-1) + nthFibonacci(n-2);
}

int calcIndex(int n){
  int fibIndex = 0;
  int fibVal = nthFibonacci(fibIndex);
  while(fibVal <= n){
    fibIndex += 1;
    fibVal = nthFibonacci(fibIndex);
  };

  return fibIndex;
}

int main()
{
  std::cout << "Testing...\n";
  assert(calcIndex(8)==7);
  assert(calcIndex(100000)==26);

  std::cout << "Success!";

  return 0;
}