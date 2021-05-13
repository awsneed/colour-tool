# colorio-tool
It's a really rough and basic tool from a newbie programmer using nschloe/colorio mostly just for things I want to use it for or think of adding to it.

You need `colorio` and `tabulate`, which can be acquired from `pip`.

Example output, generating a palette:
```
Choose from the options available:
        1. Generate Palette
        2. Get from Jch
        3. Color diff
1
# of Greys: 5
Greys min lightness: 10
Greys max lightness: 90
# of Accents: 5
Custom hue offset: 
Accents lightness: 50
Accents chroma: 20
Name       J    h        R        G        B      a*       b*
-------  ---  ---  -------  -------  -------  ------  -------
grey0     10    0   19.338   18.755   18.647    0       0
grey1     30    0   67.241   65.823   65.558    0       0
grey2     50    0  114.495  112.252  111.833    0       0
grey3     70    0  165.937  162.796  162.21     0       0
grey4     90    0  224.986  220.815  220.036    0       0
accent0   50   36  161.455   91.366   68.777   16.18   11.756
accent1   50  108  120.41   116.155   41.658   -6.18   19.021
accent2   50  180   46.672  128.511  112.251  -20       0
accent3   50  252   73.968  116.633  160.833   -6.18  -19.021
accent4   50  324  137.524   95.106  145.943   16.18  -11.756
```
