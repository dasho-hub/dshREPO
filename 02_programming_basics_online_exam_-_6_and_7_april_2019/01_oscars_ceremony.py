venue_rent = int(input())

statuettes = venue_rent * 0.7
cattering = statuettes * 0.85
sound = cattering * 0.5

total_cost = venue_rent + statuettes + cattering + sound

print (f"{total_cost:.2f}")