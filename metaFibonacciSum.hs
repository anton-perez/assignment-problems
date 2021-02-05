fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

partialSumEntries k = [fib x | x <- [0..k]]
sumList [] = 0
sumList (x:xs) = x + sumList xs
partialSum k = sumList (partialSumEntries k)
metaSumEntries n = [partialSum x | x <-partialSumEntries n]
metaSum n = sumList (metaSumEntries n)

main = print(metaSum 6)