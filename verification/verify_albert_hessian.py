"""Independent verification of the Albert determinant's rank-one and rank-two Hessians.

At diagonal rank representatives, the octonion triple product has no quadratic
term; each of the three octonion norms is a nondegenerate 8D quadratic form.
Thus setting n(v)=sum(v_i^2) and omitting the triple product preserves the
full Hessian at both representatives (over characteristic zero).
"""
import sympy as s

a,b,c=s.symbols('a b c')
X=s.symbols('X0:8');Y=s.symbols('Y0:8');Z=s.symbols('Z0:8')
w=(a,b,c,*X,*Y,*Z)
N=a*b*c-a*sum(x*x for x in X)-b*sum(y*y for y in Y)-c*sum(z*z for z in Z)
M=s.hessian(N,w)
assert len(w)==27
for name,point,expected in [('rank-one',{a:1,b:0,c:0},10),('rank-two',{a:1,b:1,c:0},18)]:
    H=M.subs({**dict.fromkeys((*X,*Y,*Z),0),**point})
    rank=H.rank()
    assert rank==expected, f'{name}: expected {expected}, got {rank}'
    print(name,'Hessian rank',rank,'radical dimension',27-rank)
print('PASS Albert Hessian rank bounds underlying the F4 norm-one reduction')
