"""
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

height = float(input())
man_formula = (72.7 * height) - 58
women_formula = (62.1 * height) - 44.7
print("man %.1f " % man_formula)
print("women %.1f " % women_formula)
