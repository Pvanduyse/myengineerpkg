def _SQR_SQR(X, LEN_CONV): return LEN_CONV(X**(1/2))**2
def _CUB_CUB(X, LEN_CONV): return LEN_CONV(X**(1/3))**3

def _CHAIN_CONV(X, CONVERSIONS):
    RES = X
    for CONV in CONVERSIONS:
        RES = CONV(RES)
    return RES

# -------------------
#  METRIC CONVERIONS
# -------------------

PREFIXES = {
    "TERA":10**12,
    "GIGA":10**9,
    "MEGA":10**6,
    "KILO":10**3,
    "HECTO":10**2,
    "DECA":10**1,
    "DECI":10**-1,
    "CENTI":10**-2,
    "MILLI":10**-3,
    "MICRO":10**-6,
    "NANO":10**-9,
    "PICO":10**-12
}

PRE_METRIC = lambda X, PRE: X*PREFIXES[PRE]
METRIC_PRE = lambda X, PRE: X/PREFIXES[PRE]
PRE2_METRIC2 = lambda X, PRE: _SQR_SQR(X, lambda Y: PRE_METRIC(Y, PRE))
METRIC2_PRE2 = lambda X, PRE: _SQR_SQR(X, lambda Y: METRIC_PRE(Y, PRE))
PRE3_METRIC3 = lambda X, PRE: _CUB_CUB(X, lambda Y: PRE_METRIC(Y, PRE))
METRIC3_PRE3 = lambda X, PRE: _CUB_CUB(X, lambda Y: METRIC_PRE(Y, PRE))

# length
def μm_m(X): return PRE_METRIC(X, "MICRO")
def mm_m(X): return PRE_METRIC(X, "MILLI")
def cm_m(X): return PRE_METRIC(X, "CENTI")
def km_m(X): return PRE_METRIC(X, "KILO")

def m_μm(X): return METRIC_PRE(X, "MICRO")
def m_mm(X): return METRIC_PRE(X, "MILLI")
def m_cm(X): return METRIC_PRE(X, "CENTI")
def m_km(X): return METRIC_PRE(X, "KILO")

# area
def μm2_m2(X): return PRE2_METRIC2(X, "MICRO")
def mm2_m2(X): return PRE2_METRIC2(X, "MILLI")
def cm2_m2(X): return PRE2_METRIC2(X, "CENTI")
def km2_m2(X): return PRE2_METRIC2(X, "KILO")

def m2_μm2(X): return METRIC2_PRE2(X, "MICRO")
def m2_mm2(X): return METRIC2_PRE2(X, "MILLI")
def m2_cm2(X): return METRIC2_PRE2(X, "CENTI")
def m2_km2(X): return METRIC2_PRE2(X, "KILO")

# volume
def μm3_m3(X): return PRE3_METRIC3(X, "MICRO")
def mm3_m3(X): return PRE3_METRIC3(X, "MILLI")
def cm3_m3(X): return PRE3_METRIC3(X, "CENTI")
def km3_m3(X): return PRE3_METRIC3(X, "KILO")

def m3_μm3(X): return METRIC3_PRE3(X, "MICRO")
def m3_mm3(X): return METRIC3_PRE3(X, "MILLI")
def m3_cm3(X): return METRIC3_PRE3(X, "CENTI")
def m3_km3(X): return METRIC3_PRE3(X, "KILO")

# mass
def kg_g(X): return PRE_METRIC(X, "KILO")
def g_kg(X): return METRIC_PRE(X, "KILO")

# energy
def kJ_J(X): return PRE_METRIC(X, "KILO")
def J_kJ(X): return METRIC_PRE(X, "KILO")


# ----------------------
#  IMPERIAL CONVERSIONS
# ----------------------

# length
def in_ft(X): return X/12
def ft_yd(X): return X/3
def yd_mi(X): return X/1760
def ft_mi(X): return _CHAIN_CONV(X, (ft_yd,yd_mi))

def ft_in(X): return X*12
def yd_ft(X): return X*3
def mi_yd(X): return X*1760
def mi_ft(X): return _CHAIN_CONV(X, (mi_yd,yd_ft))

# areas
def in2_ft2(X): return _SQR_SQR(X, in_ft)
def ft2_yd2(X): return _SQR_SQR(X, ft_yd)
def ft2_mi2(X): return _SQR_SQR(X, ft_mi)
def yd2_mi2(X): return _SQR_SQR(X, yd_mi)

def mi2_yd2(X): return _SQR_SQR(X, mi_yd)
def mi2_ft2(X): return _SQR_SQR(X, mi_ft)
def yd2_ft2(X): return _SQR_SQR(X, yd_ft)
def ft2_in2(X): return _SQR_SQR(X, ft_in)

# volumes
def in3_ft3(X): return _CUB_CUB(X, in_ft)
def ft3_yd3(X): return _CUB_CUB(X, ft_yd)
def yd3_mi3(X): return _CUB_CUB(X, yd_mi)
def ft3_mi3(X): return _CUB_CUB(X, ft_mi)

def mi3_yd3(X): return _CUB_CUB(X, mi_yd)
def mi3_ft3(X): return _CUB_CUB(X, mi_ft)
def yd3_ft3(X): return _CUB_CUB(X, yd_ft)
def ft3_in3(X): return _CUB_CUB(X, ft_in)


# --------------------------
#  COMMON INTER CONVERSIONS
# --------------------------

def m_ft(X): return X*3.2808
def ft_m(X): return X/3.2808

def km_mi(X): return _CHAIN_CONV(X, (km_m,m_ft,ft_mi))
def mi_km(X): return _CHAIN_CONV(X, (mi_ft,ft_m,m_km))

# temperature - C/K
def C_K(X): return X+273.15
def K_C(X): return X-273.15

# temperature - F
def C_F(X): return X*9/5 + 32
def F_C(X): return (X - 32) * 5/9
def K_F(X): return _CHAIN_CONV(X, (K_C,C_F))
def F_K(X): return _CHAIN_CONV(X, (F_C,C_K))

# temperature - R
def K_R(X): return X*5/9
def R_K(X): return X*9/5
def R_C(X): return _CHAIN_CONV(X, (R_K,K_C))
def C_R(X): return _CHAIN_CONV(X, (C_K,K_C))
def R_F(X): return _CHAIN_CONV(X, (R_K,K_C,C_F))
def F_R(X): return _CHAIN_CONV(X, (F_C,C_K,K_R))