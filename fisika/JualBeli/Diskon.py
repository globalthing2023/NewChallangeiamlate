# ket:
# D = Discount amount
# P = price

# def JL( D ):
#     return D / 100

def PriceCut( P ):
    return lambda JL : JL/100 * P