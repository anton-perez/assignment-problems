letterToPoint n 
  | n == "A" = 4
  | n == "B" = 3
  | n == "C" = 2
  | n == "D" = 1
  | n == "F" = 0
  | otherwise = 0

pointList x = [letterToPoint n | n<-x]
calcGPA x = sum(pointList x) / (length x)

main = print(calcGPA ["A", "B", "B", "C", "C", "C", "D", "F"])