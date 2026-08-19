# numbers 官方示例

本文件由 `tools/sync-library-examples.py` 从已准备好的上游 skill/runtime 导出：

```arturo
info.get 'symbol | get 'example
```

它用于沉淀默认官方示例，便于后续把示例改写为更严格的 `ensure.that:` 测试。

## `abs`

Documentation: https://arturo-lang.io/documentation/library/numbers/abs

### Example 1

```arturo
print abs 6                 ; 6
print abs 6-7               ; 1
```

### Example 2

```arturo
abs to :complex @[pi 1] 
; => 3.296908309475615
```

## `acos`

Documentation: https://arturo-lang.io/documentation/library/numbers/acos

### Example 1

```arturo
print acos 0                ; 1.570796326794897
print acos 0.3              ; 1.266103672779499
print acos 1.0              ; 0.0
```

### Example 2

```arturo
acos to :complex @[pi 1]
; => 0.3222532939814587-1.86711439316026i
```

## `acosh`

Documentation: https://arturo-lang.io/documentation/library/numbers/acosh

### Example 1

```arturo
print acosh 1.0             ; 0.0
print acosh 2               ; 1.316957896924817
print acosh 5.0             ; 2.292431669561178
```

### Example 2

```arturo
acosh to :complex @[pi 1]
; => 1.86711439316026+0.3222532939814587i
```

## `acsec`

Documentation: https://arturo-lang.io/documentation/library/numbers/acsec

### Example 1

```arturo
print acsec 0               ; nan
print acsec 1.0             ; 1.570796326794897
print acsec 10              ; 0.1001674211615598
```

### Example 2

```arturo
acsec to :complex @[pi 1]
; => 0.2918255976444114-0.0959139808172324i
```

## `acsech`

Documentation: https://arturo-lang.io/documentation/library/numbers/acsech

### Example 1

```arturo
print acsech 0              ; inf
print acsech 1.0            ; 0.0
print acsech 10             ; 0.09983407889920758
```

### Example 2

```arturo
acsech to :complex @[pi 1]
; => 0.2862356627279947-0.08847073864038091i
```

## `actan`

Documentation: https://arturo-lang.io/documentation/library/numbers/actan

### Example 1

```arturo
print actan 0                   ; 1.570796326794897
print actan 1                   ; 0.7853981633974483
print actan 10.0                ; 0.09966865249116204
```

### Example 2

```arturo
actan to :complex @[pi 1]
; => 0.2834557524705047-0.08505998507745414i
```

## `actanh`

Documentation: https://arturo-lang.io/documentation/library/numbers/actanh

### Example 1

```arturo
print actanh 0                  ; nan
print actanh 1                  ; inf
print actanh 10.0               ; 0.1003353477310756
```

### Example 2

```arturo
actanh to :complex @[pi 1]
; => 0.2946214403408572-0.09996750087543603i
```

## `angle`

Documentation: https://arturo-lang.io/documentation/library/numbers/angle

### Example 1

```arturo
a: to complex [1 1]     ; a: 1.0+1.0i
print angle a           ; 0.7853981633974483
```

## `asec`

Documentation: https://arturo-lang.io/documentation/library/numbers/asec

### Example 1

```arturo
print asec 0                ; nan
print asec 45               ; 1.548572275176629
print asec 5                ; 1.369438406004566
```

### Example 2

```arturo
asec to :complex @[pi 1]
; => 1.278970729150485+0.09591398081723231i
```

## `asech`

Documentation: https://arturo-lang.io/documentation/library/numbers/asech

### Example 1

```arturo
print asech 0               ; inf
print asech 0.45            ; 1.436685652839686
print asech 1               ; 0.0
```

### Example 2

```arturo
asech to :complex @[pi 1]
; => 0.09591398081723221-1.278970729150485i
```

## `asin`

Documentation: https://arturo-lang.io/documentation/library/numbers/asin

### Example 1

```arturo
print asin 0                ; 0.0
print asin 0.3              ; 0.3046926540153975
print asin 1.0              ; 1.570796326794897
```

### Example 2

```arturo
asin to :complex @[pi 1]
; => 1.248543032813438+1.867114393160262i
```

## `asinh`

Documentation: https://arturo-lang.io/documentation/library/numbers/asinh

### Example 1

```arturo
print asinh 0               ; 0.0
print asinh 0.3             ; 0.2956730475634224
print asinh 1.0             ; 0.881373587019543
```

### Example 2

```arturo
asinh to :complex @[pi 1]
; => 1.904627686970658+0.2955850342116299i
```

## `atan`

Documentation: https://arturo-lang.io/documentation/library/numbers/atan

### Example 1

```arturo
print atan 0                ; 0.0
print atan 0.3              ; 0.2914567944778671
print atan 1.0              ; 0.7853981633974483
```

### Example 2

```arturo
atan to :complex @[pi 1]
; => 1.287340574324392+0.08505998507745416i
```

## `atan2`

Documentation: https://arturo-lang.io/documentation/library/numbers/atan2

### Example 1

```arturo
atan2 1 1           ; 0.7853981633974483
atan2 1 1.5         ; 0.9827937232473291
```

## `atanh`

Documentation: https://arturo-lang.io/documentation/library/numbers/atanh

### Example 1

```arturo
print atanh 0               ; 0.0
print atanh 0.3             ; 0.3095196042031118
print atanh 1.0             ; inf
```

### Example 2

```arturo
atanh to :complex @[pi 1]
; => 0.2946214403408571+1.470828825919461i
```

## `ceil`

Documentation: https://arturo-lang.io/documentation/library/numbers/ceil

### Example 1

```arturo
print ceil 2.1                      ; 3
print ceil 2.9                      ; 3
print ceil neg 3.5                  ; -3
print ceil 4                        ; 4
print ceil to :rational @[neg 7 2]  ; -3
```

## `clamp`

Documentation: https://arturo-lang.io/documentation/library/numbers/clamp

### Example 1

```arturo
clamp 2 1..3                        ; 2
clamp 0 1..3                        ; 1
clamp 4 1..3                        ; 3
clamp 4 3..1                        ; 3
clamp 5 range.step: 2 0 5           ; 4

clamp 4.5 0..6                      ; 4.5
clamp to :rational [1 5] 0..1       ; 1/5

clamp 4.5 [1 2.5]                   ; 2.5
clamp 2 [5 10]                      ; 5
clamp 2 [10 5]                      ; 5
clamp 2.5 @[1 to :rational [5 2]]   ; 2.5
```

## `conj`

Documentation: https://arturo-lang.io/documentation/library/numbers/conj

### Example 1

```arturo
b: to :complex [1 2]        ; b: 1.0+2.0i
print conj b                ; 1.0-2.0i
```

## `cos`

Documentation: https://arturo-lang.io/documentation/library/numbers/cos

### Example 1

```arturo
print cos 0                 ; 1.0
print cos 0.3               ; 0.955336489125606
print cos 1.0               ; 0.5403023058681398
```

### Example 2

```arturo
cos to :complex [1 1]
; => 0.8337300251311491-0.9888977057628651i
```

## `cosh`

Documentation: https://arturo-lang.io/documentation/library/numbers/cosh

### Example 1

```arturo
print cosh 0                ; 1.0
print cosh 0.3              ; 1.04533851412886
print cosh 1.0              ; 1.543080634815244
```

### Example 2

```arturo
cosh to :complex [2 1]
; => 2.032723007019666+3.0518977991518i
```

## `csec`

Documentation: https://arturo-lang.io/documentation/library/numbers/csec

### Example 1

```arturo
print csec 0                ; inf
print csec 0.3              ; 3.383863361824123
print csec 1.0              ; 1.188395105778121
```

### Example 2

```arturo
csec to :complex [1 1]  
; => 0.6215180171704283-0.3039310016284264i
```

## `csech`

Documentation: https://arturo-lang.io/documentation/library/numbers/csech

### Example 1

```arturo
print csech 0               ; inf
print csech 0.3             ; 3.283853396698424
print csech 1.0             ; 0.8509181282393216
```

### Example 2

```arturo
csech to :complex [1 1]
; => 0.3039310016284264-0.6215180171704283i
```

## `ctan`

Documentation: https://arturo-lang.io/documentation/library/numbers/ctan

### Example 1

```arturo
print ctan 0                ; inf
print ctan 0.3              ; 3.232728143765828
print ctan 1.0              ; 0.6420926159343308
```

### Example 2

```arturo
ctan to :complex [1 1]
; => 0.2176215618544027-0.8680141428959249i
```

## `ctanh`

Documentation: https://arturo-lang.io/documentation/library/numbers/ctanh

### Example 1

```arturo
print ctanh 0               ; inf
print ctanh 0.3             ; 3.432738430321741
print ctanh 1.0             ; 1.313035285499331
```

### Example 2

```arturo
ctanh to :complex [1 1]
; => 0.8680141428959249-0.2176215618544027i
```

## `denominator`

Documentation: https://arturo-lang.io/documentation/library/numbers/denominator

### Example 1

```arturo
num: to :rational 12.4      ; num: 62/5
print denominator num
; => 5
```

### Example 2

```arturo
print denominator 10
; => 1
```

## `digits`

Documentation: https://arturo-lang.io/documentation/library/numbers/digits

### Example 1

```arturo
digits 123
; => [1 2 3]

digits [1 2 3]
; => 123

digits 0
; => [0]

digits neg 12345
; => [1 2 3 4 5]

; digits 1231231231231231231231231231023
; => [1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 0 2 3]
```

## `epsilon`

Documentation: https://arturo-lang.io/documentation/library/numbers/epsilon

### Example 1

```arturo

```

## `even?`

Documentation: https://arturo-lang.io/documentation/library/numbers/even-

### Example 1

```arturo
even? 4           ; => true
even? 3           ; => false
```

### Example 2

```arturo
print select 1..10 => even?       ; 2 4 6 8 10
```

## `exp`

Documentation: https://arturo-lang.io/documentation/library/numbers/exp

### Example 1

```arturo
print exp 1.0           ; 2.718281828459045
print exp 0             ; 1.0
print exp neg 1.0       ; 0.3678794411714423
```

### Example 2

```arturo
exp to :complex @[pi 1]
; => 12.50296958887651+19.47222141884161i
```

## `factorial`

Documentation: https://arturo-lang.io/documentation/library/numbers/factorial

### Example 1

```arturo
factorial 1         ; => 1
factorial 5         ; => 120
factorial 20        ; => 2432902008176640000
```

## `factors`

Documentation: https://arturo-lang.io/documentation/library/numbers/factors

### Example 1

```arturo
factors 16                                  ; => [1 2 4 8 16]
```

### Example 2

```arturo
factors.prime 48                            ; => [2 2 2 2 3]
unique factors.prime 48                     ; => [2 3]

factors.prime 18446744073709551615123120
; => [2 2 2 2 3 5 61 141529 26970107 330103811]
```

## `floor`

Documentation: https://arturo-lang.io/documentation/library/numbers/floor

### Example 1

```arturo
print floor 2.1                     ; 2
print floor 2.9                     ; 2
print floor neg 3.5                 ; -4
print floor 4                       ; 4
print floor to :rational @[neg 7 2] ; -4
```

## `gamma`

Documentation: https://arturo-lang.io/documentation/library/numbers/gamma

### Example 1

```arturo
print gamma 3.0         ; 2.0
print gamma 10.0        ; 362880.0
print gamma 15          ; 87178291199.99985
```

## `gcd`

Documentation: https://arturo-lang.io/documentation/library/numbers/gcd

### Example 1

```arturo
print gcd [48 60 120]         ; 12
```

## `hypot`

Documentation: https://arturo-lang.io/documentation/library/numbers/hypot

### Example 1

```arturo
print hypot 3 4
; 5.0

print hypot 4.0 5.0
; 6.403124237432849
```

## `infinite`

Documentation: https://arturo-lang.io/documentation/library/numbers/infinite

### Example 1

```arturo

```

## `infinite?`

Documentation: https://arturo-lang.io/documentation/library/numbers/infinite-

### Example 1

```arturo
infinite? 4             ; false
infinite? infinite      ; true
infinite? ∞             ; true
```

### Example 2

```arturo
a: infinite
infinite? a             ; true

b: 0
infinite? b             ; false
```

## `lcm`

Documentation: https://arturo-lang.io/documentation/library/numbers/lcm

### Example 1

```arturo
print lcm [48 60 120]         ; 240
```

## `ln`

Documentation: https://arturo-lang.io/documentation/library/numbers/ln

### Example 1

```arturo
print ln 1.0                ; 0.0
print ln 0                  ; -inf
print ln neg 7.0            ; nan
```

### Example 2

```arturo
ln to :complex @[pi 1]
; => 1.19298515341341+0.308169071115985i
```

## `log`

Documentation: https://arturo-lang.io/documentation/library/numbers/log

### Example 1

```arturo
print log 9 3           ; 2.0
print log 32.0 2.0      ; 5.0
print log 0.0 2         ; -inf
print log 100.0 10.0    ; 2.0
```

## `negative?`

Documentation: https://arturo-lang.io/documentation/library/numbers/negative-

### Example 1

```arturo
negative? 5       ; => false
negative? 6-7     ; => true
```

## `numerator`

Documentation: https://arturo-lang.io/documentation/library/numbers/numerator

### Example 1

```arturo
num: to :rational 12.4      ; num: 62/5
print numerator num
; => 62
```

### Example 2

```arturo
print numerator 10
; => 10
```

## `odd?`

Documentation: https://arturo-lang.io/documentation/library/numbers/odd-

### Example 1

```arturo
odd? 4            ; => false
odd? 3            ; => true
```

### Example 2

```arturo
print select 1..10 => odd?       ; 1 3 5 7 9
```

## `pi`

Documentation: https://arturo-lang.io/documentation/library/numbers/pi

### Example 1

```arturo

```

## `positive?`

Documentation: https://arturo-lang.io/documentation/library/numbers/positive-

### Example 1

```arturo
positive? 5       ; => true
positive? 6-7     ; => false
```

## `powmod`

Documentation: https://arturo-lang.io/documentation/library/numbers/powmod

### Example 1

```arturo
powmod 1 10 3   ; => 1
    powmod 3 2 6    ; => 3
    powmod 5 5 15   ; => 5
    powmod 2 3 5    ; => 3
    powmod 2 4 5    ; => 1

    print (powmod 2 168277 673109) = (2 ^ 168277) % 673109
    ; true
```

## `prime?`

Documentation: https://arturo-lang.io/documentation/library/numbers/prime-

### Example 1

```arturo
prime? 2          ; => true
prime? 6          ; => false
prime? 11         ; => true
```

### Example 2

```arturo
; let's check the 14th Mersenne:
; 53113799281676709868958820655246862732959311772703192319944413
; 82004035598608522427391625022652292856688893294862465010153465
; 79337652707239409519978766587351943831270835393219031728127

prime? (2^607)-1  ; => true
```

## `product`

Documentation: https://arturo-lang.io/documentation/library/numbers/product

### Example 1

```arturo
print product [3 4]       ; 12
print product [1 2 4 6]   ; 48
print product []          ; 1
```

### Example 2

```arturo
print product 1..10       ; 3628800
```

### Example 3

```arturo
product.cartesian [[A B C][D E]]
; => [[A D] [A E] [B D] [B E] [C D] [C E]]
```

## `random`

Documentation: https://arturo-lang.io/documentation/library/numbers/random

### Example 1

```arturo
rnd: random 0 60          ; rnd: (a random number between 0 and 60)
```

## `reciprocal`

Documentation: https://arturo-lang.io/documentation/library/numbers/reciprocal

### Example 1

```arturo
r: to :rational [3 2]

print reciprocal r
; 2/3
```

### Example 2

```arturo
reciprocal 3        ; => 1/3
reciprocal 3.2      ; => 5/16
```

## `round`

Documentation: https://arturo-lang.io/documentation/library/numbers/round

### Example 1

```arturo
print round 2.1                     ; 2.0
print round 2.9                     ; 3.0
print round 6                       ; 6.0

print round to :rational [29 10]    ; 3.0
print round to :rational [21 10]    ; 2.0
print round to :rational [5 2]      ; 3.0

print round pi          ; 3.0
```

### Example 2

```arturo
print round.to:5 pi     ; 3.14159
print round.to:2 pi     ; 3.14
```

## `sec`

Documentation: https://arturo-lang.io/documentation/library/numbers/sec

### Example 1

```arturo
print sec 0                 ; 1.0
print sec 0.3               ; 1.046751601538086
print sec 1.0               ; 1.850815717680925
```

### Example 2

```arturo
sec to :complex [1 1]
; => 0.4983370305551868+0.591083841721045i
```

## `sech`

Documentation: https://arturo-lang.io/documentation/library/numbers/sech

### Example 1

```arturo
print sech 0                ; 1.0
print sech 0.3              ; 0.9566279119002483
print sech 1.0              ; 0.6480542736638855
```

### Example 2

```arturo
sech to :complex [1 1]
; => 0.4983370305551868-0.5910838417210451i
```

## `sin`

Documentation: https://arturo-lang.io/documentation/library/numbers/sin

### Example 1

```arturo
print sin 0                 ; 0.0
print sin 0.3               ; 0.2955202066613395
print sin 1.0               ; 0.8414709848078965
```

### Example 2

```arturo
sin to :complex [1 1]
; => 0.4983370305551868-0.5910838417210451i
```

## `sinh`

Documentation: https://arturo-lang.io/documentation/library/numbers/sinh

### Example 1

```arturo
print sinh 0                ; 0.0
print sinh 0.3              ; 0.3045202934471426
print sinh 1.0              ; 1.175201193643801
```

### Example 2

```arturo
sinh to :complex [1 1]
; => 0.6349639147847361+1.298457581415977i
```

## `sqrt`

Documentation: https://arturo-lang.io/documentation/library/numbers/sqrt

### Example 1

```arturo
print sqrt 4                ; 2.0
print sqrt 16.0             ; 4.0
print sqrt 1.45             ; 1.20415945787923
```

### Example 2

```arturo
sqrt to :complex @[pi 1]
; => 1.794226987182141+0.2786715413222365i
```

## `sum`

Documentation: https://arturo-lang.io/documentation/library/numbers/sum

### Example 1

```arturo
print sum [3 4]           ; 7
print sum [1 2 4 6]       ; 13
```

### Example 2

```arturo
print sum 1..10           ; 55
```

## `tan`

Documentation: https://arturo-lang.io/documentation/library/numbers/tan

### Example 1

```arturo
print tan 0                 ; 0.0
print tan 0.3               ; 0.3093362496096232
print tan 1.0               ; 1.557407724654902
```

### Example 2

```arturo
tan to :complex [1 1]
; => 0.2717525853195119+1.083923327338695i
```

## `tanh`

Documentation: https://arturo-lang.io/documentation/library/numbers/tanh

### Example 1

```arturo
print tanh 0            ; 0.0
print tanh 0.3          ; 0.2913126124515909
print tanh 1.0          ; 0.7615941559557649
```

### Example 2

```arturo
tanh to :complex [1 1]
; => 1.083923327338695+0.2717525853195117i
```

## `tau`

Documentation: https://arturo-lang.io/documentation/library/numbers/tau

### Example 1

```arturo

```
