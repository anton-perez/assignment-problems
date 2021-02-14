# include <iostream>
# include <cassert>
int main()
{
  int array[5]{ 30, 50, 20, 10, 40 };
  
  for(int i = 0; i<5; i++){
    int minimum = array[i];
    int min_index = i;
    for(int j = i; j<5; j++){
      if(array[j] < minimum){
        minimum = array[j];
        min_index = j;
      } 
    };
    int tempVal = array[i];
    array[i] = minimum;
    array[min_index] = tempVal;
  };

  std::cout << "Testing...\n";

  assert(array[0]==10);
  assert(array[1]==20);
  assert(array[2]==30);
  assert(array[3]==40);
  assert(array[4]==50);

  std::cout << "Succeeded";

  return 0;
}