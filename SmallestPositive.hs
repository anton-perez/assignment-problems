findSmallestPositive :: (Num a, Ord a) => [a] -> a  
findSmallestPositive [] = error "minimum of empty list"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs)   
  | (0 < x && x < minPositive) = x  
  | otherwise = minPositive  
  where minPositive = findSmallestPositive xs
main = print(findSmallestPositive [8, 3, -1, 2, -5, 7])