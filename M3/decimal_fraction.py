print(0.1)
print(1.1)
import decimal
print(decimal.Decimal(0.1))     # 印出高精度的浮點數
print(decimal.Decimal(1.1))
print(1.1+2.2)
print(decimal.Decimal(1.1 + 2.2))
print(decimal.Decimal('1.1') + decimal.Decimal('2.2'))      # 若有包單引號就會變回字串

# ---------------------- fraction
import fractions
print(1.5)
print(fractions.Fraction(1.5))      # 印出分數
print(fractions.Fraction(1, 3))     # x,y => x/y
print(fractions.Fraction(1.1))      # 噁心
print(fractions.Fraction('1.1'))    # 印出11/10