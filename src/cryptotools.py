class CryptoTools(object):

    # returns the gcd() of 2 numbers
    def gcd(self, x, n):
        if x < n:
            x, n = n, x
        
        if n == 0:
            return x
        else:
            return CryptoTools.gcd(self, n, x % n)

    # returns the inverse of 2 numbers
    def inverse(self, x, n, showTable=None):
        qi = [0]
        ri = []
        si = [1, 0]
        ti = [0, 1]
        i = 1
        i_count = [0, 1]

        while x != 0:
            i += 1
            i_count.append(i)

            q = n // x
            qi.append(q)

            n, x = x, n % x
            ri.append(x)

            s = si[i_count[i-2]] - qi[i_count[i-1]] * si[i_count[i-1]]
            si.append(s)

            t = ti[i_count[i-2]] - qi[i_count[i-1]] * ti[i_count[i-1]]
            ti.append(t)

        i_count = i_count[2:]
        qi = qi[1:]
        si = si[2:]
        ti = ti[2:]
        
        if showTable is not None:
            print('{0: ^5}'.format('i'), '{0: ^5}'.format('qi-1'), '{0: ^5}'.format('ri'), '{0: ^5}'.format('si'), '{0: ^5}'.format('ti'))
            print('{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'), '{0: ^5}'.format('-----'))
            for k in range(len(i_count)):
                print('{0: ^5}'.format(i_count[k]), '{0: ^5}'.format(qi[k]), '{0: ^5}'.format(ri[k]), '{0: ^5}'.format(si[k]), '{0: ^5}'.format(ti[k]))
        
            print('\ninverse:', ti[len(ti)-2])
            return None

        return ti[len(ti)-2]

    # returns the result of the SQ / Mult of an exponent
    def sq_mult(self, x, e, m):
        org_e = e
        e = bin(e)[3:]
        ops = []
        result = []
        result.append(x)
        org_x = x
        binary = [1]
        exp = '1'
        exp_list = []
        print('Steps to solve', x, '^', org_e, 'mod', m)
        for i in e:
            binary.append(int(i))
            if int(i) == 0:
                ops.append('SQR')
                if x > m:
                    print(x, '%', m, '=', x%m)
                    x = x % m
                x_tmp = x
                x = x**2
                print(x_tmp, 'squared =', x)
                result.append(x % m)
                exp = exp + '0'
                exp_list.append(exp)
            else:
                ops.append('SQR')
                if x > m:
                    print(x, '%', m, '=', x%m)
                    x = x % m
                x_tmp = x
                x = x**2
                print(x_tmp, 'squared =', x)
                result.append(x % m)
                x_tmp = x % m
                exp = exp + '0'
                exp_list.append(exp)

                ops.append('MULT')
                if x > m:
                    print(x, '%', m, '=', x%m)
                    x = x % m
                x_tmp = x
                x = x * org_x
                print(x_tmp, 'x', org_x, '=', x)
                result.append(x % m)
                exp = exp[:-1]
                exp = exp + '1'
                exp_list.append(exp)

        result = result[1:]

        print()  
        print('{0: ^8}'.format('Binary'), '{0: ^12}'.format('Operation'), '{0: ^}'.format('Result'))
        for k in range(len(ops)):
            print('{0:<12}'.format(exp_list[k]), '{0:^4}'.format(ops[k]), '{0:>8}'.format(result[k]))

    # returns the encrypt & decrpyt values for RSA
    def rsa(self, p, q, e, x):
        p = int(p)
        q = int(q)
        e = int(e)
        x = int(x)
        n = p * q
        phi_n = (p-1) * (q-1)

        d = CryptoTools.inverse(self, e, phi_n)
        if d < 0:
            d = phi_n + d

        y = x ** e % n
        x = y ** d % n

        print('Results of RSA with the given values: p =', p, 'q =', q, 'e or d =', e, 'x =', x)
        print('{0: >10}'.format('n ='), '{0: <5}'.format(n))
        print('{0: >10}'.format('phi_n ='), '{0: <5}'.format(phi_n))
        print('{0: >10}'.format('e or d ='), '{0: <5}'.format(e))
        print('{0: >10}'.format('e or d ='), '{0: <5}'.format(d))
        print('{0: >10}'.format('x ='), '{0: <5}'.format(x))
        print('{0: >10}'.format('y ='), '{0: <5}'.format(y))

    # returns all of the values for CRT
    def crt(self, p, q, e, y):
        p = int(p)
        q = int(q)
        e = int(e)
        y = int(y)
        n = p * q
        phi_n = (p-1) * (q-1)

        d = CryptoTools.inverse(self, e, phi_n)
        if d < 0:
            d = phi_n + d

        dp = d % (p-1)
        dq = d % (q-1)

        cp = CryptoTools.inverse(self, q, p)
        if cp < 0:
            cp = cp + p

        cq = CryptoTools.inverse(self, p, q)
        if cq < 0:
            cq = cq + q
            
        yp = y % p
        yq = y % q

        xp = yp ** dp % p
        xq = yq ** dq % q

        x = y ** d % n

        print('Results of CRT with the given values: p =', p, 'q =', q, 'e =', e, 'y =', y)
        print('{0: >10}'.format('p ='), '{0: <5}'.format(p), '{0: >10}'.format('q ='), '{0: <5}'.format(q))
        print('{0: >10}'.format('n ='), '{0: <5}'.format(n), '{0: >10}'.format('phi_n ='), '{0: <5}'.format(phi_n))
        print('{0: >10}'.format('x ='), '{0: <5}'.format(x),'{0: >10}'.format('y ='), '{0: <5}'.format(y))
        print('{0: >10}'.format('e ='), '{0: <5}'.format(e), '{0: >10}'.format('d ='), '{0: <5}'.format(d))
        print('{0: >10}'.format('dp ='), '{0: <5}'.format(dp), '{0: >10}'.format('dq ='), '{0: <5}'.format(dq))
        print('{0: >10}'.format('cp ='), '{0: <5}'.format(cp), '{0: >10}'.format('cq ='), '{0: <5}'.format(cq))
        print('{0: >10}'.format('yp ='), '{0: <5}'.format(yp), '{0: >10}'.format('yq ='), '{0: <5}'.format(yq))
        print('{0: >10}'.format('xp ='), '{0: <5}'.format(xp), '{0: >10}'.format('xq ='), '{0: <5}'.format(xq))
