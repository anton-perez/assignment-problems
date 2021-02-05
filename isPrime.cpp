#include <iostream>
#include <cassert>

bool isPrime(int x)
{
  bool prime_boolean = true;
  if(x == 0 || x ==1){
    return false;
  };
  for(int n = 2; n <= x/2; n++){
    if((x%n) == 0){
      prime_boolean = false;
    };
  };
   
  return prime_boolean;
}

int main()
{
  assert(!isPrime(0));
  assert(!isPrime(1));
  assert(isPrime(2));
  assert(isPrime(3));
  assert(!isPrime(4));
  assert(isPrime(5));
  assert(isPrime(7));
  assert(!isPrime(9));
  assert(isPrime(11));
  assert(isPrime(13));
  assert(!isPrime(15));
  assert(!isPrime(16));
  assert(isPrime(17));
  assert(isPrime(19));
  assert(isPrime(97));
  assert(!isPrime(99));
  assert(!isPrime(99));
  assert(isPrime(13417));

  std::cout << "Success!";

  return 0;
}