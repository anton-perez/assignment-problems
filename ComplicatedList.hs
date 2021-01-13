calcList n = length [(x,y)| x<-[-n..n], y<-[-n..n], x `notElem` [-2, -1, 0, 1, 2], y `notElem` [-2, -1, 0, 1, 2], x-y <= x*y/2, x*y/2 <= x+y]
main = print (calcList 50)