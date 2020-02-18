def final_amount(p, r, n, t):
	"""
	Apply the compound interest formula to p 
	to produce the final amount.
	P = principal amount
	R = Annual nominal interest rate (as decimal)
	N = number of times the interest is compunded per year
	T = Number of years
	"""
	a = p * (1 + r/n) ** (n * t)
	return a  # This is new, and makes the function fruitful

toInvest = float(input("How much do you want to invest? "))

fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have: ", fnl)