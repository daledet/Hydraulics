import math

#Bit Nozzle Selection - Optimized Hydraulics

def NozzleAreaSqIn(nozzle1,nozzle2,nozzle3,exponent,constant): # jets 2 or three nozzles
    nozzle_area_sqin = ((nozzle1 ** exponent) + (nozzle2 ** exponent) + (nozzle3 ** exponent)) / constant
    return(nozzle_area_sqin)
NozzleAreaSqIn(17,17,17,2,1303.8)

nozzle_area = NozzleAreaSqIn

def BitNozzlePressureLossPsi(gpm,exponent,mw,constant,nozzle_area): # bPb
    bit_nozzle_pressure_loss_psi = ((gpm ** exponent) * mw) / (constant * (nozzle_area ** exponent))
    return(bit_nozzle_pressure_loss_psi)
BitNozzlePressureLossPsi(420,2,13,10858,0.664979)

def AnnularVelocityFtMin(constant,circulation_rate,hole_size,pipe_od,exponent): # AV
    annular_velocity_ft_min = (constant * circulation_rate) / ((hole_size ** exponent) - (pipe_od ** exponent))
    return(annular_velocity_ft_min)
AnnularVelocityFtMin(24.5,520,12.25,5,2)

def JetNozzlePressureLoss(constant,circulation_rate,exponent,mw,nozzle1,nozzle2,nozzle3): # jPb
    jet_nozzle_pressure_loss = (constant * (circulation_rate ** exponent) * mw) / ((nozzle1 ** exponent) + (nozzle2 ** exponent) + (nozzle3 ** exponent)) ** exponent
    return(jet_nozzle_pressure_loss)
JetNozzlePressureLoss(156.5,520,2,12,12,12,12)

# Critical Annular Velocity

def n(constant1,viscometer1,viscometer2): # dimensionless
    n = constant1 * math.log10(float(viscometer1)/float(viscometer2))
    return(n)
n(3.32,64,37)

def k(viscometer1, constant, n):
    k = float(viscometer1) / (constant ** n)
    print(k)
k(64, 1022, n)
