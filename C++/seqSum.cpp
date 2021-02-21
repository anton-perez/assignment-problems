# include <iostream>
# include <cassert>

int nthTerm(int n){
  if(n<2){
    return n;
  }
  else{
    return nthTerm(n-1) + 2*nthTerm(n-2);
  };
}

int seqSum(int n){
  int sum = 0;
  int arr[n+1];
  for(int i = 0; i<=n; i++){
    sum += nthTerm(i);
  };
  return sum;
}

int extendedSeqSum(int n){
  int sum = 0;
  int arr[nthTerm(n)+1];
  for(int i = 0; i<=nthTerm(n); i++){
    sum += nthTerm(i);
  };
  return sum;
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}