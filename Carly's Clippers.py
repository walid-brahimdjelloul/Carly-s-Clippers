hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
            #### Prices and Cuts:
## First, let’s sum up all the prices of haircuts.
total_price = 0

## Loop through the prices list and add each price to the variable total_price.
for price in prices:
  total_price += price

## average_price 
average_price = total_price / len(prices)
print("average_price: "+ str(average_price)) ## 31.875$

## That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.
new_prices = [price - 5 for price in prices]
print(new_prices)

             ### Revenue:
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

###the average daily revenue
average_daily_revenue = total_revenue / 7
print('average_daily_revenue: '+ str(average_daily_revenue))

### Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

cuts_under_30 = [hairstyles[cut] for cut in range(0,len(new_prices)-1) if new_prices[cut] < 30]
print(cuts_under_30)
