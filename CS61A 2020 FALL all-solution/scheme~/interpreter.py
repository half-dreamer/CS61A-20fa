from __future__ import print_function as o77sUl
import code as l95_1_2a_
import functools as TPzgXc5__
import inspect as r8C7
import re as Ugph89M
import signal as NC_2
import sys as q_5Yqs
import math as f2c150
import sys as q_5Yqs
import numbers as N76GD
import builtins as W1N6K_h
import math as f2c150
import numbers as N76GD
import operator as BP13
import sys as q_5Yqs
import builtins as W1N6K_h
import itertools as Bk0H7_hpl
import string as string
import sys as q_5Yqs
import tokenize as N23r1
import sys as q_5Yqs
import builtins as W1N6K_h
'gFH_20_D_84T4uB6a2hy'

def CIbm_44(sNGCB1__):
    'PvVx_7X8S12Q9526863C_46l4'
    if (r8C7.stack()[(((-119 + 59) + (-73 + 78)) + ((-19 + 43) + (80 + -48)))][int(((-0.8184473675842888 + 0.9569014433666674) * int((0.012262271439731465 * 0))))].f_locals[((('' + '__') + ('n' + 'a')) + (('' + 'me_') + chr(95)))] == ('_' + (('_m' + 'a') + ('in' + '__')))):
        yyD8610o7 = q_5Yqs.argv[(((-127 + 9) + (83 + -37)) + ((68 + 6) + (-21 + 20))):]
        sNGCB1__(*yyD8610o7)
    return sNGCB1__
zWw702843 = str()

def Kep786p(sNGCB1__):
    'x77V6P628ZJ7_o0208_53_OQ885'

    @TPzgXc5__.wraps(sNGCB1__)
    def M_3u2iF(*yyD8610o7, **w6a178):
        global zWw702843
        uA6__s = [repr(o3az1w_5) for o3az1w_5 in yyD8610o7]
        uA6__s += [((repr(O5IV9_X_) + chr(((38 + -21) + (-44 + 88)))) + repr(q5__)) for (O5IV9_X_, q5__) in w6a178.items()]
        X2O1yr_47(((chr((23 + 100)) + (('0' + '}({1') + ('}' + ')'))).format(sNGCB1__.__name__, (chr((-36 + 80)) + chr((36 + -4))).join(uA6__s)) + chr((114 + -56))))
        zWw702843 += ((chr(32) + ' ') + (chr(32) + chr(32)))
        try:
            nX1h86l7A = sNGCB1__(*yyD8610o7, **w6a178)
            zWw702843 = zWw702843[:(- (((121 + -51) + (-37 + -24)) + ((-89 + 13) + (73 + -2))))]
        except Exception as o3az1w_5:
            X2O1yr_47((sNGCB1__.__name__ + ((chr(32) + ('exited' + ' via excepti')) + ('' + ('' + 'on')))))
            zWw702843 = zWw702843[:(- (((177 + -43) + (-55 + -28)) + ((-112 + -31) + (142 + -46))))]
            raise
        X2O1yr_47((('' + ('{' + '0')) + (('}({' + '1}) ->') + (' ' + '{2}'))).format(sNGCB1__.__name__, (str() + (str() + (',' + ' '))).join(uA6__s), nX1h86l7A))
        return nX1h86l7A
    return M_3u2iF

def X2O1yr_47(nbt47):
    'hz2__x5aL5261728__9668__62_M'
    print((zWw702843 + Ugph89M.sub(chr((52 + -42)), (chr(((43 + 2) + (-82 + 47))) + zWw702843), str(nbt47))))

def M1DZk():
    'W10D8Oa0l40Up995527lXq11'
    u_5_f99B = r8C7.stack()[(((53 + -58) + (4 + -1)) + ((-83 + -2) + (67 + 21)))]
    X2O1yr_47(((('C' + 'u') + ('rrent li' + 'ne')) + (str() + (': File "{f[1]' + '}", line {f[2]}, in {f[3]}'))).format(f=u_5_f99B))

def s54G_vpl(P_7tpp45=None):
    'sv4___135K7Poe_4N6W3'
    u_5_f99B = r8C7.currentframe().f_back
    B___ = u_5_f99B.f_globals.copy()
    B___.update(u_5_f99B.f_locals)

    def R0Z_O__3T(signum, u_5_f99B):
        print()
        exit(int((0.6011260521409377 * 0)))
    NC_2.signal(NC_2.SIGINT, R0Z_O__3T)
    if (not P_7tpp45):
        (z1fd, KB41_V_u, h825J958A, z1fd, z1fd, z1fd) = r8C7.stack()[(((34 + -62) + (5 + -63)) + ((121 + 12) + (21 + -67)))]
        P_7tpp45 = (('' + ('I' + 'n')) + (('teractin' + 'g at File "{') + ('0}", line {1} ' + '\n'))).format(KB41_V_u, h825J958A)
        P_7tpp45 += ((('    ' + 'Unix:    <') + ('Control>-D continues' + ' the ')) + (('' + 'progra') + ('m; ' + '\n')))
        P_7tpp45 += ((('' + '  ') + ('  ' + 'Windows:')) + ('' + (' <Control>-Z <Enter> con' + 'tinues the program; \n')))
        P_7tpp45 += ((('' + '    ') + 'e') + (('' + 'xit() o') + ('r <Control>-C exits the pro' + 'gram')))
    l95_1_2a_.interact(P_7tpp45, None, B___)
'TI_12__y65_7_9G_9C6rS_'
if (q_5Yqs.version_info[int(((0.4066688947305519 + 0.06014510801664463) * 0))] < (((67 + -19) + (-15 + 5)) + ((-89 + 74) + (57 + -77)))):

    def input(X9x__y_):
        q_5Yqs.stderr.write(X9x__y_)
        q_5Yqs.stderr.flush()
        h825J958A = q_5Yqs.stdin.readline()
        if (not h825J958A):
            raise EOFError()
        return h825J958A.rstrip((str() + ('' + ('\r' + '\n'))))

class G_h1Y3e0L(object):
    'i65_zu5u0SA98J5_U6746'

    def __init__(h1gg_0, H4__):
        h1gg_0.index = int(((0.7436170240396914 + 0.05431776276322309) * 0))
        h1gg_0.TEu594 = []
        h1gg_0.H4__ = H4__
        h1gg_0.current_line = ()
        h1gg_0.current()

    def pZ5s(h1gg_0):
        'i7Bg_o_S0_9e8M2E_1T__fP_455kL'
        current = h1gg_0.current()
        h1gg_0.index += (((90 + 21) + (-123 + 24)) + ((104 + -73) + (-4 + -38)))
        return current

    def current(h1gg_0):
        'qy07f_8K_3VZ0983b_1e_73__1G8'
        while (not h1gg_0.rsvx9R):
            h1gg_0.index = int((((0.06516192828476008 + 0.6691065459099526) + (-0.8772331062851101 + 0.9367331080007477)) * 0))
            try:
                h1gg_0.current_line = next(h1gg_0.H4__)
                h1gg_0.TEu594.append(h1gg_0.current_line)
            except StopIteration:
                h1gg_0.current_line = ()
                return None
        return h1gg_0.current_line[h1gg_0.index]

    @property
    def rsvx9R(h1gg_0):
        return (h1gg_0.index < len(h1gg_0.current_line))

    def __str__(h1gg_0):
        'biK_393D4M013Gp45h62UU05'
        U_t__5__7 = len(h1gg_0.TEu594)
        P_7tpp45 = ((('{' + (('0' + ':') + chr(62))) + str((f2c150.floor(f2c150.log10(U_t__5__7)) + (((-26 + -86) + (-19 + 80)) + ((94 + 17) + (30 + -89)))))) + ((str() + ('}' + ':')) + chr((-18 + 50))))
        R14t_l93D = ''
        for T5Q71_U_ in range(max(int(((-0.0814970546874233 + 0.48024603825884116) * int((0.40418206247649413 * 0)))), (U_t__5__7 - (((-73 + 89) + (-53 + 54)) + ((90 + -23) + (-136 + 56))))), (U_t__5__7 - (((-140 + 94) + (34 + -41)) + ((-14 + -7) + (87 + -12))))):
            R14t_l93D += ((P_7tpp45.format((T5Q71_U_ + (((4 + -16) + (17 + -16)) + ((-17 + 62) + (-13 + -20))))) + chr(((54 + -7) + (-18 + 3))).join(map(str, h1gg_0.TEu594[T5Q71_U_]))) + chr((51 + -41)))
        R14t_l93D += P_7tpp45.format(U_t__5__7)
        R14t_l93D += chr(((-79 + 87) + (-70 + 94))).join(map(str, h1gg_0.current_line[:h1gg_0.index]))
        R14t_l93D += ((chr(32) + chr(62)) + ('>' + ' '))
        R14t_l93D += chr(32).join(map(str, h1gg_0.current_line[h1gg_0.index:]))
        return R14t_l93D.strip()
try:
    import readline as Ia_H
except:
    pass

class T_g66l8(object):
    'L3P64o_ckt_764vYu_v_9946m'

    def __init__(h1gg_0, X9x__y_):
        h1gg_0.X9x__y_ = X9x__y_

    def __iter__(h1gg_0):
        while True:
            (yield input(h1gg_0.X9x__y_))
            h1gg_0.X9x__y_ = (chr((-57 + 89)) * len(h1gg_0.X9x__y_))

class McE513D_(object):
    'kH50_Xy8_62hC_6o9sY5'

    def __init__(h1gg_0, TEu594, X9x__y_, DgQZ78=';'):
        h1gg_0.TEu594 = TEu594
        h1gg_0.X9x__y_ = X9x__y_
        h1gg_0.DgQZ78 = DgQZ78

    def __iter__(h1gg_0):
        while h1gg_0.TEu594:
            h825J958A = h1gg_0.TEu594.pop(int((((-0.9077564454578811 + 0.5222880132479137) + (-0.0581229065835952 + 0.9470279900565965)) * int(((-0.05311702756935288 + 0.4627087314802689) * int((0.8332477592558166 * 0))))))).strip(chr(((-31 + -16) + (50 + 7))))
            if ((h1gg_0.X9x__y_ is not None) and (h825J958A != str()) and (not h825J958A.lstrip().startswith(h1gg_0.DgQZ78))):
                print((h1gg_0.X9x__y_ + h825J958A))
                h1gg_0.X9x__y_ = (chr(((112 + -15) + (-139 + 74))) * len(h1gg_0.X9x__y_))
            (yield h825J958A)
        raise EOFError
't446t49_R_86pS_9I1ni_T21s3AV0'

class Pair(object):
    'V6_G583_R5c204kZ_0j_vO_10'

    def __init__(h1gg_0, g_7033293, rp4nk2Mm):
        if ((not W1N6K_h.DOTS_ARE_CONS) and (not lKa4b11c7(rp4nk2Mm))):
            print(rp4nk2Mm, type(rp4nk2Mm).__name__)
            raise E_VH(((('cdr c' + 'an') + (' only be a pair, nil, or a promise but ' + 'was')) + (str() + (' {' + '}'))).format(rp4nk2Mm))
        h1gg_0.g_7033293 = g_7033293
        h1gg_0.rp4nk2Mm = rp4nk2Mm

    def __repr__(h1gg_0):
        return ((('Pair({' + '0') + ('},' + ' {')) + ('' + ('' + '1})'))).format(repr(h1gg_0.g_7033293), repr(h1gg_0.rp4nk2Mm))

    def __str__(h1gg_0):
        R14t_l93D = (chr(40) + repl_str(h1gg_0.g_7033293))
        rp4nk2Mm = h1gg_0.rp4nk2Mm
        while isinstance(rp4nk2Mm, Pair):
            R14t_l93D += (' ' + repl_str(rp4nk2Mm.g_7033293))
            rp4nk2Mm = rp4nk2Mm.rp4nk2Mm
        if (rp4nk2Mm is not nil):
            R14t_l93D += ((str() + (' ' + ('' + '. '))) + repl_str(rp4nk2Mm))
        return (R14t_l93D + chr(((166 + -63) + (-134 + 72))))

    def __len__(h1gg_0):
        (U_t__5__7, rp4nk2Mm) = ((((-106 + 80) + (-52 + 80)) + ((1 + 12) + (-41 + 27))), h1gg_0.rp4nk2Mm)
        while isinstance(rp4nk2Mm, Pair):
            U_t__5__7 += (((18 + 24) + (35 + -54)) + ((-184 + 77) + (49 + 36)))
            rp4nk2Mm = rp4nk2Mm.rp4nk2Mm
        if (rp4nk2Mm is not nil):
            raise TypeError(((('l' + 'ength attempt') + ('ed on improper li' + 's')) + 't'))
        return U_t__5__7

    def __eq__(h1gg_0, qT71):
        if (not isinstance(qT71, Pair)):
            return False
        return ((h1gg_0.g_7033293 == qT71.g_7033293) and (h1gg_0.rp4nk2Mm == qT71.rp4nk2Mm))

    def map(h1gg_0, sNGCB1__):
        'KG_eHyU9121ow5f_dVLIrNSoh8M'
        RJ2_T1T = sNGCB1__(h1gg_0.g_7033293)
        if ((h1gg_0.rp4nk2Mm is nil) or isinstance(h1gg_0.rp4nk2Mm, Pair)):
            return Pair(RJ2_T1T, h1gg_0.rp4nk2Mm.map(sNGCB1__))
        else:
            raise TypeError(((('ill' + '-formed ') + ('l' + 'i')) + (('s' + 't') + (' (cdr is a pro' + 'mise)'))))

    def Nc_c61_(h1gg_0, sNGCB1__):
        'I97DY_O_80_65MdnU9D9k430w'
        RJ2_T1T = sNGCB1__(h1gg_0.g_7033293)
        if ((h1gg_0.rp4nk2Mm is nil) or isinstance(h1gg_0.rp4nk2Mm, Pair)):
            return F5HAi_Iv_(RJ2_T1T, h1gg_0.rp4nk2Mm.Nc_c61_(sNGCB1__))
        else:
            raise TypeError(((('ill-formed list (c' + 'd') + ('r' + ' i')) + (('' + 's a pro') + ('m' + 'ise)'))))

class nil(object):
    'la_sqtZ6jDuOuga_T6_79o'

    def __repr__(h1gg_0):
        return (('' + ('n' + 'i')) + chr((123 + -15)))

    def __str__(h1gg_0):
        return (str() + (str() + ('(' + ')')))

    def __len__(h1gg_0):
        return int((((-0.36019798824651594 + 0.42687550643887395) + (-0.3414590858236136 + 0.4697875930622135)) * 0))

    def map(h1gg_0, sNGCB1__):
        return h1gg_0

    def Nc_c61_(h1gg_0, sNGCB1__):
        return h1gg_0
nil = nil()
O83A5 = {chr(((-31 + 74) + (11 + -15))): (str() + (chr(113) + ('' + 'uote'))), chr(((81 + -10) + (-23 + 48))): ((chr(113) + ('uasi' + 'qu')) + (('o' + 't') + 'e')), (str() + (chr(44) + '@')): (('' + ('u' + 'nqu')) + (('ote-s' + 'p') + ('lici' + 'ng'))), chr(((119 + 22) + (-116 + 19))): ('u' + (str() + ('' + 'nquote')))}

def FkZs_2_1(D_gy_7):
    'h9G___298lacXb550SV_6Nz6gl'
    if (D_gy_7.current() is None):
        raise EOFError
    B9_7F40b = D_gy_7.pZ5s()
    if (B9_7F40b == (str() + (('' + 'ni') + chr(108)))):
        return nil
    elif (B9_7F40b in set((str() + (chr(40) + '[')))):
        if (D_gy_7.current() == chr(((-26 + 85) + (44 + -57)))):
            raise SyntaxError(((str() + ('.' + ' ca')) + (('nnot be the first token ' + 'in ') + ('a ' + 'list'))))
        return Sf__Qr(D_gy_7, B9_7F40b, {chr((40 + 0)): chr(41), chr((81 + 10)): chr(((52 + -8) + (145 + -96)))}[B9_7F40b])
    elif (B9_7F40b in O83A5):
        return Pair(O83A5[B9_7F40b], Pair(FkZs_2_1(D_gy_7), nil))
    elif (B9_7F40b not in BR87HY_4):
        return B9_7F40b
    else:
        raise SyntaxError(((str() + ('unexp' + 'ected ')) + ('t' + ('oken' + ': {0}'))).format(B9_7F40b))

def Sf__Qr(D_gy_7, AQ9Ak='(', Qh_c83=')'):
    'dI55900294A3_4473_H_143F_fET6'
    try:
        if (D_gy_7.current() is None):
            raise SyntaxError(((str() + ('unexpe' + 'cte')) + (('d' + ' en') + ('d of fi' + 'le'))))
        elif (D_gy_7.current() in set((chr((24 + 17)) + chr(93)))):
            if (D_gy_7.current() != Qh_c83):
                raise SyntaxError(((('Exp' + 'ected {} ') + ('to match with' + ' {} bu')) + (('t go' + 't ') + ('' + '{}'))).format(Qh_c83, AQ9Ak, D_gy_7.current()))
            D_gy_7.pZ5s()
            return nil
        elif (D_gy_7.current() == chr(((-8 + -20) + (119 + -45)))):
            D_gy_7.pZ5s()
            U44x2 = FkZs_2_1(D_gy_7)
            if (D_gy_7.current() is None):
                raise SyntaxError(((('' + 'une') + ('xpected e' + 'nd ')) + ('o' + ('f fil' + 'e'))))
            if (D_gy_7.pZ5s() != chr(((24 + 98) + (-19 + -62)))):
                raise SyntaxError(((('expected on' + 'e ') + ('eleme' + 'nt a')) + (('ft' + 'er') + ('' + ' .'))))
            if W1N6K_h.DOTS_ARE_CONS:
                return U44x2
            else:
                return Pair(Pair(((chr(118) + chr(97)) + (('ria' + 'd') + ('i' + 'c'))), Pair(U44x2, nil)), nil)
        else:
            g_7033293 = FkZs_2_1(D_gy_7)
            rp4nk2Mm = Sf__Qr(D_gy_7, AQ9Ak, Qh_c83)
            return Pair(g_7033293, rp4nk2Mm)
    except EOFError:
        raise SyntaxError((('' + ('unexpecte' + 'd en')) + (('d of f' + 'i') + ('' + 'le'))))

def I_1NZ10(X9x__y_='scm> '):
    'p5y8J8_sq_8__0ud88__J6_c94'
    return G_h1Y3e0L(f89CMz8vf(T_g66l8(X9x__y_)))

def H41634F7(TEu594, X9x__y_='scm> ', l__x3d=False):
    'J0M713_hE_8_3I05225_8z62aOh_n'
    if l__x3d:
        V382_46 = TEu594
    else:
        V382_46 = McE513D_(TEu594, X9x__y_)
    return G_h1Y3e0L(f89CMz8vf(V382_46))

def BV34_x(h825J958A):
    'QIQ6x29v1678g_lR08525__9R2_'
    b9w6r_ = G_h1Y3e0L(f89CMz8vf([h825J958A]))
    nX1h86l7A = FkZs_2_1(b9w6r_)
    if b9w6r_.rsvx9R:
        raise SyntaxError(((('r' + 'e') + ('a' + 'd')) + (("_line's argument can only be a sin" + 'g') + ('' + 'le element, but received multiple'))))
    return nX1h86l7A

def repl_str(B9_7F40b):
    'SkiUc_F6N0J761tDV71TY6C8W3g_7'
    if (B9_7F40b is True):
        return ('#' + chr(116))
    if (B9_7F40b is False):
        return (str() + ('#' + chr(102)))
    if (B9_7F40b is None):
        return ((str() + ('u' + 'ndefine')) + chr((149 + -49)))
    if (isinstance(B9_7F40b, N76GD.Number) and (not isinstance(B9_7F40b, N76GD.Integral))):
        return repr(B9_7F40b)
    return str(B9_7F40b)

def Gk3_YW329():
    'S8_u34T_9_1__J__7__8_1'
    while True:
        try:
            D_gy_7 = I_1NZ10(((str() + ('re' + 'ad')) + (str() + ('' + '> '))))
            while D_gy_7.rsvx9R:
                vQ1g4I__0 = FkZs_2_1(D_gy_7)
                if (vQ1g4I__0 == (str() + (chr(101) + ('' + 'xit')))):
                    print()
                    return
                print((chr(115) + (('t' + 'r') + ('' + ' :'))), vQ1g4I__0)
                print(('' + (('' + 're') + ('pr' + ':'))), repr(vQ1g4I__0))
        except (SyntaxError, ValueError) as Ai5C8:
            print((type(Ai5C8).__name__ + chr(((149 + 5) + (-77 + -19)))), Ai5C8)
        except (KeyboardInterrupt, EOFError):
            print()
            return

def CIbm_44(*yyD8610o7):
    if (len(yyD8610o7) and ((('' + ('--' + 'r')) + ('e' + ('p' + 'l'))) in yyD8610o7)):
        Gk3_YW329()
'pX7aiJ658Cn99_Jn1dzwuHF8f7'

class E_VH(Exception):
    'S6_1_338jD5c__p21I__zy_22'
C3m_ = []

def lRyIV_K4(*y_R9365):
    'h63_1J00lWI29A_c_7YP3j4w'

    def add(sNGCB1__):
        for t8_33E__ in y_R9365:
            C3m_.append((t8_33E__, sNGCB1__, y_R9365[int((((0.15987500453505044 + 0.5130814474261818) + (-0.9241462208231203 + 0.9456822188307696)) * int(((0.47034996329596135 + 0.11597798132387449) * 0))))]))
        return sNGCB1__
    return add

def QI0_kY(B9_7F40b, NL_y0H, O5IV9_X_, t8_33E__):
    'yT7i7IQD_s1yEyc8Dfb8iiLe_eM'
    if (not NL_y0H(B9_7F40b)):
        P_7tpp45 = ((chr(97) + ('rgument {0} of {1}' + ' has wrong type ({2')) + ('}' + chr(41)))
        pJp2 = type(B9_7F40b).__name__
        if s600(B9_7F40b):
            pJp2 = ((('sy' + 'm') + 'b') + (chr(111) + 'l'))
        raise E_VH(P_7tpp45.format(O5IV9_X_, t8_33E__, pJp2))
    return B9_7F40b

@lRyIV_K4((str() + (('bo' + 'o') + ('lean' + '?'))))
def zdE__4g9(szU6w57):
    return ((szU6w57 is True) or (szU6w57 is False))

def u05_4S8(B9_7F40b):
    'q_3y441_P9_9Ig5_k_R9'
    return (B9_7F40b is not False)

def zB2j3Q8_(B9_7F40b):
    'cwD45_RfVX7Y1z9_8_352_9L7Eh'
    return (B9_7F40b is False)

@lRyIV_K4(('n' + ('' + ('o' + 't'))))
def oFlD9k226(szU6w57):
    return (not u05_4S8(szU6w57))

@lRyIV_K4((chr((185 + -84)) + (('' + 'qua') + ('l' + '?'))))
def aZ_A2sa_4(szU6w57, M_8fT_l7):
    if (NA_lk(szU6w57) and NA_lk(M_8fT_l7)):
        return (aZ_A2sa_4(szU6w57.g_7033293, M_8fT_l7.g_7033293) and aZ_A2sa_4(szU6w57.rp4nk2Mm, M_8fT_l7.rp4nk2Mm))
    elif (M9QsCem(szU6w57) and M9QsCem(M_8fT_l7)):
        return (szU6w57 == M_8fT_l7)
    else:
        return ((type(szU6w57) == type(M_8fT_l7)) and (szU6w57 == M_8fT_l7))

@lRyIV_K4((str() + (('e' + 'q') + chr(63))))
def q684_84(szU6w57, M_8fT_l7):
    if (M9QsCem(szU6w57) and M9QsCem(M_8fT_l7)):
        return (szU6w57 == M_8fT_l7)
    elif (s600(szU6w57) and s600(M_8fT_l7)):
        return (szU6w57 == M_8fT_l7)
    else:
        return (szU6w57 is M_8fT_l7)

@lRyIV_K4(((chr(112) + ('ai' + 'r')) + chr((162 + -99))))
def NA_lk(szU6w57):
    return (type(szU6w57).__name__ == (str() + (('' + 'Pai') + 'r')))

@lRyIV_K4(((('scheme-v' + 'al') + 'i') + (('' + 'd-') + ('cdr' + '?'))))
def lKa4b11c7(szU6w57):
    return (NA_lk(szU6w57) or N5vQ20(szU6w57) or u312__A_5(szU6w57))

@lRyIV_K4((str() + ('p' + ('ro' + 'mise?'))))
def u312__A_5(szU6w57):
    return (type(szU6w57).__name__ == (('P' + 'r') + (('omi' + 's') + chr(101))))

@lRyIV_K4((chr((116 + -14)) + ('o' + ('' + 'rce'))))
def I1_I_04P6(szU6w57):
    QI0_kY(szU6w57, u312__A_5, int((0.5151389876216892 * 0)), ((('' + 'pr') + ('omi' + 's')) + chr((74 + 27))))
    return szU6w57.H_7_31_()

@lRyIV_K4((('c' + ('dr' + '-st')) + (chr(114) + ('e' + 'am'))))
def C232B85T2(szU6w57):
    QI0_kY(szU6w57, (lambda szU6w57: (NA_lk(szU6w57) and u312__A_5(szU6w57.rp4nk2Mm))), int((((-0.45548544657896595 + 0.02259361771294177) + (-0.16794467204218355 + 0.9752736273627003)) * int(((0.00444766277475217 + 0.02930109226494748) * int((0.1605161555228808 * 0)))))), (chr((133 + -34)) + (('dr-st' + 'r') + ('e' + 'am'))))
    return I1_I_04P6(szU6w57.rp4nk2Mm)

@lRyIV_K4(((('' + 'nul') + chr(108)) + '?'))
def N5vQ20(szU6w57):
    return (type(szU6w57).__name__ == (str() + ('n' + ('i' + 'l'))))

@lRyIV_K4((('l' + ('' + 'is')) + (str() + ('' + 't?'))))
def hB97uMMe3(szU6w57):
    'MSH05198f8_d71kb2Z224D1a1'
    while (szU6w57 is not nil):
        if (not isinstance(szU6w57, Pair)):
            return False
        szU6w57 = szU6w57.rp4nk2Mm
    return True

@lRyIV_K4(('' + (('l' + 'e') + ('n' + 'gth'))))
def Q_i987(szU6w57):
    QI0_kY(szU6w57, hB97uMMe3, int(((0.5536255537088202 + 0.08510615114349618) * 0)), (str() + (chr(108) + ('' + 'ength'))))
    if (szU6w57 is nil):
        return int((((-0.990120274279149 + 0.716890304652938) + (0.32934270105362196 + 0.5157299132031907)) * int(((0.03541625720874786 + 0.765204158409574) * int((0.19024527087419707 * 0))))))
    return len(szU6w57)

@lRyIV_K4((('' + ('' + 'con')) + chr((189 + -74))))
def M5_8uB(szU6w57, M_8fT_l7):
    return Pair(szU6w57, M_8fT_l7)

@lRyIV_K4((chr((27 + 72)) + (chr(97) + 'r')))
def Y_2l(szU6w57):
    QI0_kY(szU6w57, NA_lk, int(((-0.5281946773379047 + 0.6040804290851023) * int((0.6808746478784761 * 0)))), ((chr(99) + 'a') + chr((84 + 30))))
    return szU6w57.g_7033293

@lRyIV_K4((str() + (('' + 'cd') + chr(114))))
def T8ZIR_H4(szU6w57):
    QI0_kY(szU6w57, NA_lk, int((((-0.5243144935271634 + 0.43991950061844476) + (-0.12175343490967994 + 0.6361383010428399)) * int((0.7552720258144116 * 0)))), ('c' + (str() + ('d' + 'r'))))
    return szU6w57.rp4nk2Mm

@lRyIV_K4(('s' + (str() + ('et-' + 'car!'))))
def Y34_0(szU6w57, M_8fT_l7):
    QI0_kY(szU6w57, NA_lk, int((((-0.38868344114303854 + 0.4280732410236311) + (0.004973499182824415 + 0.18581928372103507)) * int(((-0.8026379827901294 + 0.9216184470805058) * int((0.24802243213101005 * 0)))))), (str() + (('se' + 't') + ('-ca' + 'r!'))))
    szU6w57.g_7033293 = M_8fT_l7

@lRyIV_K4((str() + ('' + ('set-cdr' + '!'))))
def Jn_17LN(szU6w57, M_8fT_l7):
    QI0_kY(szU6w57, NA_lk, int((((-0.9788397619785092 + 0.47307782338679527) + (0.7276166407615791 + 0.20371380855919485)) * int(((-0.29898954724131477 + 0.5591695808193938) * int((0.1272185127066694 * 0)))))), ((('' + 'se') + ('t' + '-')) + ('c' + ('dr' + '!'))))
    if (not W1N6K_h.DOTS_ARE_CONS):
        QI0_kY(M_8fT_l7, lKa4b11c7, (((-41 + -23) + (92 + -53)) + ((121 + -35) + (-38 + -22))), ((('s' + 'e') + ('t-' + 'c')) + (chr(100) + ('' + 'r!'))))
    szU6w57.rp4nk2Mm = M_8fT_l7

@lRyIV_K4((('' + ('l' + 'i')) + ('s' + chr(116))))
def v7__G_(*T22O_l):
    nX1h86l7A = nil
    for o3az1w_5 in reversed(T22O_l):
        nX1h86l7A = Pair(o3az1w_5, nX1h86l7A)
    return nX1h86l7A

@lRyIV_K4((('' + ('app' + 'en')) + 'd'))
def F5HAi_Iv_(*T22O_l):
    if (len(T22O_l) == int(((-0.10082167965756383 + 0.20241969296125717) * int((0.4743662071558825 * 0))))):
        return nil
    nX1h86l7A = T22O_l[(- (((-19 + -51) + (-61 + 99)) + ((3 + 85) + (44 + -99))))]
    for T5Q71_U_ in range((len(T22O_l) - (((-161 + 89) + (49 + 11)) + ((138 + -54) + (-128 + 58)))), (- (((-33 + 85) + (-61 + 8)) + ((-167 + 97) + (5 + 67)))), (- (((-11 + -73) + (-58 + 85)) + ((17 + 98) + (-25 + -32))))):
        q5__ = T22O_l[T5Q71_U_]
        if (q5__ is not nil):
            QI0_kY(q5__, NA_lk, T5Q71_U_, ('' + (('a' + 'ppen') + 'd')))
            gng_y = qT71 = Pair(q5__.g_7033293, nX1h86l7A)
            q5__ = q5__.rp4nk2Mm
            while NA_lk(q5__):
                qT71.rp4nk2Mm = Pair(q5__.g_7033293, nX1h86l7A)
                qT71 = qT71.rp4nk2Mm
                q5__ = q5__.rp4nk2Mm
            nX1h86l7A = gng_y
    return nX1h86l7A

@lRyIV_K4((('' + ('s' + 't')) + (('ri' + 'ng') + '?')))
def ODx_t(szU6w57):
    return (isinstance(szU6w57, str) and szU6w57.startswith('"'))

@lRyIV_K4(((('' + 'sy') + 'm') + (str() + ('' + 'bol?'))))
def s600(szU6w57):
    return (isinstance(szU6w57, str) and (not ODx_t(szU6w57)))

def AqoF6(szU6w57):
    return (hB97uMMe3(szU6w57) and (Q_i987(szU6w57) == (((-36 + -11) + (115 + -80)) + ((173 + -93) + (-124 + 58)))) and (szU6w57.g_7033293 == ((str() + ('' + 'va')) + (('r' + 'i') + ('ad' + 'ic')))) and s600(szU6w57.rp4nk2Mm.g_7033293))

def Pza_(szU6w57):
    assert AqoF6(szU6w57)
    return szU6w57.rp4nk2Mm.g_7033293

@lRyIV_K4(((str() + ('' + 'number')) + '?'))
def M9QsCem(szU6w57):
    return (isinstance(szU6w57, N76GD.Real) and (not zdE__4g9(szU6w57)))

@lRyIV_K4(((('' + 'in') + ('' + 'te')) + (('' + 'ge') + ('r' + '?'))))
def bw6b(szU6w57):
    return (M9QsCem(szU6w57) and (isinstance(szU6w57, N76GD.Integral) or (int(szU6w57) == szU6w57)))

def I_OX_74Z(*T22O_l):
    'GSA9___VjRj46_1__9bk6u798tzK'
    for (T5Q71_U_, q5__) in enumerate(T22O_l):
        if (not M9QsCem(q5__)):
            P_7tpp45 = ((('operand {0} ({1' + '}) is not') + (' ' + 'a')) + (chr(32) + ('' + 'number')))
            raise E_VH(P_7tpp45.format(T5Q71_U_, q5__))

def TWD_09(sNGCB1__, v3e_yipno, T22O_l):
    'tmu_85qW4_L_0r3fWg_d_'
    I_OX_74Z(*T22O_l)
    R14t_l93D = v3e_yipno
    for B9_7F40b in T22O_l:
        R14t_l93D = sNGCB1__(R14t_l93D, B9_7F40b)
    R14t_l93D = ED_62n(R14t_l93D)
    return R14t_l93D

def ED_62n(szU6w57):
    if (int(szU6w57) == szU6w57):
        szU6w57 = int(szU6w57)
    return szU6w57

@lRyIV_K4(chr(((63 + -98) + (146 + -68))))
def H5lN4n(*T22O_l):
    return TWD_09(BP13.add, int((((-0.3232775373904151 + 0.0820483873722545) + (-0.323383063044239 + 0.8819112095406978)) * int(((0.18409121154738384 + 0.6487409851687201) * int((0.07508126577726759 * 0)))))), T22O_l)

@lRyIV_K4(chr(((150 + -16) + (-65 + -24))))
def GOr6fa(R9240, *T22O_l):
    I_OX_74Z(R9240, *T22O_l)
    if (len(T22O_l) == int((((-0.08110504689429054 + 0.30180678597719424) + (-0.42906268766302635 + 0.8431121619355172)) * int(((-0.12274816726234983 + 0.5160868592176114) * int((0.5811011761496104 * 0))))))):
        return ED_62n((- R9240))
    return TWD_09(BP13.sub, R9240, T22O_l)

@lRyIV_K4(chr(42))
def DeQnR(*T22O_l):
    return TWD_09(BP13.mul, (((-10 + -91) + (158 + -97)) + ((8 + 72) + (49 + -88))), T22O_l)

@lRyIV_K4(chr(((23 + 42) + (-61 + 43))))
def q08U40_(R9240, *T22O_l):
    I_OX_74Z(R9240, *T22O_l)
    try:
        if (len(T22O_l) == int((((-1.1998999667803698 + 0.8933388599703614) + (0.3826918959479383 + 0.3496470811308008)) * int((0.8750645959689087 * 0))))):
            return ED_62n(BP13.truediv((int(((0.5374560181003825 + 0.1957026761918066) * 0)) + ((-21 + -7) + (121 + -92))), R9240))
        return TWD_09(BP13.truediv, R9240, T22O_l)
    except ZeroDivisionError as Ai5C8:
        raise E_VH(Ai5C8)

@lRyIV_K4(((str() + ('e' + 'x')) + (str() + ('' + 'pt'))))
def tF41i_(R9240, W3335):
    I_OX_74Z(R9240, W3335)
    return pow(R9240, W3335)

@lRyIV_K4(('' + ('' + ('a' + 'bs'))))
def Sf21Q(R9240):
    return abs(R9240)

@lRyIV_K4(((chr(113) + ('' + 'uo')) + ('t' + ('ien' + 't'))))
def D_v1(R9240, W3335):
    I_OX_74Z(R9240, W3335)
    try:
        return ((- ((- R9240) // W3335)) if ((R9240 < 0) ^ (W3335 < int((((-0.2791340881817058 + 0.3577962260401827) + (-0.5877817433525472 + 0.8924950453280138)) * 0)))) else (R9240 // W3335))
    except ZeroDivisionError as Ai5C8:
        raise E_VH(Ai5C8)

@lRyIV_K4((chr((44 + 65)) + (chr(111) + ('du' + 'lo'))))
def V5y2gE(R9240, W3335):
    I_OX_74Z(R9240, W3335)
    try:
        return (R9240 % W3335)
    except ZeroDivisionError as Ai5C8:
        raise E_VH(Ai5C8)

@lRyIV_K4(((chr(114) + ('emai' + 'nde')) + 'r'))
def Cn9u3(R9240, W3335):
    I_OX_74Z(R9240, W3335)
    try:
        nX1h86l7A = (R9240 % W3335)
    except ZeroDivisionError as Ai5C8:
        raise E_VH(Ai5C8)
    while (((nX1h86l7A < int(((-0.3224634890775525 + 0.933609209630475) * int((0.51747117681729 * 0))))) and (R9240 > int((((0.036381348560786675 + 0.4004719235621833) + (-0.724010716484315 + 0.7773221095219298)) * int(((0.3851090627671899 + 0.38072772090860807) * int((0.02439576697166257 * 0)))))))) or ((nX1h86l7A > int(((-0.5495597826902608 + 0.7598490311246475) * int((0.21898276704945607 * 0))))) and (R9240 < int(((0.030427439979912596 + 0.5729470108374554) * 0))))):
        nX1h86l7A -= W3335
    return nX1h86l7A

def Qu32h2(ZLWo_49, t8_33E__, W3s73=None):
    's_85j___95_V121Hb4Qb_QB10'
    qX84k = (getattr(ZLWo_49, t8_33E__) if (W3s73 is None) else getattr(ZLWo_49, t8_33E__, W3s73))

    def zj_ll(*T22O_l):
        I_OX_74Z(*T22O_l)
        return qX84k(*T22O_l)
    return zj_ll
for gB6t3 in [(chr((146 + -49)) + (str() + ('' + 'cos'))), ('' + (('' + 'acos') + 'h')), (chr(97) + ('' + ('s' + 'in'))), (str() + (('a' + 'si') + ('' + 'nh'))), ((str() + ('' + 'at')) + (str() + ('' + 'an'))), ('a' + (chr(116) + ('a' + 'n2'))), (('a' + ('' + 'ta')) + (str() + ('n' + 'h'))), ((('c' + 'e') + chr(105)) + chr((14 + 94))), ((('' + 'co') + ('' + 'pysi')) + (chr(103) + chr(110))), (('' + ('' + 'co')) + chr((104 + 11))), ('' + ('' + ('co' + 'sh'))), (chr(100) + (('e' + 'gr') + ('' + 'ees'))), ((chr(102) + ('' + 'lo')) + (chr(111) + 'r')), (str() + (chr(108) + ('o' + 'g'))), (chr(108) + (('' + 'og') + ('' + '10'))), ((('' + 'log') + chr(49)) + 'p'), ((str() + ('rad' + 'ian')) + chr((171 + -56))), ('' + (str() + ('si' + 'n'))), (('' + ('s' + 'in')) + chr(104)), ((chr(115) + chr(113)) + (chr(114) + 't')), (chr((62 + 54)) + ('a' + 'n')), ((chr(116) + ('' + 'an')) + chr(104)), (('' + ('t' + 'r')) + (str() + ('' + 'unc')))]:
    lRyIV_K4(gB6t3)(Qu32h2(f2c150, gB6t3))
lRyIV_K4(((chr(108) + chr(111)) + (str() + ('g' + '2'))))(Qu32h2(f2c150, (str() + (('lo' + 'g') + chr(50))), (lambda szU6w57: f2c150.log(szU6w57, (((-67 + -43) + (-34 + 48)) + ((120 + 64) + (-156 + 70)))))))

def y80c8_0x(oU2JCuL, szU6w57, M_8fT_l7):
    I_OX_74Z(szU6w57, M_8fT_l7)
    return oU2JCuL(szU6w57, M_8fT_l7)

@lRyIV_K4(chr(((196 + -79) + (-94 + 38))))
def h8nR6vY1(szU6w57, M_8fT_l7):
    return y80c8_0x(BP13.eq, szU6w57, M_8fT_l7)

@lRyIV_K4(chr(60))
def u8m45_s(szU6w57, M_8fT_l7):
    return y80c8_0x(BP13.lt, szU6w57, M_8fT_l7)

@lRyIV_K4(chr(((184 + -41) + (-79 + -2))))
def gh80(szU6w57, M_8fT_l7):
    return y80c8_0x(BP13.gt, szU6w57, M_8fT_l7)

@lRyIV_K4((str() + (chr(60) + chr(61))))
def aQ_8t7c0(szU6w57, M_8fT_l7):
    return y80c8_0x(BP13.le, szU6w57, M_8fT_l7)

@lRyIV_K4(('>' + chr((30 + 31))))
def y99R(szU6w57, M_8fT_l7):
    return y80c8_0x(BP13.ge, szU6w57, M_8fT_l7)

@lRyIV_K4(('' + (('' + 'ev') + ('e' + 'n?'))))
def B2_US(szU6w57):
    I_OX_74Z(szU6w57)
    return ((szU6w57 % (((-69 + 43) + (162 + -100)) + ((75 + -64) + (-104 + 59)))) == int((((-1.0443483115834407 + 0.6599033461680168) + (0.04246199560417829 + 0.5848600852129269)) * int(((-0.6100246162706274 + 0.8679425833459736) * int((0.9290927758324161 * 0)))))))

@lRyIV_K4(((chr(111) + 'd') + (str() + ('' + 'd?'))))
def v9__91D_(szU6w57):
    I_OX_74Z(szU6w57)
    return ((szU6w57 % (((-75 + 84) + (-45 + -14)) + ((24 + 86) + (-85 + 27)))) == (((158 + -100) + (-37 + 33)) + ((68 + -95) + (13 + -39))))

@lRyIV_K4((('' + ('' + 'ze')) + (str() + ('ro' + '?'))))
def vKP4B(szU6w57):
    I_OX_74Z(szU6w57)
    return (szU6w57 == int((((-0.536971258559434 + 0.6425991031849333) + (-0.10071816829969238 + 0.2539573985707003)) * int(((-0.4322439310479791 + 0.8616744990223814) * 0)))))

@lRyIV_K4(((('' + 'ato') + chr(109)) + chr((90 + -27))))
def T2rS50q(szU6w57):
    return (zdE__4g9(szU6w57) or M9QsCem(szU6w57) or s600(szU6w57) or N5vQ20(szU6w57) or ODx_t(szU6w57))

@lRyIV_K4(((('d' + 'i') + ('' + 'sp')) + (('l' + 'a') + chr(121))))
def yo74brdY(*T22O_l):
    T22O_l = [repl_str((eval(B9_7F40b) if ODx_t(B9_7F40b) else B9_7F40b)) for B9_7F40b in T22O_l]
    print(*T22O_l, end=str())

@lRyIV_K4(((('p' + 'r') + 'i') + ('' + ('' + 'nt'))))
def qUP06_c(*T22O_l):
    T22O_l = [repl_str(B9_7F40b) for B9_7F40b in T22O_l]
    print(*T22O_l)

@lRyIV_K4((chr((124 + -24)) + (chr(105) + ('splayl' + 'n'))))
def JuLF(*T22O_l):
    yo74brdY(*T22O_l)
    x_x07()

@lRyIV_K4((('n' + ('e' + 'wlin')) + chr((161 + -60))))
def x_x07():
    print()
    q_5Yqs.stdout.flush()

@lRyIV_K4((str() + (('e' + 'r') + ('' + 'ror'))))
def x33__T(P_7tpp45=None):
    P_7tpp45 = (str() if (P_7tpp45 is None) else repl_str(P_7tpp45))
    raise E_VH(P_7tpp45)

@lRyIV_K4(((('' + 'ex') + chr(105)) + chr((85 + 31))))
def n0tj_():
    raise EOFError
hq69__wI8 = qb_6_U = None

def Lt82():
    import turtle as O__a
    O__a.title(((('Schem' + 'e') + (' Turt' + 'le')) + chr(115)))

def O69_dEm():
    try:
        from abstract_turtle import turtle as hq69__wI8
    except ImportError:
        raise E_VH((str() + (('Could not find abstract_turtle.' + ' This should never happen in student-facing situations. If ') + ('you' + ' are a student, please file a bug on Piazza.'))))
    return hq69__wI8

def qLa_3():
    try:
        import tkinter as z1fd
    except:
        raise E_VH(chr(((32 + 6) + (19 + -47))).join([((('Could not ' + 'impo') + ('rt tk' + 'inter, so the tk-turtle will ')) + (('not' + ' ') + ('wor' + 'k.'))), ((('' + 'Either install python with tkinter ') + ('support or r' + 'un in pillow-turtle m')) + ('o' + ('' + 'de')))]))
    from abstract_turtle import TkCanvas as T69tO1
    return T69tO1((((1005 + -42) + (-21 + 70)) + ((-13 + -36) + (-31 + 68))), (((940 + 85) + (8 + 31)) + ((-51 + -6) + (17 + -24))), init_hook=Lt82)

def B87_():
    try:
        import PIL as z1fd
        import numpy as z1fd
    except:
        raise E_VH(chr((17 + -7)).join([((('Cou' + 'ld not imp') + ('ort abstract_' + "turtle[pillow_canvas]'s ")) + (('de' + 'pe') + ('nde' + 'ncies.'))), ((('To instal' + 'l t') + ('hes' + 'e pac')) + (('k' + 'ag') + ('es, ' + 'run'))), ((('   ' + ' python3 -m p') + ('ip insta' + "ll 'abstract_")) + (('turtle' + '[') + ('pillow_' + "canvas]'"))), ((('' + 'You can also run in ') + ('t' + 'k-')) + (('tu' + 'rtle') + (' mode by removing the flag' + ' `--pillow-turtle`')))]))
    from abstract_turtle import PillowCanvas as Smf34W7
    return Smf34W7((((875 + 68) + (-3 + -24)) + ((95 + 21) + (-67 + 35))), (((1044 + 61) + (-84 + 71)) + ((29 + -62) + (-2 + -57))))

def j8l_93479():
    global hq69__wI8, qb_6_U
    if (hq69__wI8 is not None):
        return
    Y278r3W = O69_dEm()
    if W1N6K_h.TK_TURTLE:
        try:
            uBHc = qLa_3()
        except E_VH as o3az1w_5:
            print(o3az1w_5, file=q_5Yqs.stderr)
            print(((('Attem' + 'pting pi') + ('l' + 'l')) + (('' + 'ow canvas') + ('' + ' mode'))), file=q_5Yqs.stderr)
            uBHc = B87_()
    else:
        uBHc = B87_()
    (hq69__wI8, qb_6_U) = (Y278r3W, uBHc)
    hq69__wI8.set_canvas(qb_6_U)
    hq69__wI8.mode(('' + (('' + 'lo') + ('g' + 'o'))))

@lRyIV_K4(((str() + ('for' + 'wa')) + (chr(114) + chr(100))), ('' + (chr(102) + chr(100))))
def k531J8(U_t__5__7):
    'lxJ7Z_U88__9P0bRH6X62hO831'
    I_OX_74Z(U_t__5__7)
    j8l_93479()
    hq69__wI8.forward(U_t__5__7)

@lRyIV_K4(((str() + ('' + 'back')) + (('' + 'wa') + ('' + 'rd'))), (('' + ('' + 'bac')) + chr((183 + -76))), (str() + (chr(98) + 'k')))
def Q8k7G1f(U_t__5__7):
    'N2_6y93636__JO_l7kvrpG426cJWa'
    I_OX_74Z(U_t__5__7)
    j8l_93479()
    hq69__wI8.backward(U_t__5__7)

@lRyIV_K4((chr((176 + -68)) + ('' + ('e' + 'ft'))), (str() + ('l' + 't')))
def Wh0__6(U_t__5__7):
    'vw_ZE42g98L614_4Yxx72c2b4k7_'
    I_OX_74Z(U_t__5__7)
    j8l_93479()
    hq69__wI8.left(U_t__5__7)

@lRyIV_K4(((('' + 'ri') + 'g') + (chr(104) + 't')), ('r' + chr(116)))
def q6Ks(U_t__5__7):
    'I_7_6__PTI9_8VR_o246_R'
    I_OX_74Z(U_t__5__7)
    j8l_93479()
    hq69__wI8.right(U_t__5__7)

@lRyIV_K4((str() + (str() + ('c' + 'ircle'))))
def v948396(gng_y, v1FOH_=None):
    'mR_GzI17TXJ9q_X_hY35DCY4__9k2'
    if (v1FOH_ is None):
        I_OX_74Z(gng_y)
    else:
        I_OX_74Z(gng_y, v1FOH_)
    j8l_93479()
    hq69__wI8.circle(gng_y, (v1FOH_ and v1FOH_))

@lRyIV_K4(((('s' + 'e') + ('' + 'tpos')) + ('' + ('itio' + 'n'))), (('' + ('' + 'setpo')) + chr((136 + -21))), (str() + ('' + ('' + 'goto'))))
def t_2p(szU6w57, M_8fT_l7):
    'PeS1o3_GJ0xP349k56nK31_413'
    I_OX_74Z(szU6w57, M_8fT_l7)
    j8l_93479()
    hq69__wI8.setposition(szU6w57, M_8fT_l7)

@lRyIV_K4(((('' + 'set') + ('' + 'headi')) + ('' + ('' + 'ng'))), (chr((70 + 45)) + ('e' + ('t' + 'h'))))
def y930e8a8_(S5QE):
    'DPdfEg88b__X9_YkZ8o_'
    I_OX_74Z(S5QE)
    j8l_93479()
    hq69__wI8.setheading(S5QE)

@lRyIV_K4(((chr(112) + chr(101)) + ('' + ('' + 'nup'))), (chr(112) + 'u'))
def Q87kn2x():
    'fkYG6y_05JG7yo__80J5_0'
    j8l_93479()
    hq69__wI8.penup()

@lRyIV_K4((chr((172 + -60)) + ('e' + ('n' + 'down'))), (str() + (chr(112) + chr(100))))
def N0M0():
    'p__Dk699rSE38_3_bf8p_4'
    j8l_93479()
    hq69__wI8.pendown()

@lRyIV_K4(((('' + 'sh') + ('' + 'owt')) + (('' + 'ur') + ('t' + 'le'))), ('' + ('' + ('' + 'st'))))
def sR1gG7():
    'Tw100RWH5rz1h_5P36Rw'
    j8l_93479()
    hq69__wI8.showturtle()

@lRyIV_K4(((str() + ('h' + 'id')) + (chr(101) + ('tu' + 'rtle'))), (str() + ('' + ('' + 'ht'))))
def XO87Z_c8():
    'ZDoRmw103m_Ml_7n_Ld_'
    j8l_93479()
    hq69__wI8.hideturtle()

@lRyIV_K4((('c' + chr(108)) + (('e' + 'a') + 'r')))
def j3o_26_():
    'cU27__UYOWepH4pS5l_Q29e'
    j8l_93479()
    hq69__wI8.clear()

@lRyIV_K4(((str() + ('' + 'co')) + (str() + ('l' + 'or'))))
def j9A__406s(N5193):
    'e_D__mS6IQ2_2rK4Yfsi5__DoO'
    j8l_93479()
    QI0_kY(N5193, ODx_t, int(((-0.2576749387981436 + 0.4692992724980838) * int((0.5348465109919383 * 0)))), (chr((107 + -8)) + ('o' + ('' + 'lor'))))
    hq69__wI8.color(eval(N5193))

@lRyIV_K4(((str() + ('' + 'rg')) + chr((196 + -98))))
def p_0PTW(i54yU_8EU, j4p_j0_c, r1z5):
    'hg0M8u_8___nZWr_ZYi6E'
    b6_6r25E = (i54yU_8EU, j4p_j0_c, r1z5)
    for szU6w57 in b6_6r25E:
        if ((szU6w57 < int((((-0.03725179688719504 + 0.37022589317938615) + (0.12779270624065397 + 0.29925762986702376)) * int(((-0.09951544142569868 + 0.9413617754948261) * 0))))) or (szU6w57 > (((188 + -78) + (-128 + 63)) + ((-40 + 46) + (10 + -60))))):
            raise E_VH((((('Illega' + 'l ') + ('color in' + 'te')) + ('' + ('nsity' + ' in '))) + repl_str(b6_6r25E)))
    I09_ = tuple((int((szU6w57 * (((221 + 27) + (106 + -90)) + ((-67 + -26) + (96 + -12))))) for szU6w57 in b6_6r25E))
    return (('' + (('' + '"#%02') + ('x' + '%02x%02x"'))) % I09_)

@lRyIV_K4((('' + ('b' + 'egin_')) + ('' + ('fi' + 'll'))))
def UH24z():
    'iHZIs3_qU1txj4_a1_u0_6_v_'
    j8l_93479()
    hq69__wI8.begin_fill()

@lRyIV_K4(((('' + 'en') + ('d' + '_')) + (('' + 'fi') + ('' + 'll'))))
def GS__YTv1():
    'O1D77t0n_j_880qWnkcO1'
    j8l_93479()
    hq69__wI8.end_fill()

@lRyIV_K4(((('b' + 'g') + ('' + 'colo')) + chr(114)))
def EW_34(N5193):
    j8l_93479()
    QI0_kY(N5193, ODx_t, int((((0.14329018300620977 + 0.01379343593623894) + (0.03357595671261204 + 0.2832847350647507)) * int((0.22273676684826116 * 0)))), ((str() + ('b' + 'g')) + (('c' + 'olo') + 'r')))
    hq69__wI8.bgcolor(eval(N5193))

@lRyIV_K4(((chr(101) + ('' + 'xi')) + (('ton' + 'cl') + ('' + 'ick'))))
def F_2I():
    global hq69__wI8
    'jm8m76E_2y9_92J6X__R'
    if (hq69__wI8 is None):
        return
    j8l_93479()
    if W1N6K_h.TK_TURTLE:
        print(((('Close or' + ' ') + ('click ' + 'on turtl')) + (('e window' + ' ') + ('to' + ' complete exit'))))
    if (W1N6K_h.TURTLE_SAVE_PATH is not None):
        gj0H4_7ll(W1N6K_h.TURTLE_SAVE_PATH)
    hq69__wI8.exitonclick()
    hq69__wI8 = None

@lRyIV_K4((('s' + ('' + 'pe')) + (chr(101) + chr(100))))
def mr7JP(R14t_l93D):
    'GNm3_j5FiitZ0_sw7__N0YN'
    QI0_kY(R14t_l93D, bw6b, int(((0.03652747997238415 + 0.8706503583059532) * int((0.7796770481816093 * 0)))), ((str() + ('' + 'spe')) + (chr(101) + chr(100))))
    j8l_93479()
    hq69__wI8.speed(R14t_l93D)

@lRyIV_K4(((chr(112) + ('ix' + 'e')) + 'l'))
def UM9v(szU6w57, M_8fT_l7, N5193):
    'V0o3mR496oY__jKf94dU_'
    QI0_kY(N5193, ODx_t, int((((-0.08605434222047981 + 0.05987538048522234) + (-0.1045736016180352 + 0.36634558196369493)) * int(((-0.54030155178415 + 0.7752841003976276) * int((0.8385354049870588 * 0)))))), (chr((47 + 65)) + ('i' + ('' + 'xel'))))
    WF_8 = eval(N5193)
    j8l_93479()
    hq69__wI8.pixel(szU6w57, M_8fT_l7, WF_8)

@lRyIV_K4(((('' + 'pi') + ('x' + 'elsi')) + ('z' + 'e')))
def L_8L8T(m3R2_UuF):
    'tBq_K_82334OC_x6l598__'
    I_OX_74Z(m3R2_UuF)
    j8l_93479()
    hq69__wI8.pixel_size(m3R2_UuF)

@lRyIV_K4(((('scr' + 'een_w') + chr(105)) + (('' + 'dt') + 'h')))
def x_99G_v():
    'y_nV0WLFgK4L030iR9Gb___O_5'
    j8l_93479()
    return hq69__wI8.canvas_width()

@lRyIV_K4((('' + ('s' + 'creen')) + (('' + '_h') + ('eigh' + 't'))))
def f9yZ1_p_():
    'D7nH5RRWS27R4133G632ejx'
    j8l_93479()
    return hq69__wI8.canvas_height()

def gj0H4_7ll(M832):
    if (not W1N6K_h.TK_TURTLE):
        M832 = (M832 + ('' + (('' + '.pn') + 'g')))
        qb_6_U.export().save(M832, ('p' + ('n' + chr(103))))
    else:
        qb_6_U.export((M832 + ((chr(46) + chr(112)) + chr((94 + 21)))))

@lRyIV_K4((chr(115) + (('' + 'ave-to-fi') + ('' + 'le'))))
def B1_Av4(M832):
    j8l_93479()
    QI0_kY(M832, ODx_t, int((((-0.7485294307014028 + 0.7293454052598287) + (0.05085063926534572 + 0.052860020792128926)) * int(((0.12035348507943633 + 0.6636177725436209) * 0)))), ((('sav' + 'e') + ('-t' + 'o-fil')) + 'e'))
    M832 = eval(M832)
    gj0H4_7ll(M832)

@lRyIV_K4(((('' + 'pri') + 'n') + (('t-t' + 'h') + ('' + 'en-return'))))
def M_TS(W3335, e8N3):
    print(repl_str(W3335))
    return e8N3
'LL4pT_z8N6e88160C_wiJ_A7s_'
tDd9 = (set(string.digits) | set((str() + (('+' + '-') + '.'))))
VE28Mj = (((set(((chr(33) + '$') + (('%&*' + '/:<=>?@') + ('^_' + '~')))) | set(string.ascii_lowercase)) | set(string.ascii_uppercase)) | tDd9)
b____6j8 = set(chr((0 + (-58 + 92))))
Ut8_ = set(((('' + ' \t') + chr(10)) + chr((101 + -88))))
m65p = set(((('()[' + ']') + chr(39)) + chr((46 + 50))))
C3f8S3c = (((Ut8_ | m65p) | b____6j8) | {chr((39 + 5)), ('' + ('' + ('' + ',@')))})
BR87HY_4 = (m65p | {chr(((76 + 64) + (5 + -99))), chr(((15 + 55) + (-107 + 81))), (',' + chr((29 + 35)))})

def Oc3B___(R14t_l93D):
    'nv2_B96_57t64945C_L14B'
    if (len(R14t_l93D) == 0):
        return False
    for N5193 in R14t_l93D:
        if (N5193 not in VE28Mj):
            return False
    return True

def b09q26P(h825J958A, O5IV9_X_):
    'VldE_8_nl_78x92lJ3v8hkb9k'
    while (O5IV9_X_ < len(h825J958A)):
        N5193 = h825J958A[O5IV9_X_]
        if (N5193 == chr(((110 + 3) + (24 + -78)))):
            return (None, len(h825J958A))
        elif (N5193 in Ut8_):
            O5IV9_X_ += (((-78 + 93) + (48 + -9)) + ((-32 + -63) + (-43 + 85)))
        elif (N5193 in m65p):
            'h42y8rK5q7as__PR05P7'
            return (N5193, (O5IV9_X_ + (((139 + -72) + (-40 + -37)) + ((52 + -22) + (-94 + 75)))))
        elif (N5193 == chr((-26 + 61))):
            return (h825J958A[O5IV9_X_:(O5IV9_X_ + (((-137 + 82) + (44 + -73)) + ((48 + -4) + (21 + 21))))], min((O5IV9_X_ + (((76 + -100) + (41 + -81)) + ((0 + 60) + (-26 + 32)))), len(h825J958A)))
        elif (N5193 == ','):
            if (((O5IV9_X_ + (((-105 + 58) + (55 + -98)) + ((149 + -78) + (6 + 14)))) < len(h825J958A)) and (h825J958A[(O5IV9_X_ + (((-147 + 3) + (136 + -75)) + ((177 + -51) + (25 + -67))))] == chr(((141 + 3) + (-124 + 44))))):
                return ((str() + (',' + chr(64))), (O5IV9_X_ + (((-125 + -68) + (124 + -26)) + ((73 + 0) + (66 + -42)))))
            return (N5193, (O5IV9_X_ + (((40 + 80) + (-64 + -16)) + ((55 + -39) + (-148 + 93)))))
        elif (N5193 in b____6j8):
            if (((O5IV9_X_ + (((-83 + 9) + (36 + -4)) + ((-67 + 49) + (27 + 34)))) < len(h825J958A)) and (h825J958A[(O5IV9_X_ + (((-42 + -40) + (64 + 13)) + ((-11 + 56) + (0 + -39))))] == N5193)):
                return ((N5193 + N5193), (O5IV9_X_ + (((55 + 68) + (-43 + 20)) + ((-163 + 47) + (114 + -96)))))
            x_G0 = (bytes(h825J958A[O5IV9_X_:], encoding=((str() + ('' + 'utf')) + ('-' + '8'))),)
            x_ki = N23r1.tokenize(iter(x_G0).__next__)
            next(x_ki)
            b4D__ = next(x_ki)
            if (b4D__.type != N23r1.STRING):
                raise ValueError(((('in' + 'v') + ('' + 'al')) + (('id ' + 'string: {') + ('' + '0}'))).format(b4D__.string))
            return (b4D__.string, (b4D__.end[(((-109 + 99) + (-36 + -14)) + ((62 + 48) + (-23 + -26)))] + O5IV9_X_))
        else:
            X_7MNw95 = O5IV9_X_
            while ((X_7MNw95 < len(h825J958A)) and (h825J958A[X_7MNw95] not in C3f8S3c)):
                X_7MNw95 += (((-113 + 65) + (56 + -63)) + ((55 + -28) + (-18 + 47)))
            return (h825J958A[O5IV9_X_:X_7MNw95], min(X_7MNw95, len(h825J958A)))
    return (None, len(h825J958A))

def C683_7LZ(h825J958A):
    'Z8B81Z_E9_471X_1A86NW5_pAuy0'
    nX1h86l7A = []
    (SQY8_8_7, T5Q71_U_) = b09q26P(h825J958A, 0)
    while (SQY8_8_7 is not None):
        if (SQY8_8_7 in BR87HY_4):
            nX1h86l7A.append(SQY8_8_7)
        elif ((SQY8_8_7 == ('#' + chr(116))) or (SQY8_8_7.lower() == (('t' + 'r') + (chr(117) + chr(101))))):
            nX1h86l7A.append(True)
        elif ((SQY8_8_7 == (chr((64 + -29)) + chr((101 + 1)))) or (SQY8_8_7.lower() == (('' + ('' + 'fal')) + ('' + ('s' + 'e'))))):
            nX1h86l7A.append(False)
        elif (SQY8_8_7 == (('' + ('n' + 'i')) + chr((84 + 24)))):
            nX1h86l7A.append(SQY8_8_7)
        elif (SQY8_8_7[0] in VE28Mj):
            ZQ_62 = False
            if (SQY8_8_7[int((((-0.2923549993638991 + 0.24011453630334567) + (0.3549238735880733 + 0.07942867939335052)) * int(((0.33648847625992095 + 0.6159699376555893) * int((0.23182442244219836 * 0))))))] in tDd9):
                try:
                    nX1h86l7A.append(int(SQY8_8_7))
                    ZQ_62 = True
                except ValueError:
                    try:
                        nX1h86l7A.append(float(SQY8_8_7))
                        ZQ_62 = True
                    except ValueError:
                        pass
            if (not ZQ_62):
                if Oc3B___(SQY8_8_7):
                    nX1h86l7A.append(SQY8_8_7.lower())
                else:
                    raise ValueError(((('i' + 'n') + chr(118)) + (('alid num' + 'era') + ('l or symb' + 'ol: {0}'))).format(SQY8_8_7))
        elif (SQY8_8_7[int(((-0.6838728647896913 + 0.8538412389541079) * 0))] in b____6j8):
            nX1h86l7A.append(SQY8_8_7)
        else:
            y_Dd_9 = [(chr(119) + (('ar' + 'ning') + (': invalid to' + 'ken: {0}'))).format(SQY8_8_7), ((chr((-43 + 75)) * (((41 + -85) + (-60 + 66)) + ((-18 + 5) + (111 + -56)))) + h825J958A), ((chr(((84 + -18) + (-78 + 44))) * (T5Q71_U_ + (((61 + -40) + (49 + 6)) + ((17 + -100) + (-53 + 64))))) + chr(((112 + 67) + (-91 + 6))))]
            raise ValueError(chr(10).join(y_Dd_9))
        (SQY8_8_7, T5Q71_U_) = b09q26P(h825J958A, T5Q71_U_)
    return nX1h86l7A

def f89CMz8vf(input):
    'Vp5Tp341sE1i7lumc_a46z3'
    return (C683_7LZ(h825J958A) for h825J958A in input)

def RQ76U(input):
    'L3_oEUTL6Z3b3_2Y_LJ8_8'
    return len(list(Bk0H7_hpl.chain(*f89CMz8vf(input))))

def F2___6(*yyD8610o7):
    import argparse as fB_434m55
    D5Vz7mF = fB_434m55.ArgumentParser(description=((str() + ('Count Sche' + 'm')) + (('' + 'e ') + ('tokens' + '.'))))
    D5Vz7mF.add_argument((('f' + chr(105)) + ('' + ('' + 'le'))), nargs=chr((64 + -1)), type=fB_434m55.FileType(chr(114)), default=q_5Yqs.stdin, help=((('i' + 'nput') + (' file' + ' to be co')) + (('' + 'unt') + ('e' + 'd'))))
    yyD8610o7 = D5Vz7mF.parse_args()
    print((('c' + ('o' + 'un')) + (chr(116) + ('' + 'ed'))), RQ76U(yyD8610o7.file), ((('' + 'to') + ('ke' + 'n')) + 's'))
'H_cs9DGEBK___e_J3rM3_4'
__version__ = ((('1' + '.') + ('2' + '.')) + chr((134 + -82)))
W1N6K_h.DOTS_ARE_CONS = False
W1N6K_h.TK_TURTLE = False
W1N6K_h.TURTLE_SAVE_PATH = None

def PC_M2(U44x2, aL9z8, z1fd=None):
    'uT96__XY3C3P2VyVY_BZ_y_Ns0'
    aL9z8.stack.append(U44x2)
    if s600(U44x2):
        nX1h86l7A = aL9z8.e8L9_8(U44x2)
        aL9z8.stack.pop()
        return nX1h86l7A
    elif y__Ito(U44x2):
        aL9z8.stack.pop()
        return U44x2
    if (not hB97uMMe3(U44x2)):
        raise E_VH((str() + (('malf' + 'o') + ('rmed list' + ': {0}'))).format(repl_str(U44x2)))
    (g_7033293, rp4nk2Mm) = (U44x2.g_7033293, U44x2.rp4nk2Mm)
    if (s600(g_7033293) and (g_7033293 in VGQk5_)):
        nX1h86l7A = VGQk5_[g_7033293](rp4nk2Mm, aL9z8)
        aL9z8.stack.pop()
        return nX1h86l7A
    else:
        j2nb0Y = PC_M2(g_7033293, aL9z8)
        WP_lA8(j2nb0Y)
        if isinstance(j2nb0Y, ed2_83yG):
            U44x2 = j2nb0Y.tyv__Yh(rp4nk2Mm, aL9z8)
            nX1h86l7A = PC_M2(U44x2, aL9z8)
        else:
            yyD8610o7 = rp4nk2Mm.map((lambda p3_9mu_: PC_M2(p3_9mu_, aL9z8)))
            nX1h86l7A = y77O4e(j2nb0Y, yyD8610o7, aL9z8)
        aL9z8.stack.pop()
        return nX1h86l7A

def y__Ito(U44x2):
    'YA57p5YiH7joTKXX_Is266103EWx'
    return ((T2rS50q(U44x2) and (not s600(U44x2))) or (U44x2 is None))

def y77O4e(j2nb0Y, yyD8610o7, aL9z8):
    'b2pb4_6mSlsG2v_2V5_g19xU4G'
    WP_lA8(j2nb0Y)
    if isinstance(j2nb0Y, BuiltinProcedure):
        return j2nb0Y.D49__LvY(yyD8610o7, aL9z8)
    else:
        c8XTOyH89 = j2nb0Y.LDHHGLT(yyD8610o7, aL9z8)
        return jg91J(j2nb0Y.cr17_1, c8XTOyH89)

def jg91J(N00b4476, aL9z8):
    'PA_Z4q____263aZ_8X0e_6_7'
    H__33NWh7 = None
    while (N00b4476 is not nil):
        TZ68_7 = (N00b4476.rp4nk2Mm is nil)
        H__33NWh7 = PC_M2(N00b4476.g_7033293, aL9z8, TZ68_7)
        N00b4476 = N00b4476.rp4nk2Mm
    return H__33NWh7

class Y_I3G_G9(object):
    'e4fF6AcFp__x2u__R23_73J2_r3S1'

    def __init__(h1gg_0, m47_zR_uz):
        'X93N9o0lJ7U2e54_0rI2'
        h1gg_0.bO_154S = {}
        h1gg_0.m47_zR_uz = m47_zR_uz
        if h1gg_0.m47_zR_uz:
            h1gg_0.stack = h1gg_0.m47_zR_uz.stack
        else:
            h1gg_0.stack = []

    def __repr__(h1gg_0):
        if (h1gg_0.m47_zR_uz is None):
            return ((str() + ('<G' + 'lobal Fr')) + (('a' + 'm') + ('' + 'e>')))
        R14t_l93D = sorted([('' + ('' + ('' + '{0}: {1}'))).format(O5IV9_X_, q5__) for (O5IV9_X_, q5__) in h1gg_0.bO_154S.items()])
        return ((('<{' + '{{') + ('0' + '}}}')) + ((' -> ' + '{') + ('1}' + '>'))).format((chr((28 + 16)) + chr((98 + -66))).join(R14t_l93D), repr(h1gg_0.m47_zR_uz))

    def P9ekGM77T(h1gg_0, A1fY771w, H__33NWh7):
        'PNpP71qK6b4SW5T7_7M915UV0c_6'
        h1gg_0.bO_154S[A1fY771w] = H__33NWh7

    def e8L9_8(h1gg_0, A1fY771w):
        'o_4M_9O8_X4bs3_065_Lr'
        o3az1w_5 = h1gg_0
        while (o3az1w_5 is not None):
            if (A1fY771w in o3az1w_5.bO_154S):
                return o3az1w_5.bO_154S[A1fY771w]
            o3az1w_5 = o3az1w_5.m47_zR_uz
        raise E_VH(((('' + 'un') + ('' + 'known identifier: {0')) + chr((166 + -41))).format(A1fY771w))

    def g09_7(h1gg_0, A1fY771w, H__33NWh7):
        'Yq8tJ5K0Nm26825O_lMY__6ix945_'
        o3az1w_5 = h1gg_0
        while (o3az1w_5 is not None):
            if (A1fY771w in o3az1w_5.bO_154S):
                o3az1w_5.bO_154S[A1fY771w] = H__33NWh7
                return
            o3az1w_5 = o3az1w_5.m47_zR_uz
        raise E_VH(((str() + ('unk' + 'now')) + (('n i' + 'den') + ('tif' + 'ier: {0}'))).format(A1fY771w))

    def O28u6(h1gg_0, cn88J, T22O_l):
        'W4x5W_7713i8_0xqBq4F52105Ftf'
        YjMnz2 = Y_I3G_G9(h1gg_0)
        while ((cn88J != nil) and (T22O_l != nil)):
            if AqoF6(cn88J.g_7033293):
                assert (cn88J.rp4nk2Mm is nil), ((('sho' + 'uld have been caught ea') + ('rl' + 'i')) + (chr(101) + 'r'))
                YjMnz2.P9ekGM77T(Pza_(cn88J.g_7033293), T22O_l)
                return YjMnz2
            if (T22O_l is nil):
                raise E_VH(((chr(116) + ('oo few argum' + 'ents to function c')) + ('a' + ('l' + 'l'))))
            YjMnz2.P9ekGM77T(cn88J.g_7033293, T22O_l.g_7033293)
            (cn88J, T22O_l) = (cn88J.rp4nk2Mm, T22O_l.rp4nk2Mm)
        if ((cn88J != nil) and AqoF6(cn88J.g_7033293)):
            assert (cn88J.rp4nk2Mm is nil), ((('' + 'sh') + ('' + 'ould have ')) + (('been caught' + ' ea') + ('rl' + 'ier')))
            YjMnz2.P9ekGM77T(Pza_(cn88J.g_7033293), T22O_l)
            return YjMnz2
        if ((cn88J != nil) or (T22O_l != nil)):
            raise E_VH(((('Incorrec' + 't number of') + (' argum' + 'e')) + (('nts ' + 'to ') + ('f' + 'unction call'))))
        if (cn88J != nil):
            YjMnz2.P9ekGM77T(cn88J, T22O_l)
        elif (T22O_l != nil):
            raise E_VH(((chr(116) + 'o') + (str() + ('o many arguments to fun' + 'ction call'))))
        return YjMnz2

class j05s(object):
    'gnU847_20DA_5_78Kv7Hn9a5_q_8'

def kTx61Z_Yr(szU6w57):
    return isinstance(szU6w57, j05s)

class BuiltinProcedure(j05s):
    'y7y_H41m727uc5yULE_yj4u_2h'

    def __init__(h1gg_0, sNGCB1__, F6hrGS9=False, t8_33E__='builtin'):
        h1gg_0.t8_33E__ = t8_33E__
        h1gg_0.sNGCB1__ = sNGCB1__
        h1gg_0.F6hrGS9 = F6hrGS9

    def __str__(h1gg_0):
        return (str() + (('#[{' + '0') + ('' + '}]'))).format(h1gg_0.t8_33E__)

    def D49__LvY(h1gg_0, yyD8610o7, aL9z8):
        't85I_xpBDB_pU5U33_Rh2di7_'
        if (not hB97uMMe3(yyD8610o7)):
            raise E_VH((('a' + ('' + 'rg')) + (('uments are n' + 'o') + ('t in ' + 'a list: {0}'))).format(yyD8610o7))
        l6n6kya = []
        while (yyD8610o7 is not nil):
            l6n6kya.append(yyD8610o7.g_7033293)
            yyD8610o7 = yyD8610o7.rp4nk2Mm
        if h1gg_0.F6hrGS9:
            l6n6kya.append(aL9z8)
        try:
            return h1gg_0.sNGCB1__(*l6n6kya)
        except TypeError as Ai5C8:
            raise E_VH(((('i' + 'ncorrect number ') + 'o') + (('' + 'f ') + ('argu' + 'ments: {0}'))).format(h1gg_0))

class LambdaProcedure(j05s):
    'U3t60_9u30AA9_I_Wf41Gm_50B27T'
    t8_33E__ = ((('[la' + 'mbd') + chr(97)) + chr((74 + 19)))

    def __init__(h1gg_0, cn88J, cr17_1, aL9z8):
        'D_52MfesL9hv75j75vw31__whA'
        assert isinstance(aL9z8, Y_I3G_G9), ((('e' + 'n') + ('v must be ' + 'of type Fram')) + chr(101))
        QI0_kY(cn88J, hB97uMMe3, int((((-0.07787017129305351 + 0.5000945080475223) + (-0.37628982313438386 + 0.6889737346504234)) * int(((0.059246953117517376 + 0.14949689182154158) * int((0.4734549911443169 * 0)))))), ((str() + ('Lam' + 'bdaProcedu')) + ('r' + 'e')))
        QI0_kY(cr17_1, hB97uMMe3, (((-110 + 43) + (36 + -6)) + ((-41 + 88) + (21 + -30))), ((('L' + 'am') + chr(98)) + (chr(100) + ('aProce' + 'dure'))))
        h1gg_0.cn88J = cn88J
        h1gg_0.cr17_1 = cr17_1
        h1gg_0.aL9z8 = aL9z8

    def LDHHGLT(h1gg_0, yyD8610o7, aL9z8):
        'Q7862QF03P_O_1spr_7k2o1c0F_c'
        return h1gg_0.aL9z8.O28u6(h1gg_0.cn88J, yyD8610o7)

    def __str__(h1gg_0):
        return str(Pair((('l' + ('a' + 'mb')) + (str() + ('d' + 'a'))), Pair(h1gg_0.cn88J, h1gg_0.cr17_1)))

    def __repr__(h1gg_0):
        return ((str() + ('La' + 'm')) + ('' + ('bdaProcedur' + 'e({0}, {1}, {2})'))).format(repr(h1gg_0.cn88J), repr(h1gg_0.cr17_1), repr(h1gg_0.aL9z8))

class ed2_83yG(LambdaProcedure):
    'R5hKW3B5_o72B43Gw3Ij26RHZ'

    def tyv__Yh(h1gg_0, O83q, aL9z8):
        'gB45_069Kw4_0__m_478ogz__80'
        return tNX_9Ky_Z(h1gg_0, O83q, aL9z8)

def u_B_4_p4q(u_5_f99B, eL4_7):
    'T4o_1_50u3_9X_6_riW__'
    for (t8_33E__, sNGCB1__, a8635_) in eL4_7:
        u_5_f99B.P9ekGM77T(t8_33E__, BuiltinProcedure(sNGCB1__, t8_33E__=a8635_))

def c8cv(N00b4476, aL9z8):
    'e8cE_h88x_4q751q5_X27_F16JY'
    oiK__u_(N00b4476, (((109 + 33) + (-155 + 62)) + ((85 + -74) + (-53 + -5))))
    RJ77Y6f2R = N00b4476.g_7033293
    if s600(RJ77Y6f2R):
        oiK__u_(N00b4476, (((75 + -62) + (61 + -31)) + ((-69 + 12) + (84 + -68))), (((-120 + -33) + (5 + 75)) + ((-82 + 69) + (45 + 43))))
        H__33NWh7 = PC_M2(N00b4476.rp4nk2Mm.g_7033293, aL9z8)
        aL9z8.P9ekGM77T(RJ77Y6f2R, H__33NWh7)
        return RJ77Y6f2R
    elif (isinstance(RJ77Y6f2R, Pair) and s600(RJ77Y6f2R.g_7033293)):
        t8_33E__ = RJ77Y6f2R.g_7033293
        cn88J = RJ77Y6f2R.rp4nk2Mm
        cr17_1 = N00b4476.rp4nk2Mm
        H__33NWh7 = q6iI(Pair(cn88J, cr17_1), aL9z8)
        H__33NWh7.t8_33E__ = t8_33E__
        aL9z8.P9ekGM77T(t8_33E__, H__33NWh7)
        return t8_33E__
    else:
        Y_x944691 = (RJ77Y6f2R.g_7033293 if isinstance(RJ77Y6f2R, Pair) else RJ77Y6f2R)
        raise E_VH(((('' + 'no') + ('n-' + 'sy')) + (('mbol' + ':') + (' {0' + '}'))).format(Y_x944691))

def Qf2Nw4w_(N00b4476, aL9z8):
    'H23V43j41nt9_2W16X046VO03__'
    oiK__u_(N00b4476, (((-20 + -7) + (-51 + 43)) + ((190 + -96) + (-2 + -56))), (((38 + 83) + (-84 + 52)) + ((-12 + -7) + (-128 + 59))))
    return N00b4476.g_7033293

def K86LG6_a3(N00b4476, aL9z8):
    'U73bq0_3z15e83_645c75_GS_L9'
    oiK__u_(N00b4476, (((15 + 61) + (-57 + 34)) + ((34 + -96) + (-3 + 13))))
    return jg91J(N00b4476, aL9z8)

def q6iI(N00b4476, aL9z8):
    'Q29kC_z34h_7vGN_BQ1t'
    oiK__u_(N00b4476, (((-35 + -4) + (99 + -69)) + ((-75 + 39) + (49 + -2))))
    cn88J = N00b4476.g_7033293
    L_Mf_(cn88J)
    return LambdaProcedure(cn88J, N00b4476.rp4nk2Mm, aL9z8)

def N__f5_3Y(N00b4476, aL9z8):
    'x2__8_8Q9453r01a__U35__39'
    oiK__u_(N00b4476, (((7 + 88) + (-20 + 27)) + ((-250 + 71) + (69 + 10))), (((-8 + 0) + (56 + -57)) + ((-113 + 76) + (11 + 38))))
    if u05_4S8(PC_M2(N00b4476.g_7033293, aL9z8)):
        return PC_M2(N00b4476.rp4nk2Mm.g_7033293, aL9z8, True)
    elif (len(N00b4476) == (((184 + -92) + (31 + -20)) + ((-152 + -34) + (118 + -32)))):
        return PC_M2(N00b4476.rp4nk2Mm.rp4nk2Mm.g_7033293, aL9z8, True)

def I978a583(N00b4476, aL9z8):
    'p5_0m5m28tp_I4_6eN_1VO'
    H__33NWh7 = True
    while (N00b4476 is not nil):
        TZ68_7 = (N00b4476.rp4nk2Mm is nil)
        H__33NWh7 = PC_M2(N00b4476.g_7033293, aL9z8, TZ68_7)
        if zB2j3Q8_(H__33NWh7):
            return H__33NWh7
        N00b4476 = N00b4476.rp4nk2Mm
    return H__33NWh7

def Kr4F8aJ_9(N00b4476, aL9z8):
    'c_gnw312VezI77ju8VYr4827t_laW'
    H__33NWh7 = False
    while (N00b4476 is not nil):
        TZ68_7 = (N00b4476.rp4nk2Mm is nil)
        H__33NWh7 = PC_M2(N00b4476.g_7033293, aL9z8, TZ68_7)
        if u05_4S8(H__33NWh7):
            return H__33NWh7
        N00b4476 = N00b4476.rp4nk2Mm
    return H__33NWh7

def J0VF1717B(N00b4476, aL9z8):
    'bjrt48O3_F4_nt__t8i8_c'
    while (N00b4476 is not nil):
        HhXHr0C_8 = N00b4476.g_7033293
        oiK__u_(HhXHr0C_8, (((-24 + -72) + (5 + 49)) + ((64 + -6) + (-85 + 70))))
        if (HhXHr0C_8.g_7033293 == ((str() + ('e' + 'l')) + ('s' + chr(101)))):
            t___534 = True
            if (N00b4476.rp4nk2Mm != nil):
                raise E_VH((('e' + ('lse' + ' mus')) + (('t ' + 'be ') + ('la' + 'st'))))
        else:
            t___534 = PC_M2(HhXHr0C_8.g_7033293, aL9z8)
        if u05_4S8(t___534):
            if (len(HhXHr0C_8) == (((-81 + 70) + (67 + 26)) + ((-227 + 70) + (-12 + 88)))):
                return t___534
            else:
                return jg91J(HhXHr0C_8.rp4nk2Mm, aL9z8)
        N00b4476 = N00b4476.rp4nk2Mm

def F5E_2T4_s(N00b4476, aL9z8):
    'oN_52166U96Dv1Y_72J1__W7'
    oiK__u_(N00b4476, (((-143 + 91) + (-6 + 26)) + ((42 + 2) + (69 + -79))))
    i6TI1B4o6 = m84Do2(N00b4476.g_7033293, aL9z8)
    return jg91J(N00b4476.rp4nk2Mm, i6TI1B4o6)

def m84Do2(bO_154S, aL9z8):
    'K816q6F_MzrzM_wH52279U_5TODn'
    if (not hB97uMMe3(bO_154S)):
        raise E_VH(((str() + ('ba' + 'd bi')) + (('nding' + 's list') + ('' + ' in let form'))))
    (y_R9365, grn6) = (nil, nil)
    while (bO_154S is not nil):
        t400 = bO_154S.g_7033293
        oiK__u_(t400, (((-58 + -41) + (-19 + 57)) + ((-26 + -3) + (88 + 4))), (((23 + 31) + (2 + -82)) + ((-52 + 60) + (-47 + 67))))
        t8_33E__ = t400.g_7033293
        B9_7F40b = PC_M2(t400.rp4nk2Mm.g_7033293, aL9z8)
        y_R9365 = Pair(t8_33E__, y_R9365)
        grn6 = Pair(B9_7F40b, grn6)
        bO_154S = bO_154S.rp4nk2Mm
    L_Mf_(y_R9365)
    return aL9z8.O28u6(y_R9365, grn6)

def OpkI_N540(N00b4476, aL9z8):
    'M_CCLX69V_13E_9E9P___450SEq'
    oiK__u_(N00b4476, (((150 + -59) + (-73 + 33)) + ((-65 + 6) + (55 + -45))))
    RJ77Y6f2R = N00b4476.g_7033293
    if (isinstance(RJ77Y6f2R, Pair) and s600(RJ77Y6f2R.g_7033293)):
        t8_33E__ = RJ77Y6f2R.g_7033293
        cn88J = RJ77Y6f2R.rp4nk2Mm
        cr17_1 = N00b4476.rp4nk2Mm
        L_Mf_(cn88J)
        H__33NWh7 = ed2_83yG(cn88J, cr17_1, aL9z8)
        H__33NWh7.t8_33E__ = t8_33E__
        aL9z8.P9ekGM77T(t8_33E__, H__33NWh7)
        return t8_33E__
    else:
        raise E_VH(((('imp' + 'roper fo') + ('rm' + ' for define-ma')) + ('' + ('cr' + 'o'))))

def i976l(N00b4476, aL9z8):
    'p9_l_g1Sxl0f_S16_h6l_VD7Ec_RP'

    def db09H(B9_7F40b, aL9z8, TNy_1):
        'o4529__9423668Y3817Q'
        if (not NA_lk(B9_7F40b)):
            return B9_7F40b
        if (B9_7F40b.g_7033293 == ((('unq' + 'u') + ('o' + 't')) + chr((188 + -87)))):
            TNy_1 -= (((-83 + 93) + (11 + -38)) + ((139 + -40) + (-39 + -42)))
            if (TNy_1 == int((((-0.525272994243672 + 0.5048487408252756) + (0.21059767736090873 + 0.7639851260472836)) * int(((0.14088923118598573 + 0.04309564875249039) * 0))))):
                N00b4476 = B9_7F40b.rp4nk2Mm
                oiK__u_(N00b4476, (((71 + -86) + (62 + -44)) + ((155 + -59) + (-176 + 78))), (((12 + -81) + (-9 + 57)) + ((51 + -43) + (7 + 7))))
                return PC_M2(N00b4476.g_7033293, aL9z8)
        elif (B9_7F40b.g_7033293 == ((str() + ('qu' + 'a')) + (('siq' + 'uot') + chr(101)))):
            TNy_1 += (((58 + -83) + (-36 + 46)) + ((-42 + -42) + (186 + -86)))
        return B9_7F40b.map((lambda T_5w: db09H(T_5w, aL9z8, TNy_1)))
    oiK__u_(N00b4476, (((41 + -34) + (99 + -53)) + ((10 + -25) + (-58 + 21))), (((-13 + -42) + (-41 + 14)) + ((73 + 30) + (-76 + 56))))
    return db09H(N00b4476.g_7033293, aL9z8, (((88 + -66) + (58 + -79)) + 0))

def Dk_5h(N00b4476, aL9z8):
    raise E_VH(((('unquote' + ' o') + ('u' + 'tside ')) + (('of qua' + 'siq') + ('uo' + 'te'))))

def dGj2f54_4(N00b4476, aL9z8):
    'pkwxIl070k_0_a_7r_3ky_2ov5BM_'
    oiK__u_(N00b4476, (((59 + 39) + (-99 + 12)) + ((-23 + -29) + (100 + -57))))
    t8_33E__ = N00b4476.g_7033293
    if (not s600(t8_33E__)):
        raise E_VH((((('' + 'ba') + ('d' + ' a')) + (('rg' + 'u') + ('me' + 'nt: '))) + repl_str(t8_33E__)))
    H__33NWh7 = PC_M2(N00b4476.rp4nk2Mm.g_7033293, aL9z8)
    aL9z8.g09_7(t8_33E__, H__33NWh7)

def i976l(N00b4476, aL9z8):
    'Zyc0FbN_9H_8I4_U0__134yXreM5'
    oiK__u_(N00b4476, (((-70 + 39) + (15 + -26)) + ((103 + -97) + (14 + 23))), (((64 + -85) + (145 + -94)) + ((-68 + 35) + (-65 + 69))))

    def db09H(B9_7F40b, TNy_1=1):
        'BJZ_1c7_1HD24_Batc7p_3_b03'
        if NA_lk(B9_7F40b):
            if (B9_7F40b.g_7033293 in (((('unq' + 'u') + ('o' + 't')) + chr(101)), ((chr(117) + chr(110)) + (('qu' + 'ote-spl') + ('i' + 'cing'))))):
                TNy_1 -= (((136 + -71) + (96 + -95)) + ((-144 + -6) + (175 + -90)))
                if (TNy_1 == int(((-0.18848068756581426 + 0.42543561058341983) * int((0.4830250028418167 * 0))))):
                    N00b4476 = B9_7F40b.rp4nk2Mm
                    oiK__u_(N00b4476, (((-12 + -60) + (61 + -80)) + ((83 + -79) + (146 + -58))), (((67 + -83) + (-110 + 65)) + ((101 + -26) + (-4 + -9))))
                    f4M31_H01 = PC_M2(N00b4476.g_7033293, aL9z8)
                    mV9_ = (B9_7F40b.g_7033293 == ((('un' + 'quot') + ('e' + '-')) + (('' + 'spli') + ('c' + 'ing'))))
                    if (mV9_ and (not hB97uMMe3(f4M31_H01))):
                        P_7tpp45 = ((('unqu' + 'ote-') + 's') + (('plicing used on non-' + 'list') + (': {' + '0}')))
                        raise E_VH(P_7tpp45.format(f4M31_H01))
                    return (f4M31_H01 if mV9_ else Pair(f4M31_H01, nil))
            elif (B9_7F40b.g_7033293 == (chr(113) + (('' + 'uasi') + ('qu' + 'ote')))):
                TNy_1 += ((0 + (13 + -49)) + ((48 + -58) + (92 + -45)))
            return Pair(B9_7F40b.Nc_c61_((lambda T_5w: db09H(T_5w, TNy_1))), nil)
        else:
            return Pair(B9_7F40b, nil)
    if (NA_lk(N00b4476.g_7033293) and (N00b4476.g_7033293.g_7033293 == (str() + (('unq' + 'u') + ('o' + 'te-splicing'))))):
        P_7tpp45 = ((chr(117) + ('n' + 'qu')) + (('ote-splicing' + ' not in list te') + ('mplate: {' + '0}')))
        raise E_VH(P_7tpp45.format(N00b4476.g_7033293))
    return db09H(N00b4476.g_7033293).g_7033293

def WW6___n(N00b4476, aL9z8):
    raise E_VH(((('Ca' + 'nno') + ('t ev' + 'al')) + (('ua' + 'te variadi') + ('c' + ' symbol'))))
VGQk5_ = {(chr(97) + (str() + ('' + 'nd'))): I978a583, (str() + (('b' + 'e') + ('' + 'gin'))): K86LG6_a3, (chr(99) + (('o' + 'n') + 'd')): J0VF1717B, ((('d' + 'e') + ('fi' + 'n')) + chr(101)): c8cv, (str() + (str() + ('i' + 'f'))): N__f5_3Y, (('l' + chr(97)) + (('' + 'mbd') + chr(97))): q6iI, (('l' + chr(101)) + chr((37 + 79))): F5E_2T4_s, ('o' + 'r'): Kr4F8aJ_9, ((str() + ('qu' + 'o')) + (chr(116) + 'e')): Qf2Nw4w_, ((('de' + 'fine-m') + chr(97)) + (('' + 'cr') + chr(111))): OpkI_N540, ((('qu' + 'asi') + ('qu' + 'ot')) + chr(101)): i976l, (str() + (chr(117) + ('nquot' + 'e'))): Dk_5h, ((chr(115) + chr(101)) + (chr(116) + chr(33))): dGj2f54_4, (('' + ('unquo' + 't')) + (('' + 'e-splic') + ('' + 'ing'))): Dk_5h, ((('var' + 'i') + ('' + 'ad')) + ('i' + 'c')): WW6___n}

def oiK__u_(U44x2, min, max=float('inf')):
    'P7gmRML1Ikc0OEY_7_s1016W'
    if (not hB97uMMe3(U44x2)):
        raise E_VH(((('' + ('badl' + 'y forme')) + (('d ' + 'expres') + ('sion' + ': '))) + repl_str(U44x2)))
    f__cU0_ = len(U44x2)
    if (f__cU0_ < min):
        raise E_VH(((('t' + 'o') + ('o fe' + 'w operan')) + (('' + 'ds i') + ('' + 'n form'))))
    elif (f__cU0_ > max):
        raise E_VH(((('too ' + 'many') + ' ') + (('operands' + ' in for') + 'm')))

def L_Mf_(cn88J):
    'J__81UB488q4xc_TN0l5'
    EK_m = set()

    def LX__(A1fY771w, ev473):
        if (AqoF6(A1fY771w) and ev473):
            A1fY771w = Pza_(A1fY771w)
        if (not s600(A1fY771w)):
            raise E_VH(((('' + 'no') + ('n-symbo' + 'l:')) + (chr(32) + ('' + '{0}'))).format(A1fY771w))
        if (A1fY771w in EK_m):
            raise E_VH(((('' + 'duplic') + ('ate sy' + 'mb')) + (chr(111) + ('l: {0' + '}'))).format(A1fY771w))
        EK_m.add(A1fY771w)
    while isinstance(cn88J, Pair):
        LX__(cn88J.g_7033293, (cn88J.rp4nk2Mm is nil))
        cn88J = cn88J.rp4nk2Mm
    if (cn88J != nil):
        import scheme as V_15
        if W1N6K_h.DOTS_ARE_CONS:
            LX__(cn88J, True)
        else:
            raise E_VH(((chr(70) + ('o' + 'rmal')) + (('s' + ' must') + (' be a' + ' list'))))

def WP_lA8(j2nb0Y):
    'h37x2XIe48gi3Mp_k_yy8410d_2n'
    if (not kTx61Z_Yr(j2nb0Y)):
        raise E_VH(((('{0} is ' + 'not ca') + ('lla' + 'ble: {1')) + chr((166 + -41))).format(type(j2nb0Y).__name__.lower(), repl_str(j2nb0Y)))

class MuProcedure(j05s):
    'V7659bZ25IAn62_3NLJ21425k3t'
    t8_33E__ = (chr(91) + ('' + ('mu' + ']')))

    def __init__(h1gg_0, cn88J, cr17_1):
        'DRYe0f44e0ld1q9U9dc80yKE'
        h1gg_0.cn88J = cn88J
        h1gg_0.cr17_1 = cr17_1

    def LDHHGLT(h1gg_0, yyD8610o7, aL9z8):
        'yH15x_sD9V2L83C9974LM3c'
        return aL9z8.O28u6(h1gg_0.cn88J, yyD8610o7)

    def __str__(h1gg_0):
        return str(Pair((chr((190 + -81)) + chr((47 + 70))), Pair(h1gg_0.cn88J, h1gg_0.cr17_1)))

    def __repr__(h1gg_0):
        return ((('Mu' + 'P') + ('' + 'roce')) + (('' + 'dure({') + ('0},' + ' {1})'))).format(repr(h1gg_0.cn88J), repr(h1gg_0.cr17_1))

def iaJ_324P8(N00b4476, aL9z8):
    'VTi8tu70q_2S_IGd6Ht8b_t3927q5'
    oiK__u_(N00b4476, (((112 + -84) + (8 + 15)) + ((-78 + 3) + (67 + -41))))
    cn88J = N00b4476.g_7033293
    L_Mf_(cn88J)
    return MuProcedure(cn88J, N00b4476.rp4nk2Mm)
VGQk5_[(str() + (chr(109) + 'u'))] = iaJ_324P8

class Promise(object):
    'X_3Q3__iX1_94JDV8y4CQ'

    def __init__(h1gg_0, vQ1g4I__0, aL9z8):
        h1gg_0.vQ1g4I__0 = vQ1g4I__0
        h1gg_0.aL9z8 = aL9z8

    def H_7_31_(h1gg_0):
        if (h1gg_0.vQ1g4I__0 is not None):
            H__33NWh7 = PC_M2(h1gg_0.vQ1g4I__0, h1gg_0.aL9z8)
            if ((not W1N6K_h.DOTS_ARE_CONS) and (not ((H__33NWh7 is nil) or isinstance(H__33NWh7, Pair)))):
                raise E_VH((((('' + 'resul') + ('t of f' + 'orci')) + (('ng a promise should be ' + 'a pair or n') + ('il, but' + ' was %s'))) % H__33NWh7))
            h1gg_0.H__33NWh7 = H__33NWh7
            h1gg_0.vQ1g4I__0 = None
        return h1gg_0.H__33NWh7

    def __str__(h1gg_0):
        return (('' + ('#[p' + 'romise (')) + (('{0' + '}for') + ('c' + 'ed)]'))).format(((chr((173 + -63)) + ('' + ('ot' + ' '))) if (h1gg_0.vQ1g4I__0 is not None) else str()))

def d3b88__21(N00b4476, aL9z8):
    'g8J_8fU762S7L_fzq_N__'
    oiK__u_(N00b4476, (((-21 + 72) + (-19 + -45)) + ((17 + -3) + int((0.6800170816558342 * 0)))), (((-23 + -22) + (44 + 42)) + ((-177 + 54) + (114 + -31))))
    return Promise(N00b4476.g_7033293, aL9z8)

def C_J_C66_(N00b4476, aL9z8):
    'M7625i4_7__Q_l82j1f44P'
    oiK__u_(N00b4476, (((-7 + -33) + (-2 + 45)) + ((-36 + 74) + (8 + -47))), (((-25 + -66) + (-45 + 54)) + ((72 + -1) + (-82 + 95))))
    return Pair(PC_M2(N00b4476.g_7033293, aL9z8), d3b88__21(N00b4476.rp4nk2Mm, aL9z8))
VGQk5_[(('' + ('cons' + '-s')) + ('t' + ('re' + 'am')))] = C_J_C66_
VGQk5_[(str() + ('' + ('del' + 'ay')))] = d3b88__21

class cQRmj(object):
    'G_dr4_0p768K52_xDh9f2x'

    def __init__(h1gg_0, U44x2, aL9z8):
        h1gg_0.U44x2 = U44x2
        h1gg_0.aL9z8 = aL9z8

def tNX_9Ky_Z(j2nb0Y, yyD8610o7, aL9z8):
    'Dos23eJFfn2b0X3_769_X'
    WP_lA8(j2nb0Y)
    B9_7F40b = y77O4e(j2nb0Y, yyD8610o7, aL9z8)
    if isinstance(B9_7F40b, cQRmj):
        return PC_M2(B9_7F40b.U44x2, B9_7F40b.aL9z8)
    else:
        return B9_7F40b

def q__1(Y__23):
    'S0__Ew9__97_t156A_Z200_VuJ5'

    def Zf_z991W4(U44x2, aL9z8, TZ68_7=False):
        'z76_s4Z__1_591_1_m_7238e7'
        if (TZ68_7 and (not s600(U44x2)) and (not y__Ito(U44x2))):
            return cQRmj(U44x2, aL9z8)
        nX1h86l7A = cQRmj(U44x2, aL9z8)
        while isinstance(nX1h86l7A, cQRmj):
            (U44x2, aL9z8) = (nX1h86l7A.U44x2, nX1h86l7A.aL9z8)
            nX1h86l7A = Y__23(U44x2, aL9z8)
        return nX1h86l7A
    return Zf_z991W4
if (((('' + 'do') + ('' + 'ct')) + ('' + ('es' + 't'))) not in q_5Yqs.argv[int((((-0.4359311763214825 + 0.16397587107951506) + (-0.1747912279179087 + 0.6399967635258975)) * int((0.1548128134186587 * 0))))]):
    PC_M2 = q__1(PC_M2)

def Z_2j6m9M(sNGCB1__, R14t_l93D, aL9z8):
    QI0_kY(sNGCB1__, kTx61Z_Yr, int(((0.0030270899711980492 + 0.6378173667472364) * int((0.43545466697399904 * 0)))), ((str() + ('m' + 'a')) + 'p'))
    QI0_kY(R14t_l93D, hB97uMMe3, (((-67 + -5) + (13 + -22)) + ((148 + -35) + (0 + -31))), ('' + (chr(109) + ('a' + 'p'))))
    return R14t_l93D.map((lambda szU6w57: tNX_9Ky_Z(sNGCB1__, Pair(szU6w57, nil), aL9z8)))

def n6Qa5Zx(sNGCB1__, R14t_l93D, aL9z8):
    QI0_kY(sNGCB1__, kTx61Z_Yr, int((((-0.5504946498248897 + 0.2274019371320054) + (0.12214247096471054 + 0.676827968832104)) * int(((0.5893762183526141 + 0.12169124187616975) * 0)))), ((chr(102) + 'i') + (('' + 'lte') + 'r')))
    QI0_kY(R14t_l93D, hB97uMMe3, (((0 + -21) + (11 + 1)) + ((17 + -71) + (115 + -51))), ((str() + ('f' + 'il')) + ('t' + ('e' + 'r'))))
    (Zb___69vz, current) = (nil, nil)
    while (R14t_l93D is not nil):
        (OK9o_e2, R14t_l93D) = (R14t_l93D.g_7033293, R14t_l93D.rp4nk2Mm)
        if tNX_9Ky_Z(sNGCB1__, Pair(OK9o_e2, nil), aL9z8):
            if (Zb___69vz is nil):
                Zb___69vz = Pair(OK9o_e2, nil)
                current = Zb___69vz
            else:
                current.rp4nk2Mm = Pair(OK9o_e2, nil)
                current = current.rp4nk2Mm
    return Zb___69vz

def H7__198_(sNGCB1__, R14t_l93D, aL9z8):
    QI0_kY(sNGCB1__, kTx61Z_Yr, int((((-0.5369183179844388 + 0.464630900373999) + (0.2197524070903606 + 0.03503898560000962)) * int((0.3928023237566778 * 0)))), ((str() + ('red' + 'u')) + ('c' + chr(101))))
    QI0_kY(R14t_l93D, (lambda szU6w57: (szU6w57 is not nil)), (((113 + -64) + (-66 + -1)) + ((97 + -40) + (-82 + 44))), ((('re' + 'd') + ('' + 'uc')) + chr(101)))
    QI0_kY(R14t_l93D, hB97uMMe3, (((-44 + 49) + (-188 + 90)) + ((178 + -52) + (-15 + -17))), (chr(114) + (('' + 'ed') + ('uc' + 'e'))))
    (H__33NWh7, R14t_l93D) = (R14t_l93D.g_7033293, R14t_l93D.rp4nk2Mm)
    while (R14t_l93D is not nil):
        H__33NWh7 = tNX_9Ky_Z(sNGCB1__, v7__G_(H__33NWh7, R14t_l93D.g_7033293), aL9z8)
        R14t_l93D = R14t_l93D.rp4nk2Mm
    return H__33NWh7

def H_F_(g_q9d921z, aL9z8, r6Dq10H_c=False, NBee5As=False, L33S=False, jlYO6x3=(), K96a7_3X=False):
    'uPETx6__2t_SGreB9c_F'
    if L33S:
        try:
            enIzy308_((chr((57 + 58)) + (('cheme' + '_li') + chr(98))), True, aL9z8)
        except E_VH:
            pass
        for KB41_V_u in jlYO6x3:
            enIzy308_(KB41_V_u, True, aL9z8)
    while True:
        try:
            D_gy_7 = g_q9d921z()
            while D_gy_7.rsvx9R:
                vQ1g4I__0 = FkZs_2_1(D_gy_7)
                nX1h86l7A = PC_M2(vQ1g4I__0, aL9z8)
                if ((not NBee5As) and (nX1h86l7A is not None)):
                    print(repl_str(nX1h86l7A))
        except (E_VH, SyntaxError, ValueError, RuntimeError) as Ai5C8:
            if K96a7_3X:
                if isinstance(Ai5C8, SyntaxError):
                    Ai5C8 = E_VH(Ai5C8)
                    raise Ai5C8
            VBJ71B80(aL9z8)
            if (isinstance(Ai5C8, RuntimeError) and (((('maxi' + 'mum r') + chr(101)) + (('c' + 'ursion') + (' depth exce' + 'eded'))) not in getattr(Ai5C8, ((('a' + 'r') + chr(103)) + chr(115)))[0])):
                raise
            elif isinstance(Ai5C8, RuntimeError):
                print(((('' + 'Error: maximu') + ('m recu' + 'rsion depth exc')) + (('e' + 'e') + ('' + 'ded'))))
            else:
                print((('' + ('E' + 'r')) + (('r' + 'o') + ('' + 'r:'))), Ai5C8)
        except KeyboardInterrupt:
            if (not L33S):
                raise
            aL9z8.stack = []
            print()
            print(((('' + 'Ke') + ('yboa' + 'rdIn')) + ('t' + ('errup' + 't'))))
            if (not r6Dq10H_c):
                return
        except EOFError:
            print()
            return
X__xU = {(str() + (str() + ('' + 'set'))): (('s' + 'e') + ('' + ('t' + '!')))}

def VBJ71B80(aL9z8):
    print(((('Tra' + 'ceback (m') + ('ost' + ' ')) + (('rece' + 'nt c') + ('' + 'all last):'))))
    for (C_7th, U44x2) in enumerate(aL9z8.stack):
        print(((str() + (chr(32) + ' ')) + str(C_7th)), repl_str(U44x2), sep=chr(((71 + -69) + (55 + -48))))
    aL9z8.stack[:] = []

def enIzy308_(*yyD8610o7):
    'j_5_D_qiF5157264Y2_6_62y'
    if (not ((((-135 + -47) + (33 + 53)) + ((107 + -37) + (120 + -92))) <= len(yyD8610o7) <= (((180 + -87) + (-118 + 65)) + ((21 + -95) + (28 + 9))))):
        N00b4476 = yyD8610o7[:(- (((9 + 16) + (-84 + -13)) + ((-68 + 52) + (37 + 52))))]
        raise E_VH(((('"load' + '" given incorr') + ('ect number o' + 'f argument')) + (('s: ' + '{0') + chr(125))).format(len(N00b4476)))
    y4Z3 = yyD8610o7[int((((-1.3379518627853126 + 0.9272955634009954) + (-0.33227625974861674 + 0.900174788653162)) * int(((0.6703669536175484 + 0.20118899192593187) * int((0.6384244416087161 * 0))))))]
    NBee5As = (yyD8610o7[(((-13 + -14) + (163 + -70)) + ((-95 + -63) + (69 + 24)))] if (len(yyD8610o7) > (((86 + -12) + (-24 + -72)) + ((57 + -40) + (-54 + 61)))) else True)
    aL9z8 = yyD8610o7[(- (((-8 + 62) + (-84 + 55)) + ((82 + -35) + (-41 + -30))))]
    if ODx_t(y4Z3):
        y4Z3 = eval(y4Z3)
    QI0_kY(y4Z3, s600, int((((-0.02172050851492613 + 0.8152672362380198) + (-0.7613832482476788 + 0.9074410066567823)) * int(((0.3842674981464165 + 0.35517165030704523) * 0)))), ((chr(108) + chr(111)) + (str() + ('' + 'ad'))))
    with Z_6JhWu03(y4Z3) as T18z2E:
        TEu594 = T18z2E.readlines()
    yyD8610o7 = ((TEu594, None) if NBee5As else (TEu594,))

    def g_q9d921z():
        return H41634F7(*yyD8610o7)
    J_9s = aL9z8.stack[:]
    aL9z8.stack[:] = []
    H_F_(g_q9d921z, aL9z8, NBee5As=NBee5As, K96a7_3X=True)
    aL9z8.stack[:] = J_9s

def L5948Fbo(kd8FDNX, aL9z8):
    'a_C_83Y2pX31_v9q3ea54_996_22'
    assert ODx_t(kd8FDNX)
    kd8FDNX = eval(kd8FDNX)
    import os as x1374_H
    for szU6w57 in sorted(x1374_H.listdir(chr(((68 + 71) + (-85 + -8))))):
        if (not szU6w57.endswith((('' + ('.' + 's')) + (chr(99) + chr(109))))):
            continue
        enIzy308_(szU6w57, aL9z8)

def Z_6JhWu03(KB41_V_u):
    'Uw0m12s0Hr_1148S0_757Du_HB5_X'
    try:
        return open(KB41_V_u)
    except IOError as u9_7ow:
        if KB41_V_u.endswith((chr((-49 + 95)) + (chr(115) + ('' + 'cm')))):
            raise E_VH(str(u9_7ow))
    try:
        return open((KB41_V_u + ((('' + '.s') + chr(99)) + 'm')))
    except IOError as u9_7ow:
        raise E_VH(str(u9_7ow))

def a7V46_U_():
    'F94cUH0v7_x4__98_M7P'
    aL9z8 = Y_I3G_G9(None)
    aL9z8.P9ekGM77T(((str() + ('' + 'ev')) + (chr(97) + 'l')), BuiltinProcedure(PC_M2, True, (str() + (('e' + 'va') + 'l'))))
    aL9z8.P9ekGM77T(('' + ('' + ('a' + 'pply'))), BuiltinProcedure(tNX_9Ky_Z, True, (('' + ('a' + 'p')) + ('p' + ('l' + 'y')))))
    aL9z8.P9ekGM77T((str() + (('' + 'lo') + ('' + 'ad'))), BuiltinProcedure(enIzy308_, True, (chr(108) + (str() + ('' + 'oad')))))
    aL9z8.P9ekGM77T(((('lo' + 'a') + ('d' + '-')) + ('a' + ('l' + 'l'))), BuiltinProcedure(L5948Fbo, True, ((('l' + 'oad') + ('' + '-a')) + (str() + ('l' + 'l')))))
    aL9z8.P9ekGM77T((chr(112) + (('' + 'rocedu') + ('' + 're?'))), BuiltinProcedure(kTx61Z_Yr, False, ((str() + ('proced' + 'u')) + (chr(114) + ('e' + '?')))))
    aL9z8.P9ekGM77T((str() + (('m' + 'a') + chr(112))), BuiltinProcedure(Z_2j6m9M, True, ((str() + ('' + 'ma')) + chr((153 + -41)))))
    aL9z8.P9ekGM77T(((('f' + 'i') + ('' + 'lte')) + chr((130 + -16))), BuiltinProcedure(n6Qa5Zx, True, (('f' + 'i') + (('lt' + 'e') + chr(114)))))
    aL9z8.P9ekGM77T((('r' + ('ed' + 'uc')) + chr((181 + -80))), BuiltinProcedure(H7__198_, True, ((str() + ('' + 'redu')) + (chr(99) + 'e'))))
    aL9z8.P9ekGM77T(((('und' + 'e') + ('f' + 'in')) + ('' + ('e' + 'd'))), None)
    aL9z8.stack = []
    u_B_4_p4q(aL9z8, C3m_)
    return aL9z8

def F2___6(*argv):
    import argparse as fB_434m55
    D5Vz7mF = fB_434m55.ArgumentParser(description=((('C' + 'S') + ('' + ' 61A Scheme Inte')) + (('' + 'rpret') + ('e' + 'r'))))
    import __main__ as o_9EM_
    if (((str() + ('lo' + 'gi')) + chr(99)) in o_9EM_.__file__):
        V4t_ = (chr(76) + (chr(111) + ('' + 'gic')))
    else:
        V4t_ = (('S' + ('' + 'che')) + (chr(109) + 'e'))
    version = o_9EM_.__version__
    D5Vz7mF.add_argument(((chr(45) + ('' + '-versio')) + chr((20 + 90))), action=(str() + ('v' + ('e' + 'rsion'))), version=(chr(123) + chr((124 + 1))).format(version))
    D5Vz7mF.add_argument(((('' + '--') + chr(100)) + (('ots' + '-are-con') + 's')), action=((('s' + 'to') + ('' + 're_t')) + (chr(114) + ('' + 'ue'))), help=((('run with' + ' p') + ('' + 're-sp19 dotted lists behavior where')) + ((' ' + 'do') + ('ts are con' + 's'))))
    D5Vz7mF.add_argument((('-' + '-') + (('pillow-turt' + 'l') + chr(101))), action=((str() + ('' + 'st')) + (('or' + 'e_tr') + ('' + 'ue'))), help=((('run ' + 'with pillo') + ('w-base' + 'd')) + ((' turtle. This is much faster for r' + 'endering but') + (' there is ' + 'no GUI'))))
    D5Vz7mF.add_argument(((str() + ('' + '--')) + (('turtle-s' + 'ave-pa') + ('t' + 'h'))), default=None, help=((('save the' + ' ') + ('im' + 'age')) + ((' to t' + 'his location when') + (' d' + 'one'))))
    D5Vz7mF.add_argument((chr((96 + -51)) + ('' + ('' + 'load'))), (str() + ('' + ('-' + 'i'))), action=(('' + ('s' + 'to')) + (('re' + '_tr') + ('u' + 'e'))), help=((('' + 'run f') + 'i') + ('' + ('le interacti' + 'vely'))))
    D5Vz7mF.add_argument(((chr(102) + 'i') + ('' + ('' + 'le'))), nargs=chr(((191 + -42) + (-110 + 24))), type=fB_434m55.FileType(chr(((157 + 29) + (-126 + 54)))), default=None, help=(('' + ('' + 'Scheme file to ru')) + chr(110)))
    yyD8610o7 = D5Vz7mF.parse_args()
    import builtins as W1N6K_h
    W1N6K_h.DOTS_ARE_CONS = yyD8610o7.dots_are_cons
    W1N6K_h.TK_TURTLE = (not yyD8610o7.pillow_turtle)
    W1N6K_h.TURTLE_SAVE_PATH = yyD8610o7.turtle_save_path
    q_5Yqs.path.insert(int((((-0.014638054254973665 + 0.6132966668102753) + (-0.02268682361898 + 0.10691114465284235)) * int(((0.5766878162459047 + 0.14468187582763115) * int((0.18079843310999477 * 0)))))), str())
    g_q9d921z = I_1NZ10
    r6Dq10H_c = True
    jlYO6x3 = []
    if (yyD8610o7.file is not None):
        if yyD8610o7.load:
            jlYO6x3.append(getattr(yyD8610o7.file, ('' + (('n' + 'a') + ('' + 'me')))))
        else:
            TEu594 = yyD8610o7.file.readlines()

            def g_q9d921z():
                return H41634F7(TEu594)
            r6Dq10H_c = False
    print(((('We' + 'lcome to the ') + ('' + 'CS ')) + (('61A {}' + ' Interp') + ('reter (' + 'version {})'))).format(V4t_, version))
    H_F_(g_q9d921z, a7V46_U_(), L33S=True, r6Dq10H_c=r6Dq10H_c, jlYO6x3=jlYO6x3)
    F_2I()

