listFactors n = [k | k <- [1..n], n `mod` k == 0]
sumFactors n = sum (listFactors n)

main = print(sumFactors 10)