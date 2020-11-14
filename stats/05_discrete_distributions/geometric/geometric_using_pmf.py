




'''
Geometric Distr
- models the number of failures up to the first success
    - two formulas
        - up to but not including the first success
        - up to and including the first success
'''

# 0000001
# 001
# 00000000000000001


'''
Write the geometric_pmf function
3 parameters
p : probability
k : number of failures (inclusive or exclusive of the 1st success)
inclusive=True : whether or not to use the inclusive or exclusive form
'''
def geometric_pmf(p, k, inclusive=True):
    if inclusive:
        return p * (1-p)**(k-1)
    else:
        return p * (1-p)**k

