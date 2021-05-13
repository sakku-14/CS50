pizzas = {
	"cheese": 9,
	"pepperoni": 10,
	"vegetable": 11,
	"buffalo chicken": 12,
}

pizzas["bacon"] = 14

print("cheese pizza is {0} dollors.".format(pizzas["cheese"]))
print("bacon pizza is {0} dollors.".format(pizzas["bacon"]))

for pie in pizzas:
	print(pie)

for pie, price in pizzas.items():
	print("{} pizza is {} dollors.".format(pie, price))
