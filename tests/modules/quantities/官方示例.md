# quantities 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `acceleration?`

Documentation: https://arturo-lang.io/documentation/library/quantities/acceleration-

### Example 1

```arturo
acceleration? 3`m/s2
; => true
```

## `action?`

Documentation: https://arturo-lang.io/documentation/library/quantities/action-

### Example 1

```arturo
action? 4`kg.m2/s
; => true
```

## `alphaParticleMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/alphaparticlemass

### Example 1

```arturo

```

## `angle?`

Documentation: https://arturo-lang.io/documentation/library/quantities/angle-

### Example 1

```arturo
angle? 5`rad
; => true
```

## `angstromStar`

Documentation: https://arturo-lang.io/documentation/library/quantities/angstromstar

### Example 1

```arturo

```

## `angularVelocity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/angularvelocity-

### Example 1

```arturo
angularVelocity? 6`rad/s
; => true
```

## `area?`

Documentation: https://arturo-lang.io/documentation/library/quantities/area-

### Example 1

```arturo
area? 3`m2
; => true
```

## `areaDensity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/areadensity-

### Example 1

```arturo
areaDensity? 4`kg/m2
; => true
```

## `atomicMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/atomicmass

### Example 1

```arturo

```

## `avogadroConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/avogadroconstant

### Example 1

```arturo

```

## `bohrRadius`

Documentation: https://arturo-lang.io/documentation/library/quantities/bohrradius

### Example 1

```arturo

```

## `boltzmannConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/boltzmannconstant

### Example 1

```arturo

```

## `capacitance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/capacitance-

### Example 1

```arturo
capacitance? 5`F
; => true
```

## `charge?`

Documentation: https://arturo-lang.io/documentation/library/quantities/charge-

### Example 1

```arturo
charge? 6`C
; => true
```

## `classicalElectronRadius`

Documentation: https://arturo-lang.io/documentation/library/quantities/classicalelectronradius

### Example 1

```arturo

```

## `conductance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/conductance-

### Example 1

```arturo
conductance? 3`S
; => true
```

## `conductanceQuantum`

Documentation: https://arturo-lang.io/documentation/library/quantities/conductancequantum

### Example 1

```arturo

```

## `conforms?`

Documentation: https://arturo-lang.io/documentation/library/quantities/conforms-

### Example 1

```arturo
conforms? 3`m `m                ; => true
conforms? 4`m `cm               ; => true

4`yd := 5`m                     ; => true
5`m := `s                       ; => false
```

### Example 2

```arturo
givenValue: 6`yd/s      

conforms? givenValue `m         ; => false
conforms? givenValue `km/h      ; => true
```

### Example 3

```arturo
3`m := 4`m                      ; => true
5`W := 5`N                      ; => false
5`W := 3`J/s                    ; => true
```

## `convert`

Documentation: https://arturo-lang.io/documentation/library/quantities/convert

### Example 1

```arturo
print convert 3`m `cm
; 300.0 cm

print 1`yd2 --> `m2
; 0.836127 m²
```

## `currency?`

Documentation: https://arturo-lang.io/documentation/library/quantities/currency-

### Example 1

```arturo
currency? 4`USD
; => true
```

## `current?`

Documentation: https://arturo-lang.io/documentation/library/quantities/current-

### Example 1

```arturo
current? 5`A
; => true
```

## `currentDensity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/currentdensity-

### Example 1

```arturo
currentDensity? 6`A/m2
; => true
```

## `dataTransferRate?`

Documentation: https://arturo-lang.io/documentation/library/quantities/datatransferrate-

### Example 1

```arturo
dataTransferRate? 3`B/s
; => true
```

## `density?`

Documentation: https://arturo-lang.io/documentation/library/quantities/density-

### Example 1

```arturo
density? 4`kg/m3
; => true
```

## `deuteronMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/deuteronmass

### Example 1

```arturo

```

## `elastance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/elastance-

### Example 1

```arturo
elastance? 5`Daraf
; => true
```

## `electricField?`

Documentation: https://arturo-lang.io/documentation/library/quantities/electricfield-

### Example 1

```arturo
electricField? 6`V/m
; => true
```

## `electricityPrice?`

Documentation: https://arturo-lang.io/documentation/library/quantities/electricityprice-

### Example 1

```arturo
electricityPrice? 3`USD/kWh
; => true
```

## `electronCharge`

Documentation: https://arturo-lang.io/documentation/library/quantities/electroncharge

### Example 1

```arturo

```

## `electronMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/electronmass

### Example 1

```arturo

```

## `electronMassEnergy`

Documentation: https://arturo-lang.io/documentation/library/quantities/electronmassenergy

### Example 1

```arturo

```

## `energy?`

Documentation: https://arturo-lang.io/documentation/library/quantities/energy-

### Example 1

```arturo
energy? 4`J
; => true
```

## `entropy?`

Documentation: https://arturo-lang.io/documentation/library/quantities/entropy-

### Example 1

```arturo
entropy? 5`J/K
; => true
```

## `force?`

Documentation: https://arturo-lang.io/documentation/library/quantities/force-

### Example 1

```arturo
force? 6`N
; => true
```

## `frequency?`

Documentation: https://arturo-lang.io/documentation/library/quantities/frequency-

### Example 1

```arturo
frequency? 3`Hz
; => true
```

## `gravitationalConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/gravitationalconstant

### Example 1

```arturo

```

## `hartreeEnergy`

Documentation: https://arturo-lang.io/documentation/library/quantities/hartreeenergy

### Example 1

```arturo

```

## `heatFlux?`

Documentation: https://arturo-lang.io/documentation/library/quantities/heatflux-

### Example 1

```arturo
heatFlux? 4`W/m2
; => true
```

## `helionMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/helionmass

### Example 1

```arturo

```

## `illuminance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/illuminance-

### Example 1

```arturo
illuminance? 5`lx
; => true
```

## `impedanceOfVacuum`

Documentation: https://arturo-lang.io/documentation/library/quantities/impedanceofvacuum

### Example 1

```arturo

```

## `in`

Documentation: https://arturo-lang.io/documentation/library/quantities/in

### Example 1

```arturo
print in`cm 3`m
; 300.0 cm

print in`m2 1`yd2
; 0.836127 m²
```

## `inductance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/inductance-

### Example 1

```arturo
inductance? 6`H
; => true
```

## `information?`

Documentation: https://arturo-lang.io/documentation/library/quantities/information-

### Example 1

```arturo
information? 3`kB
; => true
```

## `inverseConductanceQuantum`

Documentation: https://arturo-lang.io/documentation/library/quantities/inverseconductancequantum

### Example 1

```arturo

```

## `jerk?`

Documentation: https://arturo-lang.io/documentation/library/quantities/jerk-

### Example 1

```arturo
jerk? 4`m/s3
; => true
```

## `josephsonConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/josephsonconstant

### Example 1

```arturo

```

## `kinematicViscosity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/kinematicviscosity-

### Example 1

```arturo
kinematicViscosity? 5`m2/s
; => true
```

## `length?`

Documentation: https://arturo-lang.io/documentation/library/quantities/length-

### Example 1

```arturo
length? 6`m
; => true
```

## `luminosity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/luminosity-

### Example 1

```arturo
luminosity? 3`cd
; => true
```

## `luminousFlux?`

Documentation: https://arturo-lang.io/documentation/library/quantities/luminousflux-

### Example 1

```arturo
luminousFlux? 4`lm
; => true
```

## `magneticFieldStrength?`

Documentation: https://arturo-lang.io/documentation/library/quantities/magneticfieldstrength-

### Example 1

```arturo
magneticFieldStrength? 3`A/m
; => true
```

## `magneticFlux?`

Documentation: https://arturo-lang.io/documentation/library/quantities/magneticflux-

### Example 1

```arturo
magneticFlux? 5`Wb
; => true
```

## `magneticFluxDensity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/magneticfluxdensity-

### Example 1

```arturo
magneticFluxDensity? 6`T
; => true
```

## `magneticFluxQuantum`

Documentation: https://arturo-lang.io/documentation/library/quantities/magneticfluxquantum

### Example 1

```arturo

```

## `mass?`

Documentation: https://arturo-lang.io/documentation/library/quantities/mass-

### Example 1

```arturo
mass? 4`kg
; => true
```

## `massFlowRate?`

Documentation: https://arturo-lang.io/documentation/library/quantities/massflowrate-

### Example 1

```arturo
massFlowRate? 5`kg/s
; => true
```

## `molarConcentration?`

Documentation: https://arturo-lang.io/documentation/library/quantities/molarconcentration-

### Example 1

```arturo
molarConcentration? 6`mol/m3
; => true
```

## `molarGasConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/molargasconstant

### Example 1

```arturo

```

## `moleFlowRate?`

Documentation: https://arturo-lang.io/documentation/library/quantities/moleflowrate-

### Example 1

```arturo
moleFlowRate? 3`mol/s
; => true
```

## `momentofInertia?`

Documentation: https://arturo-lang.io/documentation/library/quantities/momentofinertia-

### Example 1

```arturo
momentofInertia? 4`kg.m2
; => true
```

## `momentum?`

Documentation: https://arturo-lang.io/documentation/library/quantities/momentum-

### Example 1

```arturo
momentum? 5`kg.m/s
; => true
```

## `muonMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/muonmass

### Example 1

```arturo

```

## `neutronMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/neutronmass

### Example 1

```arturo

```

## `permeability?`

Documentation: https://arturo-lang.io/documentation/library/quantities/permeability-

### Example 1

```arturo
permeability? 6`H/m
; => true
```

## `permittivity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/permittivity-

### Example 1

```arturo
permittivity? 3`F/m
; => true
```

## `planckConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/planckconstant

### Example 1

```arturo

```

## `planckLength`

Documentation: https://arturo-lang.io/documentation/library/quantities/plancklength

### Example 1

```arturo

```

## `planckMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/planckmass

### Example 1

```arturo

```

## `planckTemperature`

Documentation: https://arturo-lang.io/documentation/library/quantities/plancktemperature

### Example 1

```arturo

```

## `planckTime`

Documentation: https://arturo-lang.io/documentation/library/quantities/plancktime

### Example 1

```arturo

```

## `potential?`

Documentation: https://arturo-lang.io/documentation/library/quantities/potential-

### Example 1

```arturo
potential? 4`V
; => true
```

## `power?`

Documentation: https://arturo-lang.io/documentation/library/quantities/power-

### Example 1

```arturo
power? 5`W
; => true
```

## `pressure?`

Documentation: https://arturo-lang.io/documentation/library/quantities/pressure-

### Example 1

```arturo
pressure? 6`Pa
; => true
```

## `property`

Documentation: https://arturo-lang.io/documentation/library/quantities/property

### Example 1

```arturo
property 3`m            ; => 'length
property 4`m2           ; => 'area
property 5`m3           ; => 'volume

property 6`J/s          ; => 'power
property 3`V            ; => 'potential
```

## `protonMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/protonmass

### Example 1

```arturo

```

## `protonMassEnergy`

Documentation: https://arturo-lang.io/documentation/library/quantities/protonmassenergy

### Example 1

```arturo

```

## `radiation?`

Documentation: https://arturo-lang.io/documentation/library/quantities/radiation-

### Example 1

```arturo
radiation? 3`Gy
; => true
```

## `radiationExposure?`

Documentation: https://arturo-lang.io/documentation/library/quantities/radiationexposure-

### Example 1

```arturo
radiationExposure? 4`C/kg
; => true
```

## `reducedPlanckConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/reducedplanckconstant

### Example 1

```arturo

```

## `resistance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/resistance-

### Example 1

```arturo
resistance? 5`Ohm
; => true
```

## `resistivity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/resistivity-

### Example 1

```arturo
resistivity? 6`Ohm.m
; => true
```

## `rydbergConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/rydbergconstant

### Example 1

```arturo

```

## `salary?`

Documentation: https://arturo-lang.io/documentation/library/quantities/salary-

### Example 1

```arturo
salary? 3`USD/h
; => true
```

## `scalar`

Documentation: https://arturo-lang.io/documentation/library/quantities/scalar

### Example 1

```arturo
scalar 3`m              ; => 3
scalar 4.0`m2           ; => 4
scalar 10:2`m3          ; => 5
```

### Example 2

```arturo
scalar 3.1`m            ; => 3.1
scalar 5:2`m            ; => 2.5
```

### Example 3

```arturo
scalar 13:3`m           ; => 13/3
```

## `snap?`

Documentation: https://arturo-lang.io/documentation/library/quantities/snap-

### Example 1

```arturo
snap? 3`m/s4
; => true
```

## `solidAngle?`

Documentation: https://arturo-lang.io/documentation/library/quantities/solidangle-

### Example 1

```arturo
solidAngle? 4`sr
; => true
```

## `specificVolume?`

Documentation: https://arturo-lang.io/documentation/library/quantities/specificvolume-

### Example 1

```arturo
specificVolume? 5`m3/kg
; => true
```

## `specify`

Documentation: https://arturo-lang.io/documentation/library/quantities/specify

### Example 1

```arturo
specify 'nauMile 1.1508`mi

print 2`nauMile                ; 2 nauMile
print 3`nauMile --> `km        ; 5.5560992256 km
```

### Example 2

```arturo
specify.symbol:"NM" 'nauMile 1.1508`mi

print 2`nauMile                ; 2 NM
```

### Example 3

```arturo
specify.describes:"coding speed" 'lph `lines/h

print 100`lph                   ; 100 lph
print property 100`lph          ; coding speed
```

### Example 4

```arturo
specify.property "sweetness" `tspSugar

print property 3`tspSugar       ; sweetness
```

## `speed?`

Documentation: https://arturo-lang.io/documentation/library/quantities/speed-

### Example 1

```arturo
speed? 6`m/s
; => true
```

## `speedOfLight`

Documentation: https://arturo-lang.io/documentation/library/quantities/speedoflight

### Example 1

```arturo

```

## `standardGasVolume`

Documentation: https://arturo-lang.io/documentation/library/quantities/standardgasvolume

### Example 1

```arturo

```

## `standardPressure`

Documentation: https://arturo-lang.io/documentation/library/quantities/standardpressure

### Example 1

```arturo

```

## `standardTemperature`

Documentation: https://arturo-lang.io/documentation/library/quantities/standardtemperature

### Example 1

```arturo

```

## `substance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/substance-

### Example 1

```arturo
substance? 4`mol
; => true
```

## `surfaceTension?`

Documentation: https://arturo-lang.io/documentation/library/quantities/surfacetension-

### Example 1

```arturo
surfaceTension? 5`N/m
; => true
```

## `tauMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/taumass

### Example 1

```arturo

```

## `temperature?`

Documentation: https://arturo-lang.io/documentation/library/quantities/temperature-

### Example 1

```arturo
temperature? 6`oC
; => true
```

## `thermalConductivity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/thermalconductivity-

### Example 1

```arturo
thermalConductivity? 3`W/m.K
; => true
```

## `thermalInsulance?`

Documentation: https://arturo-lang.io/documentation/library/quantities/thermalinsulance-

### Example 1

```arturo
thermalInsulance? 4`m2.K/W
; => true
```

## `thomsonCrossSection`

Documentation: https://arturo-lang.io/documentation/library/quantities/thomsoncrosssection

### Example 1

```arturo

```

## `time?`

Documentation: https://arturo-lang.io/documentation/library/quantities/time-

### Example 1

```arturo
time? 5`s
; => true
```

## `tritonMass`

Documentation: https://arturo-lang.io/documentation/library/quantities/tritonmass

### Example 1

```arturo

```

## `unitless?`

Documentation: https://arturo-lang.io/documentation/library/quantities/unitless-

### Example 1

```arturo
unitless? 6`items
; => true
```

## `units`

Documentation: https://arturo-lang.io/documentation/library/quantities/units

### Example 1

```arturo
units 3`m               ; => `m
units `m2               ; => `m2
units 8`J/s             ; => `J/s
units 7`W               ; => `W
```

### Example 2

```arturo
units.base 3`m          ; => `m
units.base `m2          ; => `m2
units.base 8`J/s        ; => `J/s
units.base 7`W          ; => `J/s
```

### Example 3

```arturo
specify 'ff 3`items
units 3`ff              ; => `items
units.base 3`ff         ; => `items
units.base 3`ff.ha      ; => `items.m2
```

### Example 4

```arturo
specify 'kk 3`m2        
units 3`kk              ; => `kk
units.base 3`kk         ; => `m2
```

## `vacuumPermeability`

Documentation: https://arturo-lang.io/documentation/library/quantities/vacuumpermeability

### Example 1

```arturo

```

## `vacuumPermittivity`

Documentation: https://arturo-lang.io/documentation/library/quantities/vacuumpermittivity

### Example 1

```arturo

```

## `viscosity?`

Documentation: https://arturo-lang.io/documentation/library/quantities/viscosity-

### Example 1

```arturo
viscosity? 3`Pa.s
; => true
```

## `volume?`

Documentation: https://arturo-lang.io/documentation/library/quantities/volume-

### Example 1

```arturo
volume? 4`m3
; => true
```

## `volumetricFlow?`

Documentation: https://arturo-lang.io/documentation/library/quantities/volumetricflow-

### Example 1

```arturo
volumetricFlow? 5`m3/s
; => true
```

## `vonKlitzingConstant`

Documentation: https://arturo-lang.io/documentation/library/quantities/vonklitzingconstant

### Example 1

```arturo

```

## `waveNumber?`

Documentation: https://arturo-lang.io/documentation/library/quantities/wavenumber-

### Example 1

```arturo
waveNumber? 6`/m
; => true
```
