chain :: (Integral a) => a -> [a]  
chain 1 = [1]  
chain n  
  | even n =  n:chain (n `div` 2)  
  | odd n  =  n:chain (n*3 + 1)

chainLength n = length(chain n)
chainLengths n = takeWhile (<=n) (map (chainLength) [1..])

firstNumberWithChainLengthGreaterThan n = length(chainLengths n) + 1

main = print(firstNumberWithChainLengthGreaterThan 15)