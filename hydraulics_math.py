import math

#Bit Nozzle Selection - Optimized Hydraulics

def nozzleAreaSqIn(nozzle1,nozzle2,nozzle3,exponent,constant): # jets 2 or three nozzles
    nozzle_area_sqin = ((nozzle1 ** exponent) + (nozzle2 ** exponent) + (nozzle3 ** exponent)) / constant
    return(nozzle_area_sqin)
nozzleAreaSqIn(17,17,17,2,1303.8)

def bitNozzlePressureLossPsi(gpm,exponent,mw,constant,nozzle_area): # bPb
    bit_nozzle_pressure_loss_psi = ((gpm ** exponent) * mw) / (constant * (nozzle_area ** exponent))
    return(bit_nozzle_pressure_loss_psi)
bitNozzlePressureLossPsi(420,2,13,10858,0.664979)

def annularVelocityFtMin(constant,circulation_rate,hole_size,pipe_od,exponent): # AV
    annular_velocity_ft_min = (constant * circulation_rate) / ((hole_size ** exponent) - (pipe_od ** exponent))
    return(annular_velocity_ft_min)
annularVelocityFtMin(24.5,520,12.25,5,2)

def jetNozzlePressureLoss(constant,circulation_rate,exponent,mw,nozzle1,nozzle2,nozzle3): # jPb
    jet_nozzle_pressure_loss = (constant * (circulation_rate ** exponent) * mw) / ((nozzle1 ** exponent) + (nozzle2 ** exponent) + (nozzle3 ** exponent)) ** exponent
    return(jet_nozzle_pressure_loss)
jetNozzlePressureLoss(156.5,520,2,12,12,12,12)

# Critical Annular Velocity

n_dimsionless = 3.32 * math.log10(float(64)/float(37))
k_dimensionless = 64 / (1022 ** n_dimsionless)
x_dimsionless = 81600 * k_dimensionless * (n_dimsionless ** 0.387) / (((8.5 - 7) ** n_dimsionless) * 14)

critical_annular_velocity = (x_dimsionless) ** (1 / (2 - n_dimsionless))
critical_flow_rate_gpm = critical_annular_velocity * ((8.5 ** 2) - (7 ** 2)) / 24.5

print (n_dimsionless)
print (k_dimensionless)
print (x_dimsionless)
print (critical_annular_velocity)
print (critical_flow_rate_gpm)

# class CriticalAnnularVelocity:
    # def __init__(self, n_dimsionless, k_dimensionless,x_dimensionless):
    #     self.n_dimsionless = n_dimsionless
    #     self.k_dimsionless =
    #     self.x_dimsionless =
    #
    # def n(constant1,viscometer1,viscometer2): # dimensionless
    #     n = constant1 * math.log10(float(viscometer1)/float(viscometer2))
    #     return(n)
    # n(3.32,64,37)
    #
    # def k(viscometer1, constant, n): #Call the function n
    #     k = viscometer1 / (constant ** n(constant1,viscometer1,viscometer2))
    #     print(k)
    # k(64, 1022, n)

# def n(constant1,viscometer1,viscometer2): # dimensionless
#     n = constant1 * math.log10(float(viscometer1)/float(viscometer2))
#     return(n)
# n(3.32,64,37)
#
# def k(viscometer1, constant, n): #Call the function n
#     k = viscometer1 / (constant ** n(constant1,viscometer1,viscometer2))
#     print(k)
# k(64, 1022, n)
