import unittest
from solve_polynomial import solve, validate, InputError

class SolverTests(unittest.TestCase):
    def assert_roots(self, n, coeffs, expected, places=6):
        result=solve(n,coeffs)
        self.assertEqual(result['number_of_roots_with_multiplicity'],n)
        values=[]
        for r in result['roots']:
            self.assertLess(r['normalized_residual'],1e-10)
            values.extend([complex(r['real'],r['imag'])]*r['multiplicity'])
        self.assertEqual(len(values),len(expected))
        for a,b in zip(sorted(values,key=lambda z:(z.real,z.imag)),sorted(expected,key=lambda z:(z.real,z.imag))):
            self.assertAlmostEqual(a.real,b.real,places=places)
            self.assertAlmostEqual(a.imag,b.imag,places=places)
    def test_linear(self):self.assert_roots(1,['2','-4'],[2])
    def test_quadratic_real(self):self.assert_roots(2,['1','-5','6'],[2,3])
    def test_quadratic_complex(self):self.assert_roots(2,['1','0','1'],[-1j,1j])
    def test_triple_root(self):self.assert_roots(3,['1','-3','3','-1'],[1,1,1])
    def test_quartic(self):self.assert_roots(4,['1','0','-5','0','4'],[-2,-1,1,2])
    def test_fraction(self):self.assert_roots(1,['1/2','-1/4'],[0.5])
    def test_decimal(self):self.assert_roots(1,['0.5','-1.25'],[2.5])
    def test_degree_five(self):self.assert_roots(5,['1','0','0','0','0','-1'],[1,complex(-.8090169944,.5877852523),complex(-.8090169944,-.5877852523),complex(.3090169944,.9510565163),complex(.3090169944,-.9510565163)])
    def test_degree_eight(self):self.assertEqual(solve(8,['1','0','0','0','0','0','0','0','-1'])['number_of_roots_with_multiplicity'],8)
    def test_exact_quadratic(self):self.assertIsNotNone(solve(2,['1','-5','6'])['exact_roots_if_available'])
    def test_zero_leading(self):
        with self.assertRaises(InputError):solve(2,['0','1','1'])
    def test_bad_count(self):
        with self.assertRaises(InputError):solve(3,['1','2'])
    def test_bad_degree(self):
        for n in (0,-1,21,1.5,'2',True):
            with self.subTest(n=n),self.assertRaises(InputError):validate(n,['1','2'])
    def test_fraction_div_zero(self):
        with self.assertRaises(InputError):solve(1,['1/0','2'])
    def test_bad_literal(self):
        for x in ('NaN','inf','x','1+2','1j','1e10'):
            with self.subTest(x=x),self.assertRaises(InputError):solve(1,['1',x])
    def test_bool_coeff(self):
        with self.assertRaises(InputError):solve(1,[True,'2'])
    def test_float_json(self):
        with self.assertRaises(InputError):solve(1,[1.0,'2'])
    def test_root_multiplicity(self):
        v=solve(4,['1','-4','6','-4','1'])
        self.assertEqual(len(v['roots']),1)
        self.assertEqual(v['roots'][0]['multiplicity'],4)
    def test_no_constant(self):self.assert_roots(2,['1','0','0'],[0,0])

if __name__=='__main__': unittest.main()
