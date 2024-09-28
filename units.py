ft_to_m = 0.3048
m_to_ft = 3.28084

ft_to_in = 12.0
in_to_ft = 1.0/12.0
mi_to_ft = 5280.0
ft_to_mi = 1.0/5280.0
in_to_mi = 1.0/12.0/5280.0
mi_to_in = 5280.0*12.0

m_to_km  = 0.001
m_to_dm  = 10.0
m_to_cm  = 100.0
m_to_mm  = 1000.0
m_to_um  = 1.0E6  # m to micrometers

m3_to_L  = 1000

min_to_s = 60
hr_to_min= 60
hr_to_s  = 3600

bar_to_pa = 100000

def K_to_C(T_K) :
    return T_K - 278.15

def C_to_K(T_C) :
    return T_C + 278.15

def F_to_C(T_F) :
    return (T_F - 32.0)/1.8

def C_to_F(T_C) :
    return T_C*1.8 + 32.0