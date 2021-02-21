recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreesCelsius  
  | degreesFahrenheit <= 50 = "You should wear a jacket."  
  | degreesFahrenheit <= 65 = "You should wear a sweater."  
  | degreesFahrenheit < 80 = "You should wear a longsleeve shirt."
  | otherwise = "You should wear a shortsleeve shirt."  
  where degreesFahrenheit = 9*degreesCelsius/5 + 32

main = print (recommendClothing 5, recommendClothing 15, recommendClothing 20, recommendClothing 30)