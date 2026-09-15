# Data Dictionary

Source: [https://nces.ed.gov/ipeds/use-the-data](https://nces.ed.gov/ipeds/use-the-data)

## adm

Rows: 22,527

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| admcon1 | BIGINT | 0.0% | 1 |  |
| admcon2 | BIGINT | 0.0% | 3 |  |
| admcon3 | BIGINT | 0.0% | 1 |  |
| admcon4 | BIGINT | 0.0% | 3 |  |
| admcon5 | BIGINT | 0.0% | 3 |  |
| admcon6 | BIGINT | 0.0% | 3 |  |
| admcon7 | BIGINT | 0.0% | 5 |  |
| admcon8 | BIGINT | 0.0% | 1 |  |
| admcon9 | BIGINT | 0.0% | 3 |  |
| admcon10 | BIGINT | 73.7% | 3 |  |
| admcon11 | BIGINT | 73.7% | 3 |  |
| admcon12 | BIGINT | 73.7% | 3 |  |
| xapplcn | VARCHAR | 0.0% | R |  |
| applicants_total | BIGINT | 0.0% | 23406 |  |
| xapplcnm | VARCHAR | 0.0% | R |  |
| applicants_men | DOUBLE | 0.0% | 7568.0 |  |
| xapplcnw | VARCHAR | 0.0% | R |  |
| applicants_women | DOUBLE | 0.0% | 14930.0 |  |
| xapplcnan | VARCHAR | 73.7% | Z |  |
| applcnan | DOUBLE | 92.8% | 0.0 |  |
| xapplcnun | VARCHAR | 73.7% | R |  |
| applcnun | DOUBLE | 78.0% | 908.0 |  |
| xadmssn | VARCHAR | 0.0% | R |  |
| admissions_total | DOUBLE | 1.0% | 13564.0 |  |
| xadmssnm | VARCHAR | 0.0% | R |  |
| admissions_men | DOUBLE | 4.5% | 4580.0 |  |
| xadmssnw | VARCHAR | 0.0% | R |  |
| admissions_women | DOUBLE | 5.0% | 8981.0 |  |
| xadmssnan | VARCHAR | 73.7% | A |  |
| admssnan | DOUBLE | 96.9% | 8.0 |  |
| xadmssnun | VARCHAR | 73.7% | R |  |
| admssnun | DOUBLE | 78.0% | 3.0 |  |
| xenrlt | VARCHAR | 0.0% | R |  |
| enrolled_total | DOUBLE | 1.3% | 1968.0 |  |
| xenrlm | VARCHAR | 0.0% | R |  |
| enrolled_men | DOUBLE | 5.3% | 832.0 |  |
| xenrlw | VARCHAR | 0.0% | R |  |
| enrolled_women | DOUBLE | 5.3% | 1136.0 |  |
| xenrlan | VARCHAR | 73.7% | A |  |
| enrlan | DOUBLE | 97.2% | 0.0 |  |
| xenrlun | VARCHAR | 73.7% | R |  |
| enrlun | DOUBLE | 78.0% | 0.0 |  |
| xenrlft | VARCHAR | 0.0% | R |  |
| enrlft | DOUBLE | 1.7% | 1939.0 |  |
| xenrlftm | VARCHAR | 0.0% | R |  |
| enrlftm | DOUBLE | 6.3% | 818.0 |  |
| xenrlftw | VARCHAR | 0.0% | R |  |
| enrlftw | DOUBLE | 6.0% | 1121.0 |  |
| xenrlftan | VARCHAR | 73.7% | A |  |
| enrlftan | DOUBLE | 98.2% | 21.0 |  |
| xenrlftun | VARCHAR | 73.7% | R |  |
| enrlftun | DOUBLE | 78.1% | 0.0 |  |
| xenrlpt | VARCHAR | 0.0% | R |  |
| enrlpt | DOUBLE | 24.9% | 29.0 |  |
| xenrlptm | VARCHAR | 0.0% | R |  |
| enrlptm | DOUBLE | 27.6% | 14.0 |  |
| xenrlptw | VARCHAR | 0.0% | R |  |
| enrlptw | DOUBLE | 25.5% | 15.0 |  |
| xenrlptan | VARCHAR | 73.7% | A |  |
| enrlptan | DOUBLE | 98.7% | 0.0 |  |
| xenrlptun | VARCHAR | 73.7% | R |  |
| enrlptun | DOUBLE | 83.3% | 0.0 |  |
| xsatnum | VARCHAR | 0.0% | R |  |
| satnum | DOUBLE | 39.3% | 537.0 |  |
| xsatpct | VARCHAR | 0.0% | R |  |
| satpct | DOUBLE | 39.4% | 27.0 |  |
| xactnum | VARCHAR | 0.0% | R |  |
| actnum | DOUBLE | 39.2% | 1317.0 |  |
| xactpct | VARCHAR | 0.0% | R |  |
| actpct | DOUBLE | 39.4% | 67.0 |  |
| xsatvr25 | VARCHAR | 0.0% | R |  |
| sat_verbal_25th | DOUBLE | 45.1% | 420.0 |  |
| xsatvr50 | VARCHAR | 73.7% | R |  |
| satvr50 | DOUBLE | 86.9% | 470.0 |  |
| xsatvr75 | VARCHAR | 0.0% | R |  |
| sat_verbal_75th | DOUBLE | 45.1% | 530.0 |  |
| xsatmt25 | VARCHAR | 0.0% | R |  |
| sat_math_25th | DOUBLE | 45.0% | 390.0 |  |
| xsatmt50 | VARCHAR | 73.7% | R |  |
| satmt50 | DOUBLE | 86.9% | 440.0 |  |
| xsatmt75 | VARCHAR | 0.0% | R |  |
| sat_math_75th | DOUBLE | 45.0% | 510.0 |  |
| xactcm25 | VARCHAR | 0.0% | R |  |
| act_composite_25th | DOUBLE | 44.0% | 14.0 |  |
| xactcm50 | VARCHAR | 73.7% | R |  |
| actcm50 | DOUBLE | 87.1% | 17.0 |  |
| xactcm75 | VARCHAR | 0.0% | R |  |
| act_composite_75th | DOUBLE | 44.0% | 19.0 |  |
| xacten25 | VARCHAR | 0.0% | R |  |
| act_english_25th | DOUBLE | 48.0% | 13.0 |  |
| xacten50 | VARCHAR | 73.7% | R |  |
| acten50 | DOUBLE | 87.9% | 16.0 |  |
| xacten75 | VARCHAR | 0.0% | R |  |
| act_english_75th | DOUBLE | 48.0% | 19.0 |  |
| xactmt25 | VARCHAR | 0.0% | R |  |
| act_math_25th | DOUBLE | 47.9% | 14.0 |  |
| xactmt50 | VARCHAR | 73.7% | R |  |
| actmt50 | DOUBLE | 87.9% | 16.0 |  |
| xactmt75 | VARCHAR | 0.0% | R |  |
| act_math_75th | DOUBLE | 47.9% | 17.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xsatwr25 | VARCHAR | 80.3% | R |  |
| sat_writing_25th | DOUBLE | 93.4% | 370.0 |  |
| xsatwr75 | VARCHAR | 80.3% | R |  |
| sat_writing_75th | DOUBLE | 93.4% | 457.0 |  |
| xactwr25 | VARCHAR | 80.3% | A |  |
| act_writing_25th | DOUBLE | 97.2% | 7.0 |  |
| xactwr75 | VARCHAR | 80.3% | A |  |
| act_writing_75th | DOUBLE | 97.2% | 8.0 |  |

## al

Rows: 43,075

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| lexp100k | BIGINT | 47.8% | 1 |  |
| lcolelyn | BIGINT | 0.0% | 2 |  |
| xlpbooks | VARCHAR | 0.0% | R |  |
| lpbooks | DOUBLE | 4.2% | 321026.0 |  |
| xlebooks | VARCHAR | 0.0% | R |  |
| lebooks | BIGINT | 0.0% | 228847 |  |
| xledatab | VARCHAR | 0.0% | R |  |
| ledatab | BIGINT | 0.0% | 107 |  |
| xlpmedia | VARCHAR | 0.0% | R |  |
| lpmedia | DOUBLE | 4.2% | 25105.0 |  |
| xlemedia | VARCHAR | 0.0% | R |  |
| lemedia | BIGINT | 0.0% | 38684 |  |
| xlpseria | VARCHAR | 19.8% | R |  |
| lpseria | DOUBLE | 23.5% | 1392.0 |  |
| xleseria | VARCHAR | 19.8% | R |  |
| leseria | BIGINT | 19.8% | 132597 |  |
| xlpcollc | VARCHAR | 0.0% | R |  |
| lpcllct | DOUBLE | 4.2% | 347523.0 |  |
| xlecollc | VARCHAR | 0.0% | R |  |
| lecllct | BIGINT | 0.0% | 400235 |  |
| xltcllct | VARCHAR | 9.9% | R |  |
| ltcllct | BIGINT | 9.9% | 747758 |  |
| xlpcrclt | VARCHAR | 0.0% | R |  |
| lpcrclt | DOUBLE | 4.2% | 650.0 |  |
| xlecrclt | VARCHAR | 0.0% | R |  |
| lecrclt | BIGINT | 0.0% | 150959 |  |
| xltcrclt | VARCHAR | 9.9% | R |  |
| ltcrclt | BIGINT | 9.9% | 151609 |  |
| lilldyn | BIGINT | 19.8% | 1 |  |
| xlilldpr | VARCHAR | 0.0% | R |  |
| lilldpr | DOUBLE | 23.6% | 941.0 |  |
| xlilldrc | VARCHAR | 0.0% | R |  |
| lilldrc | DOUBLE | 23.6% | 207.0 |  |
| lilsyn | BIGINT | 56.7% | 1 |  |
| xlstotal | VARCHAR | 56.7% | R |  |
| lstotal | DOUBLE | 59.6% | 25.0 |  |
| xlslibrn | VARCHAR | 56.7% | R |  |
| lslibrn | DOUBLE | 59.6% | 6.0 |  |
| xlsoprof | VARCHAR | 56.7% | R |  |
| lsoprof | DOUBLE | 59.6% | 4.0 |  |
| xlsopaid | VARCHAR | 56.7% | R |  |
| lsopaid | DOUBLE | 59.6% | 2.0 |  |
| xlsstast | VARCHAR | 56.7% | R |  |
| lsstast | DOUBLE | 59.6% | 13.0 |  |
| xlbranch | VARCHAR | 0.0% | R |  |
| lbranch | DOUBLE | 25.9% | 0.0 |  |
| xsalwag | VARCHAR | 0.0% | R |  |
| lsalwag | DOUBLE | 25.9% | 637844.0 |  |
| lfrngbyn | BIGINT | 0.0% | 1 |  |
| xlfrngbn | VARCHAR | 0.0% | R |  |
| lfrngbn | DOUBLE | 25.9% | 211624.0 |  |
| xlexmsbb | VARCHAR | 0.0% | R |  |
| lexmsbb | DOUBLE | 25.9% | 21359.0 |  |
| xlexmscs | VARCHAR | 0.0% | R |  |
| lexmscs | DOUBLE | 25.9% | 706964.0 |  |
| xlexmsot | VARCHAR | 0.0% | R |  |
| lexmsot | DOUBLE | 25.9% | 314783.0 |  |
| xlexmstl | VARCHAR | 0.0% | R |  |
| lexmstl | DOUBLE | 25.9% | 1043106.0 |  |
| xlexomps | VARCHAR | 0.0% | R |  |
| lexomps | DOUBLE | 25.9% | 17625.0 |  |
| xlexomot | VARCHAR | 0.0% | R |  |
| lexomot | DOUBLE | 25.9% | 409052.0 |  |
| xlexomtl | VARCHAR | 0.0% | R |  |
| lexomtl | DOUBLE | 25.9% | 426677.0 |  |
| xlexptot | VARCHAR | 0.0% | R |  |
| lexptot | DOUBLE | 25.9% | 2319251.0 |  |
| lswmsom | DOUBLE | 25.9% | 2107627.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| lsuppvrs | BIGINT | 80.2% | 1 |  |

## c_a

Rows: 6,895,231

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| cipcode | DOUBLE | 0.0% | 1.0999 |  |
| major_number | BIGINT | 2.5% | 1 |  |
| award_level | BIGINT | 0.0% | 5 |  |
| xctotalt | VARCHAR | 24.8% | R |  |
| ctotalt | BIGINT | 24.8% | 10 |  |
| xctotalm | VARCHAR | 24.8% | R |  |
| ctotalm | BIGINT | 24.8% | 1 |  |
| xctotalw | VARCHAR | 24.8% | R |  |
| ctotalw | BIGINT | 24.8% | 9 |  |
| xcaiant | VARCHAR | 24.8% | R |  |
| caiant | DOUBLE | 32.4% | 0.0 |  |
| xcaianm | VARCHAR | 24.8% | R |  |
| caianm | DOUBLE | 32.4% | 0.0 |  |
| xcaianw | VARCHAR | 24.8% | Z |  |
| caianw | DOUBLE | 32.4% | 0.0 |  |
| xcasiat | VARCHAR | 24.8% | R |  |
| casiat | DOUBLE | 32.4% | 0.0 |  |
| xcasiam | VARCHAR | 24.8% | R |  |
| casiam | DOUBLE | 32.4% | 0.0 |  |
| xcasiaw | VARCHAR | 24.8% | Z |  |
| casiaw | DOUBLE | 32.4% | 0.0 |  |
| xcbkaat | VARCHAR | 24.8% | R |  |
| cbkaat | DOUBLE | 32.4% | 10.0 |  |
| xcbkaam | VARCHAR | 24.8% | R |  |
| cbkaam | DOUBLE | 32.4% | 1.0 |  |
| xcbkaaw | VARCHAR | 24.8% | R |  |
| cbkaaw | DOUBLE | 32.4% | 9.0 |  |
| xchispt | VARCHAR | 24.8% | R |  |
| chispt | DOUBLE | 32.4% | 0.0 |  |
| xchispm | VARCHAR | 24.8% | R |  |
| chispm | DOUBLE | 32.4% | 0.0 |  |
| xchispw | VARCHAR | 24.8% | Z |  |
| chispw | DOUBLE | 32.4% | 0.0 |  |
| xcnhpit | VARCHAR | 24.8% | Z |  |
| cnhpit | DOUBLE | 32.4% | 0.0 |  |
| xcnhpim | VARCHAR | 24.8% | Z |  |
| cnhpim | DOUBLE | 32.4% | 0.0 |  |
| xcnhpiw | VARCHAR | 24.8% | Z |  |
| cnhpiw | DOUBLE | 32.4% | 0.0 |  |
| xcwhitt | VARCHAR | 24.8% | Z |  |
| cwhitt | DOUBLE | 32.4% | 0.0 |  |
| xcwhitm | VARCHAR | 24.8% | Z |  |
| cwhitm | DOUBLE | 32.4% | 0.0 |  |
| xcwhitw | VARCHAR | 24.8% | Z |  |
| cwhitw | DOUBLE | 32.4% | 0.0 |  |
| xc2mort | VARCHAR | 24.8% | Z |  |
| c2mort | DOUBLE | 32.4% | 0.0 |  |
| xc2morm | VARCHAR | 24.8% | Z |  |
| c2morm | DOUBLE | 32.4% | 0.0 |  |
| xc2morw | VARCHAR | 24.8% | Z |  |
| c2morw | DOUBLE | 32.4% | 0.0 |  |
| xcunknt | VARCHAR | 24.8% | Z |  |
| cunknt | BIGINT | 24.8% | 0 |  |
| xcunknm | VARCHAR | 24.8% | Z |  |
| cunknm | BIGINT | 24.8% | 0 |  |
| xcunknw | VARCHAR | 24.8% | Z |  |
| cunknw | BIGINT | 24.8% | 0 |  |
| xcnralt | VARCHAR | 24.8% | R |  |
| cnralt | BIGINT | 24.8% | 0 |  |
| xcnralm | VARCHAR | 24.8% | R |  |
| cnralm | BIGINT | 24.8% | 0 |  |
| xcnralw | VARCHAR | 24.8% | R |  |
| cnralw | BIGINT | 24.8% | 0 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| cdistedp | BIGINT | 96.1% | 2 |  |
| xcrace03 | VARCHAR | 64.1% | R |  |
| crace03 | DOUBLE | 67.3% | 3.0 |  |
| xcrace04 | VARCHAR | 64.1% | R |  |
| crace04 | DOUBLE | 67.3% | 3.0 |  |
| xcrace05 | VARCHAR | 64.1% | R |  |
| crace05 | DOUBLE | 67.3% | 0.0 |  |
| xcrace06 | VARCHAR | 64.1% | R |  |
| crace06 | DOUBLE | 67.3% | 0.0 |  |
| xcrace07 | VARCHAR | 64.1% | R |  |
| crace07 | DOUBLE | 67.3% | 0.0 |  |
| xcrace08 | VARCHAR | 64.1% | R |  |
| crace08 | DOUBLE | 67.3% | 2.0 |  |
| xcrace09 | VARCHAR | 64.1% | R |  |
| crace09 | DOUBLE | 67.3% | 0.0 |  |
| xcrace10 | VARCHAR | 64.1% | R |  |
| crace10 | DOUBLE | 67.3% | 0.0 |  |
| xcrace11 | VARCHAR | 64.1% | R |  |
| crace11 | DOUBLE | 67.3% | 31.0 |  |
| xcrace12 | VARCHAR | 64.1% | R |  |
| crace12 | DOUBLE | 67.3% | 16.0 |  |
| xcrace18 | VARCHAR | 69.4% | R |  |
| crace18 | DOUBLE | 72.6% | 6.0 |  |
| xcrace19 | VARCHAR | 69.4% | R |  |
| crace19 | DOUBLE | 72.6% | 0.0 |  |
| xcrace20 | VARCHAR | 69.4% | R |  |
| crace20 | DOUBLE | 72.6% | 2.0 |  |
| xcrace21 | VARCHAR | 69.4% | R |  |
| crace21 | DOUBLE | 72.6% | 0.0 |  |
| xcrace22 | VARCHAR | 69.4% | R |  |
| crace22 | DOUBLE | 72.6% | 47.0 |  |
| xdvcait | VARCHAR | 88.9% | R |  |
| dvcait | BIGINT | 88.9% | 0 |  |
| xdvcaim | VARCHAR | 88.9% | R |  |
| dvcaim | BIGINT | 88.9% | 0 |  |
| xdvcaiw | VARCHAR | 88.9% | R |  |
| dvcaiw | BIGINT | 88.9% | 0 |  |
| xdvcapt | VARCHAR | 88.9% | R |  |
| dvcapt | BIGINT | 88.9% | 2 |  |
| xdvcapm | VARCHAR | 88.9% | R |  |
| dvcapm | BIGINT | 88.9% | 0 |  |
| xdvcapw | VARCHAR | 88.9% | R |  |
| dvcapw | BIGINT | 88.9% | 2 |  |
| xdvcbkt | VARCHAR | 88.9% | R |  |
| dvcbkt | BIGINT | 88.9% | 6 |  |
| xdvcbkm | VARCHAR | 88.9% | R |  |
| dvcbkm | BIGINT | 88.9% | 3 |  |
| xdvcbkw | VARCHAR | 88.9% | R |  |
| dvcbkw | BIGINT | 88.9% | 3 |  |
| xdvchst | VARCHAR | 88.9% | R |  |
| dvchst | BIGINT | 88.9% | 0 |  |
| xdvchsm | VARCHAR | 88.9% | R |  |
| dvchsm | BIGINT | 88.9% | 0 |  |
| xdvchsw | VARCHAR | 88.9% | R |  |
| dvchsw | BIGINT | 88.9% | 0 |  |
| xdvcwht | VARCHAR | 88.9% | R |  |
| dvcwht | BIGINT | 88.9% | 47 |  |
| xdvcwhm | VARCHAR | 88.9% | R |  |
| dvcwhm | BIGINT | 88.9% | 31 |  |
| xdvcwhw | VARCHAR | 88.9% | R |  |
| dvcwhw | BIGINT | 88.9% | 16 |  |
| xcrace01 | VARCHAR | 75.2% | R |  |
| crace01 | BIGINT | 75.2% | 0 |  |
| xcrace02 | VARCHAR | 75.2% | R |  |
| crace02 | BIGINT | 75.2% | 0 |  |
| xcrace13 | VARCHAR | 75.2% | R |  |
| crace13 | BIGINT | 75.2% | 1 |  |
| xcrace14 | VARCHAR | 75.2% | R |  |
| crace14 | BIGINT | 75.2% | 2 |  |
| xcrace15 | VARCHAR | 75.2% | R |  |
| crace15 | BIGINT | 75.2% | 21 |  |
| xcrace16 | VARCHAR | 75.2% | R |  |
| crace16 | BIGINT | 75.2% | 23 |  |
| xcrace17 | VARCHAR | 80.6% | R |  |
| crace17 | BIGINT | 80.6% | 0 |  |
| xcrace23 | VARCHAR | 80.6% | R |  |
| crace23 | BIGINT | 80.6% | 3 |  |
| xcrace24 | VARCHAR | 80.6% | R |  |
| crace24 | BIGINT | 80.6% | 44 |  |

## eap

Rows: 8,999,839

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| eapcat | BIGINT | 55.9% | 10000 |  |
| occupcat | BIGINT | 55.9% | 100 |  |
| facstat | BIGINT | 55.9% | 0 |  |
| xeaptot | VARCHAR | 0.5% | R |  |
| eaptot | BIGINT | 0.5% | 1099 |  |
| xeaptyp | VARCHAR | 0.5% | R |  |
| eaptyp | DOUBLE | 0.6% | 1099.0 |  |
| xeapmed | VARCHAR | 0.5% | A |  |
| eapmed | DOUBLE | 42.4% | 5569.0 |  |
| xeapft | VARCHAR | 55.9% | R |  |
| eapft | DOUBLE | 56.5% | 820.0 |  |
| xeapftty | VARCHAR | 55.9% | R |  |
| eapfttyp | DOUBLE | 56.7% | 820.0 |  |
| xeapftmd | VARCHAR | 55.9% | A |  |
| eapftmed | DOUBLE | 97.8% | 5055.0 |  |
| xeappt | VARCHAR | 55.9% | R |  |
| eappt | DOUBLE | 59.9% | 279.0 |  |
| xeapptty | VARCHAR | 55.9% | R |  |
| eappttyp | DOUBLE | 60.1% | 279.0 |  |
| xeapptmd | VARCHAR | 55.9% | A |  |
| eapptmed | DOUBLE | 97.9% | 514.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| eaprectp | BIGINT | 44.6% | 1245 |  |
| ftpt | BIGINT | 44.6% | 1 |  |
| functcd | BIGINT | 44.1% | 24 |  |
| fstat | BIGINT | 44.6% | 5 |  |
| typecd | BIGINT | 99.5% | 1 |  |
| xfstat1 | VARCHAR | 99.5% | R |  |
| fstat1 | BIGINT | 99.5% | 93 |  |
| xfstat2 | VARCHAR | 99.5% | R |  |
| fstat2 | BIGINT | 99.5% | 56 |  |
| xfstat3 | VARCHAR | 99.5% | R |  |
| fstat3 | BIGINT | 99.5% | 68 |  |
| xfstat4 | VARCHAR | 99.5% | Z |  |
| fstat4 | BIGINT | 99.5% | 0 |  |
| xfstat5 | VARCHAR | 99.5% | R |  |
| fstat5 | BIGINT | 99.5% | 217 |  |
| xfstat6 | VARCHAR | 99.5% | A |  |
| fstat6 | BIGINT | 99.5% | 0 |  |

## ef_a

Rows: 2,944,297

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 483018 | Primary institution ID, joins across all IPEDS tables |
| efalevel | BIGINT | 4.0% | 19 |  |
| line | BIGINT | 0.0% | 99 | Appears in 4 tables, common join key |
| section | BIGINT | 0.0% | 3 | Appears in 3 tables, common join key |
| lstudy | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| xeftotlt | VARCHAR | 25.9% | R |  |
| eftotlt | BIGINT | 25.9% | 7 |  |
| xeftotlm | VARCHAR | 25.9% | R |  |
| eftotlm | BIGINT | 25.9% | 1 |  |
| xeftotlw | VARCHAR | 25.9% | R |  |
| eftotlw | BIGINT | 25.9% | 6 |  |
| xefaiant | VARCHAR | 25.9% | R |  |
| efaiant | DOUBLE | 31.7% | 0.0 |  |
| xefaianm | VARCHAR | 25.9% | R |  |
| efaianm | DOUBLE | 31.7% | 0.0 |  |
| xefaianw | VARCHAR | 25.9% | R |  |
| efaianw | DOUBLE | 31.7% | 0.0 |  |
| xefasiat | VARCHAR | 25.9% | R |  |
| efasiat | DOUBLE | 31.7% | 0.0 |  |
| xefasiam | VARCHAR | 25.9% | R |  |
| efasiam | DOUBLE | 31.7% | 0.0 |  |
| xefasiaw | VARCHAR | 25.9% | R |  |
| efasiaw | DOUBLE | 31.7% | 0.0 |  |
| xefbkaat | VARCHAR | 25.9% | R |  |
| efbkaat | DOUBLE | 31.7% | 0.0 |  |
| xefbkaam | VARCHAR | 25.9% | R |  |
| efbkaam | DOUBLE | 31.7% | 0.0 |  |
| xefbkaaw | VARCHAR | 25.9% | R |  |
| efbkaaw | DOUBLE | 31.7% | 0.0 |  |
| xefhispt | VARCHAR | 25.9% | R |  |
| efhispt | DOUBLE | 31.7% | 0.0 |  |
| xefhispm | VARCHAR | 25.9% | R |  |
| efhispm | DOUBLE | 31.7% | 0.0 |  |
| xefhispw | VARCHAR | 25.9% | R |  |
| efhispw | DOUBLE | 31.7% | 0.0 |  |
| xefnhpit | VARCHAR | 25.9% | R |  |
| efnhpit | DOUBLE | 31.7% | 0.0 |  |
| xefnhpim | VARCHAR | 25.9% | R |  |
| efnhpim | DOUBLE | 31.7% | 0.0 |  |
| xefnhpiw | VARCHAR | 25.9% | R |  |
| efnhpiw | DOUBLE | 31.7% | 0.0 |  |
| xefwhitt | VARCHAR | 25.9% | R |  |
| efwhitt | DOUBLE | 31.7% | 6.0 |  |
| xefwhitm | VARCHAR | 25.9% | R |  |
| efwhitm | DOUBLE | 31.7% | 0.0 |  |
| xefwhitw | VARCHAR | 25.9% | R |  |
| efwhitw | DOUBLE | 31.7% | 6.0 |  |
| xef2mort | VARCHAR | 25.9% | R |  |
| ef2mort | DOUBLE | 31.7% | 0.0 |  |
| xef2morm | VARCHAR | 25.9% | R |  |
| ef2morm | DOUBLE | 31.7% | 0.0 |  |
| xef2morw | VARCHAR | 25.9% | R |  |
| ef2morw | DOUBLE | 31.7% | 0.0 |  |
| xefunknt | VARCHAR | 25.9% | R |  |
| efunknt | BIGINT | 25.9% | 1 |  |
| xefunknm | VARCHAR | 25.9% | R |  |
| efunknm | BIGINT | 25.9% | 1 |  |
| xefunknw | VARCHAR | 25.9% | R |  |
| efunknw | BIGINT | 25.9% | 0 |  |
| xefnralt | VARCHAR | 25.9% | R |  |
| efnralt | BIGINT | 25.9% | 0 |  |
| xefnralm | VARCHAR | 25.9% | R |  |
| efnralm | BIGINT | 25.9% | 0 |  |
| xefnralw | VARCHAR | 25.9% | R |  |
| efnralw | BIGINT | 25.9% | 0 |  |
| xefgndrun | VARCHAR | 92.2% | A |  |
| efgndrun | DOUBLE | 98.6% | 0.0 |  |
| xefgndran | VARCHAR | 92.2% | A |  |
| efgndran | DOUBLE | 99.6% | 0.0 |  |
| xefgndrua | VARCHAR | 92.2% | A |  |
| efgndrua | DOUBLE | 98.7% | 0.0 |  |
| xefgndrkn | VARCHAR | 92.2% | A |  |
| efgndrkn | DOUBLE | 98.7% | 2403.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xefgndru | VARCHAR | 96.1% | R |  |
| xefgndra | VARCHAR | 96.1% | A |  |
| xefgndru.1 | VARCHAR | 96.1% | R |  |
| xefgndrk | VARCHAR | 96.1% | R |  |
| xdvefait | VARCHAR | 90.9% | R |  |
| dvefait | BIGINT | 90.9% | 1 |  |
| xdvefaim | VARCHAR | 90.9% | R |  |
| dvefaim | BIGINT | 90.9% | 0 |  |
| xdvefaiw | VARCHAR | 90.9% | R |  |
| dvefaiw | BIGINT | 90.9% | 1 |  |
| xdvefapt | VARCHAR | 90.9% | R |  |
| dvefapt | BIGINT | 90.9% | 5 |  |
| xdvefapm | VARCHAR | 90.9% | R |  |
| dvefapm | BIGINT | 90.9% | 2 |  |
| xdvefapw | VARCHAR | 90.9% | R |  |
| dvefapw | BIGINT | 90.9% | 3 |  |
| xdvefbkt | VARCHAR | 90.9% | R |  |
| dvefbkt | BIGINT | 90.9% | 14 |  |
| xdvefbkm | VARCHAR | 90.9% | R |  |
| dvefbkm | BIGINT | 90.9% | 10 |  |
| xdvefbkw | VARCHAR | 90.9% | R |  |
| dvefbkw | BIGINT | 90.9% | 4 |  |
| xdvefhst | VARCHAR | 90.9% | R |  |
| dvefhst | BIGINT | 90.9% | 12 |  |
| xdvefhsm | VARCHAR | 90.9% | R |  |
| dvefhsm | BIGINT | 90.9% | 6 |  |
| xdvefhsw | VARCHAR | 90.9% | R |  |
| dvefhsw | BIGINT | 90.9% | 6 |  |
| xdvefwht | VARCHAR | 90.9% | R |  |
| dvefwht | BIGINT | 90.9% | 526 |  |
| xdvefwhm | VARCHAR | 90.9% | R |  |
| dvefwhm | BIGINT | 90.9% | 198 |  |
| xdvefwhw | VARCHAR | 90.9% | R |  |
| dvefwhw | BIGINT | 90.9% | 328 |  |
| xefrac19 | VARCHAR | 69.1% | R |  |
| efrace19 | DOUBLE | 72.1% | 1.0 |  |
| xefrac05 | VARCHAR | 65.1% | R |  |
| efrace05 | DOUBLE | 68.0% | 0.0 |  |
| xefrac06 | VARCHAR | 65.1% | R |  |
| efrace06 | DOUBLE | 68.0% | 1.0 |  |
| xefrac20 | VARCHAR | 69.1% | R |  |
| efrace20 | DOUBLE | 72.1% | 5.0 |  |
| xefrac07 | VARCHAR | 65.1% | R |  |
| efrace07 | DOUBLE | 68.0% | 2.0 |  |
| xefrac08 | VARCHAR | 65.1% | R |  |
| efrace08 | DOUBLE | 68.0% | 3.0 |  |
| xefrac18 | VARCHAR | 69.1% | R |  |
| efrace18 | DOUBLE | 72.1% | 14.0 |  |
| xefrac03 | VARCHAR | 65.1% | R |  |
| efrace03 | DOUBLE | 68.0% | 10.0 |  |
| xefrac04 | VARCHAR | 65.1% | R |  |
| efrace04 | DOUBLE | 68.0% | 4.0 |  |
| xefrac21 | VARCHAR | 69.1% | R |  |
| efrace21 | DOUBLE | 72.1% | 12.0 |  |
| xefrac09 | VARCHAR | 65.1% | R |  |
| efrace09 | DOUBLE | 68.0% | 6.0 |  |
| xefrac10 | VARCHAR | 65.1% | R |  |
| efrace10 | DOUBLE | 68.0% | 6.0 |  |
| xefrac22 | VARCHAR | 69.1% | R |  |
| efrace22 | DOUBLE | 72.1% | 526.0 |  |
| xefrac11 | VARCHAR | 65.1% | R |  |
| efrace11 | DOUBLE | 68.0% | 198.0 |  |
| xefrac12 | VARCHAR | 65.1% | R |  |
| efrace12 | DOUBLE | 68.0% | 328.0 |  |
| xefrac01 | VARCHAR | 74.1% | Z |  |
| efrace01 | BIGINT | 74.1% | 0 |  |
| xefrac02 | VARCHAR | 74.1% | Z |  |
| efrace02 | BIGINT | 74.1% | 0 |  |
| xefrac13 | VARCHAR | 74.1% | Z |  |
| efrace13 | BIGINT | 74.1% | 0 |  |
| xefrac14 | VARCHAR | 74.1% | Z |  |
| efrace14 | BIGINT | 74.1% | 0 |  |
| xefrac15 | VARCHAR | 74.1% | R |  |
| efrace15 | BIGINT | 74.1% | 1564 |  |
| xefrac16 | VARCHAR | 74.1% | R |  |
| efrace16 | BIGINT | 74.1% | 477 |  |
| xefrac17 | VARCHAR | 78.2% | Z |  |
| efrace17 | BIGINT | 78.2% | 0 |  |
| xefrac23 | VARCHAR | 78.2% | Z |  |
| efrace23 | BIGINT | 78.2% | 0 |  |
| xefrac24 | VARCHAR | 78.2% | R |  |
| efrace24 | BIGINT | 78.2% | 2041 |  |

## ef_b

Rows: 3,365,326

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100663 | Primary institution ID, joins across all IPEDS tables |
| efbage | BIGINT | 6.2% | 1 |  |
| line | BIGINT | 0.0% | 412 | Appears in 4 tables, common join key |
| lstudy | BIGINT | 2.2% | 1 | Appears in 3 tables, common join key |
| xefage01 | VARCHAR | 0.0% | R |  |
| efage01 | DOUBLE | 0.2% | 5719.0 |  |
| xefage02 | VARCHAR | 0.0% | R |  |
| efage02 | DOUBLE | 0.1% | 8960.0 |  |
| xefage03 | VARCHAR | 6.2% | R |  |
| efage03 | DOUBLE | 9.5% | 2142.0 |  |
| xefage04 | VARCHAR | 6.2% | R |  |
| efage04 | DOUBLE | 9.5% | 4084.0 |  |
| xefage05 | VARCHAR | 6.2% | R |  |
| efage05 | DOUBLE | 6.3% | 14679.0 |  |
| xefage06 | VARCHAR | 6.2% | R |  |
| efage06 | DOUBLE | 9.5% | 6226.0 |  |
| xefage07 | VARCHAR | 6.2% | R |  |
| efage07 | BIGINT | 6.2% | 7861 |  |
| xefage08 | VARCHAR | 6.2% | R |  |
| efage08 | BIGINT | 6.2% | 13044 |  |
| xefage09 | VARCHAR | 6.2% | R |  |
| efage09 | BIGINT | 6.2% | 20905 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| section | BIGINT | 97.8% | 1 | Appears in 3 tables, common join key |

## ef_c

Rows: 1,426,858

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| efcstate | BIGINT | 6.8% | 1 |  |
| line | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| xefres01 | VARCHAR | 0.0% | R |  |
| efres01 | BIGINT | 0.0% | 881 |  |
| xefres02 | VARCHAR | 0.0% | R |  |
| efres02 | DOUBLE | 2.2% | 464.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |

## ef_d

Rows: 151,360

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xgrcohrt | VARCHAR | 8.1% | R |  |
| grcohrt | DOUBLE | 39.5% | 1939.0 |  |
| xugenter | VARCHAR | 8.1% | R |  |
| ugentern | DOUBLE | 40.9% | 2205.0 |  |
| xpgrcohr | VARCHAR | 8.1% | R |  |
| pgrcohrt | DOUBLE | 41.0% | 88.0 |  |
| xrrftct | VARCHAR | 24.3% | R |  |
| rrftct | DOUBLE | 28.3% | 1976.0 |  |
| xrrftex | VARCHAR | 24.3% | R |  |
| rrftex | DOUBLE | 28.3% | 0.0 |  |
| xrrftin | VARCHAR | 64.7% | R |  |
| rrftin | DOUBLE | 66.8% | 0.0 |  |
| xrrftcta | VARCHAR | 24.3% | R |  |
| rrftcta | DOUBLE | 28.3% | 1976.0 |  |
| xret_nmf | VARCHAR | 24.3% | R |  |
| ret_nmf | DOUBLE | 28.3% | 1381.0 |  |
| xret_pcf | VARCHAR | 8.1% | R |  |
| ret_pcf | DOUBLE | 18.8% | 70.0 |  |
| xrrptct | VARCHAR | 24.3% | R |  |
| rrptct | DOUBLE | 46.0% | 14.0 |  |
| xrrptex | VARCHAR | 24.3% | R |  |
| rrptex | DOUBLE | 46.0% | 0.0 |  |
| xrrptin | VARCHAR | 64.7% | R |  |
| rrptin | DOUBLE | 77.4% | 0.0 |  |
| xrrptcta | VARCHAR | 24.3% | R |  |
| rrptcta | DOUBLE | 46.0% | 14.0 |  |
| xret_nmp | VARCHAR | 24.3% | R |  |
| ret_nmp | DOUBLE | 46.0% | 3.0 |  |
| xret_pcp | VARCHAR | 8.1% | R |  |
| ret_pcp | DOUBLE | 50.4% | 21.0 |  |
| xstufacr | VARCHAR | 32.4% | R |  |
| stufacr | DOUBLE | 32.4% | 19.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| fyrpyear | DOUBLE | 96.0% | 1.0 | Appears in 4 tables, common join key |
| xtostucu | VARCHAR | 96.0% | R |  |
| tostucu | DOUBLE | 96.0% | 20239.0 |  |
| xtostucg | VARCHAR | 96.0% | R |  |
| tostucg | DOUBLE | 97.5% | 3461.0 |  |
| xtostucp | VARCHAR | 96.0% | R |  |
| tostucp | DOUBLE | 97.8% | 661.0 |  |
| xcdactua | VARCHAR | 96.0% | R |  |
| cdactua | DOUBLE | 96.8% | 873152.0 |  |
| xcnactua | VARCHAR | 96.0% | B |  |
| cnactua | DOUBLE | 97.8% | 1141600.0 |  |
| xcdactga | VARCHAR | 96.0% | R |  |
| cdactga | DOUBLE | 97.8% | 111321.0 |  |

## effy

Rows: 954,918

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 483708 | Primary institution ID, joins across all IPEDS tables |
| effyalev | BIGINT | 29.8% | 20 |  |
| effylev | BIGINT | 0.0% | -2 |  |
| lstudy | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| xeytotlt | VARCHAR | 9.7% | R |  |
| efytotlt | BIGINT | 9.7% | 579 |  |
| xeytotlm | VARCHAR | 9.7% | R |  |
| efytotlm | BIGINT | 9.7% | 103 |  |
| xeytotlw | VARCHAR | 9.7% | R |  |
| efytotlw | BIGINT | 9.7% | 476 |  |
| xefyaiat | VARCHAR | 9.7% | Z |  |
| efyaiant | DOUBLE | 12.5% | 0.0 |  |
| xefyaiam | VARCHAR | 9.7% | Z |  |
| efyaianm | DOUBLE | 12.5% | 0.0 |  |
| xefyaiaw | VARCHAR | 9.7% | Z |  |
| efyaianw | DOUBLE | 12.5% | 0.0 |  |
| xefyasit | VARCHAR | 9.7% | R |  |
| efyasiat | DOUBLE | 12.5% | 48.0 |  |
| xefyasim | VARCHAR | 9.7% | R |  |
| efyasiam | DOUBLE | 12.5% | 12.0 |  |
| xefyasiw | VARCHAR | 9.7% | R |  |
| efyasiaw | DOUBLE | 12.5% | 36.0 |  |
| xefybkat | VARCHAR | 9.7% | R |  |
| efybkaat | DOUBLE | 12.5% | 394.0 |  |
| xefybkam | VARCHAR | 9.7% | R |  |
| efybkaam | DOUBLE | 12.5% | 71.0 |  |
| xefybkaw | VARCHAR | 9.7% | R |  |
| efybkaaw | DOUBLE | 12.5% | 323.0 |  |
| xefyhist | VARCHAR | 9.7% | R |  |
| efyhispt | DOUBLE | 12.5% | 90.0 |  |
| xefyhism | VARCHAR | 9.7% | R |  |
| efyhispm | DOUBLE | 12.5% | 13.0 |  |
| xefyhisw | VARCHAR | 9.7% | R |  |
| efyhispw | DOUBLE | 12.5% | 77.0 |  |
| xefynhpt | VARCHAR | 9.7% | Z |  |
| efynhpit | DOUBLE | 12.5% | 0.0 |  |
| xefynhpm | VARCHAR | 9.7% | Z |  |
| efynhpim | DOUBLE | 12.5% | 0.0 |  |
| xefynhpw | VARCHAR | 9.7% | Z |  |
| efynhpiw | DOUBLE | 12.5% | 0.0 |  |
| xefywhit | VARCHAR | 9.7% | R |  |
| efywhitt | DOUBLE | 12.5% | 24.0 |  |
| xefywhim | VARCHAR | 9.7% | R |  |
| efywhitm | DOUBLE | 12.5% | 6.0 |  |
| xefywhiw | VARCHAR | 9.7% | R |  |
| efywhitw | DOUBLE | 12.5% | 18.0 |  |
| xefy2mot | VARCHAR | 9.7% | R |  |
| efy2mort | DOUBLE | 12.5% | 22.0 |  |
| xefy2mom | VARCHAR | 9.7% | R |  |
| efy2morm | DOUBLE | 12.5% | 1.0 |  |
| xefy2mow | VARCHAR | 9.7% | R |  |
| efy2morw | DOUBLE | 12.5% | 21.0 |  |
| xeyunknt | VARCHAR | 9.7% | R |  |
| efyunknt | BIGINT | 9.7% | 1 |  |
| xeyunknm | VARCHAR | 9.7% | Z |  |
| efyunknm | BIGINT | 9.7% | 0 |  |
| xeyunknw | VARCHAR | 9.7% | R |  |
| efyunknw | BIGINT | 9.7% | 1 |  |
| xeynralt | VARCHAR | 9.7% | Z |  |
| efynralt | BIGINT | 9.7% | 0 |  |
| xeynralm | VARCHAR | 9.7% | Z |  |
| efynralm | BIGINT | 9.7% | 0 |  |
| xeynralw | VARCHAR | 9.7% | Z |  |
| efynralw | BIGINT | 9.7% | 0 |  |
| xefyguun | VARCHAR | 51.5% | A |  |
| efyguun | DOUBLE | 94.3% | 0.0 |  |
| xefygukn | VARCHAR | 51.5% | A |  |
| efygukn | DOUBLE | 94.6% | 35.0 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| xefyguan | VARCHAR | 63.5% | A |  |
| efyguan | DOUBLE | 99.1% | 0.0 |  |
| xefyguto | VARCHAR | 63.5% | R |  |
| efygutot | DOUBLE | 96.0% | 0.0 |  |
| xfyrac03 | VARCHAR | 85.3% | R |  |
| fyrace03 | DOUBLE | 87.3% | 2533.0 |  |
| xfyrac04 | VARCHAR | 85.3% | R |  |
| fyrace04 | DOUBLE | 87.3% | 3028.0 |  |
| xfyrac05 | VARCHAR | 85.3% | R |  |
| fyrace05 | DOUBLE | 87.3% | 8.0 |  |
| xfyrac06 | VARCHAR | 85.3% | R |  |
| fyrace06 | DOUBLE | 87.3% | 7.0 |  |
| xfyrac07 | VARCHAR | 85.3% | R |  |
| fyrace07 | DOUBLE | 87.3% | 12.0 |  |
| xfyrac08 | VARCHAR | 85.3% | R |  |
| fyrace08 | DOUBLE | 87.3% | 17.0 |  |
| xfyrac09 | VARCHAR | 85.3% | R |  |
| fyrace09 | DOUBLE | 87.3% | 13.0 |  |
| xfyrac10 | VARCHAR | 85.3% | R |  |
| fyrace10 | DOUBLE | 87.3% | 19.0 |  |
| xfyrac11 | VARCHAR | 85.3% | R |  |
| fyrace11 | DOUBLE | 87.3% | 152.0 |  |
| xfyrac12 | VARCHAR | 85.3% | R |  |
| fyrace12 | DOUBLE | 87.3% | 230.0 |  |
| xfyrac18 | VARCHAR | 85.3% | R |  |
| fyrace18 | DOUBLE | 87.3% | 5561.0 |  |
| xfyrac19 | VARCHAR | 85.3% | R |  |
| fyrace19 | DOUBLE | 87.3% | 15.0 |  |
| xfyrac20 | VARCHAR | 85.3% | R |  |
| fyrace20 | DOUBLE | 87.3% | 29.0 |  |
| xfyrac21 | VARCHAR | 85.3% | R |  |
| fyrace21 | DOUBLE | 87.3% | 32.0 |  |
| xfyrac22 | VARCHAR | 85.3% | R |  |
| fyrace22 | DOUBLE | 87.3% | 382.0 |  |
| xdveyait | VARCHAR | 95.0% | R |  |
| dveyait | BIGINT | 95.0% | 15 |  |
| xdveyaim | VARCHAR | 95.0% | R |  |
| dveyaim | BIGINT | 95.0% | 8 |  |
| xdveyaiw | VARCHAR | 95.0% | R |  |
| dveyaiw | BIGINT | 95.0% | 7 |  |
| xdveyapt | VARCHAR | 95.0% | R |  |
| dveyapt | BIGINT | 95.0% | 29 |  |
| xdveyapm | VARCHAR | 95.0% | R |  |
| dveyapm | BIGINT | 95.0% | 12 |  |
| xdveyapw | VARCHAR | 95.0% | R |  |
| dveyapw | BIGINT | 95.0% | 17 |  |
| xdveybkt | VARCHAR | 95.0% | R |  |
| dveybkt | BIGINT | 95.0% | 5561 |  |
| xdveybkm | VARCHAR | 95.0% | R |  |
| dveybkm | BIGINT | 95.0% | 2533 |  |
| xdveybkw | VARCHAR | 95.0% | R |  |
| dveybkw | BIGINT | 95.0% | 3028 |  |
| xdveyhst | VARCHAR | 95.0% | R |  |
| dveyhst | BIGINT | 95.0% | 32 |  |
| xdveyhsm | VARCHAR | 95.0% | R |  |
| dveyhsm | BIGINT | 95.0% | 13 |  |
| xdveyhsw | VARCHAR | 95.0% | R |  |
| dveyhsw | BIGINT | 95.0% | 19 |  |
| xdveywht | VARCHAR | 95.0% | R |  |
| dveywht | BIGINT | 95.0% | 382 |  |
| xdveywhm | VARCHAR | 95.0% | R |  |
| dveywhm | BIGINT | 95.0% | 152 |  |
| xdveywhw | VARCHAR | 95.0% | R |  |
| dveywhw | BIGINT | 95.0% | 230 |  |
| xfyrac01 | VARCHAR | 90.3% | Z |  |
| fyrace01 | BIGINT | 90.3% | 0 |  |
| xfyrac02 | VARCHAR | 90.3% | Z |  |
| fyrace02 | BIGINT | 90.3% | 0 |  |
| xfyrac13 | VARCHAR | 90.3% | R |  |
| fyrace13 | BIGINT | 90.3% | 12965 |  |
| xfyrac14 | VARCHAR | 90.3% | R |  |
| fyrace14 | BIGINT | 90.3% | 3683 |  |
| xfyrac15 | VARCHAR | 90.3% | R |  |
| fyrace15 | BIGINT | 90.3% | 268053 |  |
| xfyrac16 | VARCHAR | 90.3% | R |  |
| fyrace16 | BIGINT | 90.3% | 64042 |  |
| xfyrac17 | VARCHAR | 90.3% | Z |  |
| fyrace17 | BIGINT | 90.3% | 0 |  |
| xfyrac23 | VARCHAR | 90.3% | R |  |
| fyrace23 | BIGINT | 90.3% | 16648 |  |
| xfyrac24 | VARCHAR | 90.3% | R |  |
| fyrace24 | BIGINT | 90.3% | 332095 |  |

## efia

Rows: 160,588

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xcdactua | VARCHAR | 0.0% | R |  |
| cdactua | DOUBLE | 31.9% | 168861.0 |  |
| xcnactua | VARCHAR | 0.0% | A |  |
| cnactua | DOUBLE | 62.7% | 85812.0 |  |
| xcdactga | VARCHAR | 0.0% | R |  |
| cdactga | DOUBLE | 68.4% | 16596.0 |  |
| xefteug | VARCHAR | 8.1% | G |  |
| efteug | DOUBLE | 12.1% | 5629.0 |  |
| xeftegd | VARCHAR | 8.1% | G |  |
| eftegd | DOUBLE | 71.9% | 692.0 |  |
| xfteug | VARCHAR | 8.1% | G |  |
| fteug | DOUBLE | 12.1% | 5629.0 |  |
| xftegd | VARCHAR | 8.1% | G |  |
| ftegd | DOUBLE | 71.9% | 692.0 |  |
| xftedpp | VARCHAR | 42.5% | A |  |
| ftedpp | DOUBLE | 93.2% | 1606.0 |  |
| acttype | BIGINT | 8.1% | 2 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |

## f1a

Rows: 44,245

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xf1a01 | VARCHAR | 0.0% | R |  |
| f1a01 | DOUBLE | 19.2% | 180654640.0 |  |
| xf1a31 | VARCHAR | 24.3% | R |  |
| f1a31 | DOUBLE | 41.4% | 233194452.0 |  |
| xf1a04 | VARCHAR | 0.0% | R |  |
| f1a04 | DOUBLE | 19.2% | 0.0 |  |
| xf1a05 | VARCHAR | 0.0% | R |  |
| f1a05 | DOUBLE | 19.2% | 233194452.0 |  |
| xf1a06 | VARCHAR | 0.0% | R |  |
| f1a06 | DOUBLE | 19.2% | 413849092.0 |  |
| xf1a19 | VARCHAR | 60.3% | R |  |
| f1a19 | DOUBLE | 69.4% | 31296759.0 |  |
| xf1a07 | VARCHAR | 0.0% | R |  |
| f1a07 | DOUBLE | 19.2% | 0.0 |  |
| xf1a08 | VARCHAR | 0.0% | R |  |
| f1a08 | DOUBLE | 19.2% | 99445116.0 |  |
| xf1a09 | VARCHAR | 0.0% | R |  |
| f1a09 | DOUBLE | 19.2% | 99445116.0 |  |
| xf1a10 | VARCHAR | 0.0% | R |  |
| f1a10 | DOUBLE | 19.2% | 73285311.0 |  |
| xf1a11 | VARCHAR | 0.0% | R |  |
| f1a11 | DOUBLE | 19.2% | 121457201.0 |  |
| xf1a12 | VARCHAR | 0.0% | R |  |
| f1a12 | DOUBLE | 19.2% | 194742512.0 |  |
| xf1a13 | VARCHAR | 0.0% | R |  |
| f1a13 | DOUBLE | 19.2% | 294187628.0 |  |
| xf1a20 | VARCHAR | 60.3% | R |  |
| f1a20 | DOUBLE | 69.4% | 35223353.0 |  |
| xf1a14 | VARCHAR | 0.0% | R |  |
| f1a14 | DOUBLE | 19.2% | 161096091.0 |  |
| xf1a15 | VARCHAR | 0.0% | R |  |
| f1a15 | DOUBLE | 19.2% | -72898379.0 |  |
| xf1a16 | VARCHAR | 0.0% | R |  |
| f1a16 | DOUBLE | 19.2% | 27536158.0 |  |
| xf1a17 | VARCHAR | 0.0% | R |  |
| f1a17 | DOUBLE | 19.2% | 1000.0 |  |
| xf1a18 | VARCHAR | 0.0% | R |  |
| f1a18 | DOUBLE | 19.2% | 115734870.0 |  |
| xf1a214 | VARCHAR | 0.0% | R |  |
| f1a214 | DOUBLE | 19.2% | 11066543.0 |  |
| xf1a224 | VARCHAR | 0.0% | Z |  |
| f1a224 | DOUBLE | 19.2% | 0.0 |  |
| xf1a234 | VARCHAR | 0.0% | R |  |
| f1a234 | DOUBLE | 19.2% | 319154721.0 |  |
| xf1a324 | VARCHAR | 24.3% | R |  |
| f1a324 | DOUBLE | 46.7% | 44319348.0 |  |
| xf1a274 | VARCHAR | 0.0% | R |  |
| f1a274 | DOUBLE | 19.2% | 18672016.0 |  |
| xf1a27t4 | VARCHAR | 28.8% | R |  |
| f1a27t4 | DOUBLE | 45.2% | 393212628.0 |  |
| xf1a284 | VARCHAR | 0.0% | R |  |
| f1a284 | DOUBLE | 19.2% | 166678750.0 |  |
| xf1a334 | VARCHAR | 24.3% | Z |  |
| f1a334 | DOUBLE | 46.7% | 0.0 |  |
| xf1a344 | VARCHAR | 24.3% | R |  |
| f1a344 | DOUBLE | 46.7% | 6660573.0 |  |
| xf1d01 | VARCHAR | 0.0% | R |  |
| f1d01 | DOUBLE | 15.1% | 236433604.0 |  |
| xf1d02 | VARCHAR | 0.0% | R |  |
| f1d02 | DOUBLE | 15.1% | 261700182.0 |  |
| xf1d03 | VARCHAR | 0.0% | R |  |
| f1d03 | DOUBLE | 15.5% | -25266578.0 |  |
| xf1d04 | VARCHAR | 0.0% | R |  |
| f1d04 | DOUBLE | 19.2% | 141433143.0 |  |
| xf1d05 | VARCHAR | 0.0% | R |  |
| f1d05 | DOUBLE | 19.2% | -431695.0 |  |
| xf1d06 | VARCHAR | 0.0% | R |  |
| f1d06 | DOUBLE | 19.2% | 115734870.0 |  |
| xf1b01 | VARCHAR | 0.0% | R |  |
| f1b01 | BIGINT | 0.0% | 43172609 |  |
| xf1b02 | VARCHAR | 0.0% | R |  |
| f1b02 | BIGINT | 0.0% | 40073931 |  |
| xf1b03 | VARCHAR | 0.0% | R |  |
| f1b03 | BIGINT | 0.0% | 2479144 |  |
| xf1b04 | VARCHAR | 0.0% | R |  |
| f1b04 | BIGINT | 0.0% | 0 |  |
| xf1b04a | VARCHAR | 24.3% | R |  |
| f1b04a | DOUBLE | 30.4% | 0.0 |  |
| xf1b04b | VARCHAR | 24.3% | R |  |
| f1b04b | DOUBLE | 30.4% | 0.0 |  |
| xf1b05 | VARCHAR | 0.0% | R |  |
| f1b05 | DOUBLE | 10.0% | 37885576.0 |  |
| xf1b06 | VARCHAR | 0.0% | R |  |
| f1b06 | DOUBLE | 57.7% | 0.0 |  |
| xf1b26 | VARCHAR | 24.3% | R |  |
| f1b26 | DOUBLE | 30.4% | 1632297.0 |  |
| xf1b07 | VARCHAR | 0.0% | R |  |
| f1b07 | DOUBLE | 57.8% | 0.0 |  |
| xf1b08 | VARCHAR | 0.0% | R |  |
| f1b08 | DOUBLE | 0.0% | 4781669.0 |  |
| xf1b09 | VARCHAR | 0.0% | R |  |
| f1b09 | DOUBLE | 0.0% | 130025226.0 |  |
| xf1b10 | VARCHAR | 0.0% | R |  |
| f1b10 | BIGINT | 0.0% | 3190075 |  |
| xf1b11 | VARCHAR | 0.0% | R |  |
| f1b11 | BIGINT | 0.0% | 75401110 |  |
| xf1b12 | VARCHAR | 0.0% | Z |  |
| f1b12 | BIGINT | 0.0% | 0 |  |
| xf1b13 | VARCHAR | 0.0% | R |  |
| f1b13 | BIGINT | 0.0% | 24113450 |  |
| xf1b14 | VARCHAR | 0.0% | R |  |
| f1b14 | BIGINT | 0.0% | 0 |  |
| xf1b15 | VARCHAR | 0.0% | R |  |
| f1b15 | BIGINT | 0.0% | 0 |  |
| xf1b16 | VARCHAR | 0.0% | R |  |
| f1b16 | BIGINT | 0.0% | 770000 |  |
| xf1b17 | VARCHAR | 0.0% | R |  |
| f1b17 | DOUBLE | 0.0% | 2933743.0 |  |
| xf1b18 | VARCHAR | 0.0% | R |  |
| f1b18 | DOUBLE | 0.0% | 0.0 |  |
| xf1b19 | VARCHAR | 0.0% | R |  |
| f1b19 | DOUBLE | 0.0% | 106408378.0 |  |
| xf1b27 | VARCHAR | 33.2% | R |  |
| f1b27 | DOUBLE | 33.2% | 236433604.0 |  |
| xf1b20 | VARCHAR | 0.0% | R |  |
| f1b20 | DOUBLE | 11.4% | 0.0 |  |
| xf1b21 | VARCHAR | 0.0% | R |  |
| f1b21 | DOUBLE | 11.4% | 0.0 |  |
| xf1b22 | VARCHAR | 0.0% | R |  |
| f1b22 | DOUBLE | 11.4% | 0.0 |  |
| xf1b23 | VARCHAR | 0.0% | R |  |
| f1b23 | DOUBLE | 4.4% | 0.0 |  |
| xf1b24 | VARCHAR | 0.0% | R |  |
| f1b24 | DOUBLE | 0.0% | 0.0 |  |
| xf1b25 | VARCHAR | 0.0% | R |  |
| f1b25 | DOUBLE | 0.0% | 236433604.0 |  |
| xf1c011 | VARCHAR | 0.0% | R |  |
| f1c011 | DOUBLE | 0.0% | 40523298.0 |  |
| xf1c012 | VARCHAR | 0.0% | R |  |
| f1c012 | DOUBLE | 0.0% | 28933351.0 |  |
| xf1c021 | VARCHAR | 0.0% | R |  |
| f1c021 | DOUBLE | 0.0% | 18543915.0 |  |
| xf1c022 | VARCHAR | 0.0% | R |  |
| f1c022 | DOUBLE | 0.0% | 8247734.0 |  |
| xf1c031 | VARCHAR | 0.0% | R |  |
| f1c031 | DOUBLE | 0.0% | 15261698.0 |  |
| xf1c032 | VARCHAR | 0.0% | R |  |
| f1c032 | DOUBLE | 0.0% | 6611987.0 |  |
| xf1c051 | VARCHAR | 0.0% | R |  |
| f1c051 | DOUBLE | 0.0% | 9702741.0 |  |
| xf1c052 | VARCHAR | 0.0% | R |  |
| f1c052 | DOUBLE | 0.0% | 5545999.0 |  |
| xf1c061 | VARCHAR | 0.0% | R |  |
| f1c061 | DOUBLE | 0.0% | 24038627.0 |  |
| xf1c062 | VARCHAR | 0.0% | R |  |
| f1c062 | DOUBLE | 0.0% | 6616437.0 |  |
| xf1c071 | VARCHAR | 0.0% | R |  |
| f1c071 | DOUBLE | 0.0% | 19857772.0 |  |
| xf1c072 | VARCHAR | 0.0% | R |  |
| f1c072 | DOUBLE | 0.0% | 8771044.0 |  |
| xf1c101 | VARCHAR | 0.0% | R |  |
| f1c101 | DOUBLE | 0.2% | 31335949.0 |  |
| xf1c111 | VARCHAR | 0.0% | R |  |
| f1c111 | DOUBLE | 11.4% | 46013258.0 |  |
| xf1c112 | VARCHAR | 0.0% | R |  |
| f1c112 | DOUBLE | 11.4% | 6875696.0 |  |
| xf1c121 | VARCHAR | 0.0% | R |  |
| f1c121 | DOUBLE | 57.8% | 0.0 |  |
| xf1c122 | VARCHAR | 0.0% | Z |  |
| f1c122 | DOUBLE | 57.8% | 0.0 |  |
| xf1c131 | VARCHAR | 0.0% | R |  |
| f1c131 | DOUBLE | 57.8% | 0.0 |  |
| xf1c132 | VARCHAR | 0.0% | Z |  |
| f1c132 | DOUBLE | 57.8% | 0.0 |  |
| xf1c141 | VARCHAR | 0.0% | R |  |
| f1c141 | DOUBLE | 0.0% | 56422924.0 |  |
| xf1c142 | VARCHAR | 0.0% | R |  |
| f1c142 | DOUBLE | 0.0% | 2963587.0 |  |
| xf1c191 | VARCHAR | 0.0% | R |  |
| f1c191 | DOUBLE | 0.0% | 261700182.0 |  |
| xf1c192 | VARCHAR | 0.0% | R |  |
| f1c192 | DOUBLE | 0.0% | 74565835.0 |  |
| xf1c193 | VARCHAR | 0.0% | R |  |
| f1c193 | DOUBLE | 0.0% | 31320233.0 |  |
| xf1c19om | VARCHAR | 60.3% | R |  |
| f1c19om | BIGINT | 60.3% | 3003715 |  |
| xf1c19dp | VARCHAR | 60.3% | R |  |
| f1c19dp | BIGINT | 60.3% | 12403501 |  |
| xf1c19in | VARCHAR | 60.3% | R |  |
| f1c19in | BIGINT | 60.3% | 124167 |  |
| xf1c19ot | VARCHAR | 60.3% | R |  |
| f1c19ot | DOUBLE | 60.3% | 140282731.0 |  |
| f1mhp | BIGINT | 55.9% | 1 |  |
| xf1m01 | VARCHAR | 55.9% | R |  |
| f1m01 | DOUBLE | 68.4% | 15424000.0 |  |
| xf1m02 | VARCHAR | 55.9% | R |  |
| f1m02 | DOUBLE | 68.4% | 108151000.0 |  |
| xf1m03 | VARCHAR | 55.9% | R |  |
| f1m03 | DOUBLE | 68.4% | 4004000.0 |  |
| xf1m04 | VARCHAR | 55.9% | R |  |
| f1m04 | DOUBLE | 68.4% | 20778000.0 |  |
| f1mhop | BIGINT | 78.2% | 1 |  |
| xf1m05 | VARCHAR | 73.7% | R |  |
| f1m05 | DOUBLE | 82.1% | 6154695.0 |  |
| xf1m06 | VARCHAR | 73.7% | R |  |
| f1m06 | DOUBLE | 82.1% | 10313493.0 |  |
| xf1m07 | VARCHAR | 73.7% | R |  |
| f1m07 | DOUBLE | 82.1% | 31219353.0 |  |
| xf1m08 | VARCHAR | 73.7% | R |  |
| f1m08 | DOUBLE | 82.1% | 10518759.0 |  |
| xf1e01 | VARCHAR | 0.0% | R |  |
| f1e01 | DOUBLE | 3.0% | 24113450.0 |  |
| xf1e02 | VARCHAR | 0.0% | R |  |
| f1e02 | DOUBLE | 3.0% | 15478750.0 |  |
| xf1e03 | VARCHAR | 0.0% | R |  |
| f1e03 | DOUBLE | 3.0% | 2479144.0 |  |
| xf1e04 | VARCHAR | 0.0% | R |  |
| f1e04 | DOUBLE | 3.0% | 0.0 |  |
| xf1e05 | VARCHAR | 0.0% | R |  |
| f1e05 | DOUBLE | 3.0% | 457823.0 |  |
| xf1e06 | VARCHAR | 0.0% | R |  |
| f1e06 | DOUBLE | 3.0% | 20327025.0 |  |
| xf1e07 | VARCHAR | 0.0% | R |  |
| f1e07 | DOUBLE | 3.0% | 62856192.0 |  |
| xf1e08 | VARCHAR | 0.0% | R |  |
| f1e08 | DOUBLE | 3.0% | 31520243.0 |  |
| xf1e09 | VARCHAR | 0.0% | R |  |
| f1e09 | DOUBLE | 3.0% | 0.0 |  |
| xf1e10 | VARCHAR | 0.0% | R |  |
| f1e10 | DOUBLE | 3.0% | 31520243.0 |  |
| xf1e11 | VARCHAR | 0.0% | R |  |
| f1e11 | DOUBLE | 2.8% | 31335949.0 |  |
| xf1e12 | VARCHAR | 78.2% | R |  |
| f1e12 | DOUBLE | 78.9% | 0.0 |  |
| xf1e121 | VARCHAR | 78.2% | R |  |
| f1e121 | DOUBLE | 78.9% | 0.0 |  |
| xf1e122 | VARCHAR | 78.2% | R |  |
| f1e122 | DOUBLE | 78.9% | 0.0 |  |
| xf1e13 | VARCHAR | 78.2% | R |  |
| f1e13 | DOUBLE | 78.9% | 277340.0 |  |
| xf1e131 | VARCHAR | 78.2% | R |  |
| f1e131 | DOUBLE | 78.9% | 277340.0 |  |
| xf1e132 | VARCHAR | 78.2% | Z |  |
| f1e132 | DOUBLE | 78.9% | 0.0 |  |
| xf1e14 | VARCHAR | 78.2% | R |  |
| f1e14 | DOUBLE | 78.9% | 58478.0 |  |
| xf1e141 | VARCHAR | 78.2% | R |  |
| f1e141 | DOUBLE | 78.9% | 58478.0 |  |
| xf1e142 | VARCHAR | 78.2% | Z |  |
| f1e142 | DOUBLE | 78.9% | 0.0 |  |
| xf1e15 | VARCHAR | 78.2% | R |  |
| f1e15 | DOUBLE | 78.9% | 0.0 |  |
| xf1e151 | VARCHAR | 78.2% | Z |  |
| f1e151 | DOUBLE | 78.9% | 0.0 |  |
| xf1e152 | VARCHAR | 78.2% | Z |  |
| f1e152 | DOUBLE | 78.9% | 0.0 |  |
| xf1e16 | VARCHAR | 78.2% | R |  |
| f1e16 | DOUBLE | 78.9% | 0.0 |  |
| xf1e161 | VARCHAR | 78.2% | Z |  |
| f1e161 | DOUBLE | 78.9% | 0.0 |  |
| xf1e162 | VARCHAR | 78.2% | Z |  |
| f1e162 | DOUBLE | 78.9% | 0.0 |  |
| xf1e17 | VARCHAR | 78.2% | R |  |
| f1e17 | DOUBLE | 78.9% | 31184425.0 |  |
| xf1e171 | VARCHAR | 78.2% | R |  |
| f1e171 | DOUBLE | 78.9% | 31184425.0 |  |
| xf1e172 | VARCHAR | 78.2% | R |  |
| f1e172 | DOUBLE | 78.9% | 0.0 |  |
| f1fha | BIGINT | 2.9% | 2 |  |
| xf1h01 | VARCHAR | 2.9% | A |  |
| f1h01 | DOUBLE | 36.3% | 739372914.0 |  |
| xf1h02 | VARCHAR | 2.9% | A |  |
| f1h02 | DOUBLE | 36.3% | 858989211.0 |  |
| xf1h03 | VARCHAR | 78.2% | A |  |
| f1h03 | DOUBLE | 84.9% | 119616297.0 |  |
| xf1h03a | VARCHAR | 78.2% | A |  |
| f1h03a | DOUBLE | 84.9% | 34676076.0 |  |
| xf1h03b | VARCHAR | 78.2% | A |  |
| f1h03b | DOUBLE | 84.9% | 84940221.0 |  |
| xf1h03c | VARCHAR | 78.2% | A |  |
| f1h03c | DOUBLE | 84.9% | -32303611.0 |  |
| xf1h03d | VARCHAR | 78.2% | A |  |
| f1h03d | DOUBLE | 84.9% | 32303611.0 |  |
| xf1n01 | VARCHAR | 78.2% | R |  |
| f1n01 | DOUBLE | 83.1% | 27984574.0 |  |
| xf1n02 | VARCHAR | 78.2% | R |  |
| f1n02 | DOUBLE | 83.1% | 235478590.0 |  |
| xf1n03 | VARCHAR | 78.2% | R |  |
| f1n03 | DOUBLE | 83.1% | -26221592.0 |  |
| xf1n04 | VARCHAR | 78.2% | R |  |
| f1n04 | DOUBLE | 83.1% | 115733869.0 |  |
| xf1n05 | VARCHAR | 78.2% | R |  |
| f1n05 | DOUBLE | 83.1% | -45362221.0 |  |
| xf1n06 | VARCHAR | 78.2% | R |  |
| f1n06 | DOUBLE | 83.1% | 68084358.0 |  |
| xf1n07 | VARCHAR | 78.2% | R |  |
| f1n07 | DOUBLE | 83.1% | 261700182.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xf1c013 | VARCHAR | 39.7% | R |  |
| f1c013 | DOUBLE | 39.7% | 6893526.0 |  |
| xf1c014 | VARCHAR | 39.7% | R |  |
| f1c014 | DOUBLE | 39.7% | 2169522.0 |  |
| xf1c015 | VARCHAR | 39.7% | R |  |
| f1c015 | DOUBLE | 39.7% | 1517879.0 |  |
| xf1c016 | VARCHAR | 64.0% | R |  |
| f1c016 | DOUBLE | 70.0% | 3812817.0 |  |
| xf1c017 | VARCHAR | 68.4% | R |  |
| f1c017 | DOUBLE | 70.9% | 600867.0 |  |
| xf1c023 | VARCHAR | 39.7% | R |  |
| f1c023 | DOUBLE | 39.7% | 723458.0 |  |
| xf1c024 | VARCHAR | 39.7% | R |  |
| f1c024 | DOUBLE | 39.7% | 515745.0 |  |
| xf1c025 | VARCHAR | 39.7% | R |  |
| f1c025 | DOUBLE | 39.7% | 3127149.0 |  |
| xf1c026 | VARCHAR | 64.0% | R |  |
| f1c026 | DOUBLE | 70.0% | 906393.0 |  |
| xf1c027 | VARCHAR | 68.4% | R |  |
| f1c027 | DOUBLE | 70.9% | 142840.0 |  |
| xf1c033 | VARCHAR | 39.7% | R |  |
| f1c033 | DOUBLE | 39.7% | 2717021.0 |  |
| xf1c034 | VARCHAR | 39.7% | R |  |
| f1c034 | DOUBLE | 39.7% | 1085519.0 |  |
| xf1c035 | VARCHAR | 39.7% | R |  |
| f1c035 | DOUBLE | 39.7% | 4438690.0 |  |
| xf1c036 | VARCHAR | 64.0% | R |  |
| f1c036 | DOUBLE | 70.0% | 1907742.0 |  |
| xf1c037 | VARCHAR | 68.4% | R |  |
| f1c037 | DOUBLE | 70.9% | 300644.0 |  |
| xf1c053 | VARCHAR | 39.7% | R |  |
| f1c053 | DOUBLE | 39.7% | 926940.0 |  |
| xf1c054 | VARCHAR | 39.7% | R |  |
| f1c054 | DOUBLE | 39.7% | 443039.0 |  |
| xf1c055 | VARCHAR | 39.7% | R |  |
| f1c055 | DOUBLE | 39.7% | 2291192.0 |  |
| xf1c056 | VARCHAR | 64.0% | R |  |
| f1c056 | DOUBLE | 70.0% | 778618.0 |  |
| xf1c057 | VARCHAR | 68.4% | R |  |
| f1c057 | DOUBLE | 70.9% | 122703.0 |  |
| xf1c063 | VARCHAR | 39.7% | R |  |
| f1c063 | DOUBLE | 39.7% | 2238420.0 |  |
| xf1c064 | VARCHAR | 39.7% | R |  |
| f1c064 | DOUBLE | 39.7% | 1014962.0 |  |
| xf1c065 | VARCHAR | 39.7% | R |  |
| f1c065 | DOUBLE | 39.7% | 5195576.0 |  |
| xf1c066 | VARCHAR | 64.0% | R |  |
| f1c066 | DOUBLE | 70.0% | 1783741.0 |  |
| xf1c067 | VARCHAR | 68.4% | R |  |
| f1c067 | DOUBLE | 70.9% | 281102.0 |  |
| xf1c073 | VARCHAR | 39.7% | R |  |
| f1c073 | DOUBLE | 39.7% | 2905645.0 |  |
| xf1c074 | VARCHAR | 39.7% | R |  |
| f1c074 | DOUBLE | 39.7% | 1892470.0 |  |
| xf1c075 | VARCHAR | 39.7% | R |  |
| f1c075 | DOUBLE | 39.7% | 13067622.0 |  |
| xf1c076 | VARCHAR | 64.0% | R |  |
| f1c076 | DOUBLE | 70.0% | 3325913.0 |  |
| xf1c077 | VARCHAR | 68.4% | R |  |
| f1c077 | DOUBLE | 70.9% | 524135.0 |  |
| xf1c081 | VARCHAR | 44.2% | R |  |
| f1c081 | DOUBLE | 47.1% | 0.0 |  |
| xf1c082 | VARCHAR | 39.7% | R |  |
| f1c082 | DOUBLE | 39.7% | 336317.0 |  |
| xf1c083 | VARCHAR | 39.7% | R |  |
| f1c083 | DOUBLE | 39.7% | 124630.0 |  |
| xf1c084 | VARCHAR | 39.7% | R |  |
| f1c084 | DOUBLE | 39.7% | 0.0 |  |
| xf1c085 | VARCHAR | 39.7% | R |  |
| f1c085 | DOUBLE | 39.7% | 13382831.0 |  |
| xf1c086 | VARCHAR | 64.0% | R |  |
| f1c086 | DOUBLE | 70.0% | -13843778.0 |  |
| xf1c087 | VARCHAR | 68.4% | R |  |
| f1c087 | DOUBLE | 70.9% | 0.0 |  |
| xf1c105 | VARCHAR | 39.7% | R |  |
| f1c105 | DOUBLE | 39.9% | 16282814.0 |  |
| xf1c113 | VARCHAR | 39.7% | R |  |
| f1c113 | DOUBLE | 44.8% | 361251.0 |  |
| xf1c114 | VARCHAR | 39.7% | R |  |
| f1c114 | DOUBLE | 44.8% | 755957.0 |  |
| xf1c115 | VARCHAR | 39.7% | R |  |
| f1c115 | DOUBLE | 44.8% | 9009616.0 |  |
| xf1c116 | VARCHAR | 64.0% | R |  |
| f1c116 | DOUBLE | 75.2% | 1328554.0 |  |
| xf1c117 | VARCHAR | 68.4% | R |  |
| f1c117 | DOUBLE | 76.1% | 209369.0 |  |
| xf1c123 | VARCHAR | 39.7% | Z |  |
| f1c123 | DOUBLE | 72.9% | 0.0 |  |
| xf1c124 | VARCHAR | 39.7% | Z |  |
| f1c124 | DOUBLE | 72.9% | 0.0 |  |
| xf1c125 | VARCHAR | 39.7% | Z |  |
| f1c125 | DOUBLE | 72.9% | 0.0 |  |
| xf1c126 | VARCHAR | 64.0% | Z |  |
| f1c126 | DOUBLE | 90.3% | 0.0 |  |
| xf1c127 | VARCHAR | 68.4% | Z |  |
| f1c127 | DOUBLE | 90.5% | 0.0 |  |
| xf1c133 | VARCHAR | 39.7% | Z |  |
| f1c133 | DOUBLE | 72.9% | 0.0 |  |
| xf1c134 | VARCHAR | 39.7% | Z |  |
| f1c134 | DOUBLE | 72.9% | 0.0 |  |
| xf1c135 | VARCHAR | 39.7% | Z |  |
| f1c135 | DOUBLE | 72.9% | 0.0 |  |
| xf1c136 | VARCHAR | 64.0% | Z |  |
| f1c136 | DOUBLE | 90.3% | 0.0 |  |
| xf1c137 | VARCHAR | 68.4% | Z |  |
| f1c137 | DOUBLE | 90.5% | 0.0 |  |
| xf1c143 | VARCHAR | 39.7% | R |  |
| f1c143 | DOUBLE | 39.7% | 0.0 |  |
| xf1c144 | VARCHAR | 39.7% | R |  |
| f1c144 | DOUBLE | 39.7% | 0.0 |  |
| xf1c145 | VARCHAR | 39.7% | R |  |
| f1c145 | DOUBLE | 39.7% | 3143712.0 |  |
| xf1c146 | VARCHAR | 64.0% | R |  |
| f1c146 | DOUBLE | 70.0% | 0.0 |  |
| xf1c147 | VARCHAR | 68.4% | R |  |
| f1c147 | DOUBLE | 70.9% | 0.0 |  |
| xf1c194 | VARCHAR | 39.7% | R |  |
| f1c194 | DOUBLE | 39.7% | 7877214.0 |  |
| xf1c195 | VARCHAR | 39.7% | R |  |
| f1c195 | DOUBLE | 39.7% | 71457081.0 |  |
| xf1c196 | VARCHAR | 77.4% | R |  |
| f1c196 | BIGINT | 77.4% | 0 |  |
| xf1c197 | VARCHAR | 68.4% | R |  |
| f1c197 | DOUBLE | 70.9% | 2181660.0 |  |
| i | DOUBLE | 100.0% |  |  |
| xf1a02 | VARCHAR | 66.8% | R |  |
| f1a02 | DOUBLE | 72.5% | 202736045.0 |  |
| xf1a03 | VARCHAR | 66.8% | R |  |
| f1a03 | DOUBLE | 72.5% | 77530882.0 |  |
| xf1a211 | VARCHAR | 66.8% | R |  |
| f1a211 | DOUBLE | 72.5% | 4982207.0 |  |
| xf1a212 | VARCHAR | 66.8% | Z |  |
| f1a212 | DOUBLE | 72.5% | 0.0 |  |
| xf1a213 | VARCHAR | 66.8% | R |  |
| f1a213 | DOUBLE | 72.5% | 0.0 |  |
| xf1a221 | VARCHAR | 66.8% | Z |  |
| f1a221 | DOUBLE | 72.5% | 0.0 |  |
| xf1a222 | VARCHAR | 66.8% | Z |  |
| f1a222 | DOUBLE | 72.5% | 0.0 |  |
| xf1a223 | VARCHAR | 66.8% | Z |  |
| f1a223 | DOUBLE | 72.5% | 0.0 |  |
| xf1a231 | VARCHAR | 66.8% | R |  |
| f1a231 | DOUBLE | 72.5% | 141008356.0 |  |
| xf1a232 | VARCHAR | 66.8% | R |  |
| f1a232 | DOUBLE | 72.5% | 4020956.0 |  |
| xf1a233 | VARCHAR | 66.8% | R |  |
| f1a233 | DOUBLE | 72.5% | 0.0 |  |
| xf1a241 | VARCHAR | 66.8% | R |  |
| f1a241 | DOUBLE | 72.5% | 11306307.0 |  |
| xf1a242 | VARCHAR | 66.8% | R |  |
| f1a242 | DOUBLE | 72.5% | 206979.0 |  |
| xf1a243 | VARCHAR | 66.8% | R |  |
| f1a243 | DOUBLE | 72.5% | 0.0 |  |
| xf1a244 | VARCHAR | 66.8% | R |  |
| f1a244 | DOUBLE | 72.5% | 11513286.0 |  |
| xf1a251 | VARCHAR | 66.8% | R |  |
| f1a251 | DOUBLE | 72.5% | 13806677.0 |  |
| xf1a252 | VARCHAR | 66.8% | R |  |
| f1a252 | DOUBLE | 72.5% | 160376.0 |  |
| xf1a253 | VARCHAR | 66.8% | R |  |
| f1a253 | DOUBLE | 72.5% | 0.0 |  |
| xf1a254 | VARCHAR | 66.8% | R |  |
| f1a254 | DOUBLE | 72.5% | 13967053.0 |  |
| xf1a261 | VARCHAR | 66.8% | R |  |
| f1a261 | DOUBLE | 72.5% | 1883060.0 |  |
| xf1a262 | VARCHAR | 66.8% | Z |  |
| f1a262 | DOUBLE | 72.5% | 0.0 |  |
| xf1a263 | VARCHAR | 66.8% | R |  |
| f1a263 | DOUBLE | 72.5% | 1258149.0 |  |
| xf1a264 | VARCHAR | 66.8% | R |  |
| f1a264 | DOUBLE | 72.5% | 624911.0 |  |
| xf1a271 | VARCHAR | 66.8% | R |  |
| f1a271 | DOUBLE | 72.5% | 12688132.0 |  |
| xf1a272 | VARCHAR | 66.8% | R |  |
| f1a272 | DOUBLE | 72.5% | 14556055.0 |  |
| xf1a273 | VARCHAR | 66.8% | R |  |
| f1a273 | DOUBLE | 72.5% | 0.0 |  |
| xf1a27t1 | VARCHAR | 95.5% | R |  |
| f1a27t1 | DOUBLE | 97.7% | 185674739.0 |  |
| xf1a27t2 | VARCHAR | 95.5% | R |  |
| f1a27t2 | DOUBLE | 97.7% | 18944366.0 |  |
| xf1a27t3 | VARCHAR | 95.5% | R |  |
| f1a27t3 | DOUBLE | 97.7% | 1258149.0 |  |
| xf1a281 | VARCHAR | 66.8% | R |  |
| f1a281 | DOUBLE | 72.5% | 72609889.0 |  |
| xf1a282 | VARCHAR | 66.8% | R |  |
| f1a282 | DOUBLE | 72.5% | 4920993.0 |  |
| xf1a283 | VARCHAR | 66.8% | R |  |
| f1a283 | DOUBLE | 72.5% | 0.0 |  |
| xf1c091 | VARCHAR | 66.8% | R |  |
| f1c091 | DOUBLE | 69.6% | 4920993.0 |  |
| xf1c094 | VARCHAR | 66.8% | R |  |
| f1c094 | DOUBLE | 69.6% | 4920993.0 |  |
| xf1c102 | VARCHAR | 66.8% | A |  |
| f1c102 | DOUBLE | 93.4% | 0.0 |  |
| xf1c103 | VARCHAR | 66.8% | A |  |
| f1c103 | DOUBLE | 93.4% | 0.0 |  |
| xf1c104 | VARCHAR | 66.8% | A |  |
| f1c104 | DOUBLE | 93.4% | 0.0 |  |
| xf1c151 | VARCHAR | 66.8% | R |  |
| f1c151 | DOUBLE | 68.8% | 120384276.0 |  |
| xf1c152 | VARCHAR | 66.8% | R |  |
| f1c152 | DOUBLE | 68.8% | 57236714.0 |  |
| xf1c153 | VARCHAR | 66.8% | R |  |
| f1c153 | DOUBLE | 68.8% | 14981321.0 |  |
| xf1c154 | VARCHAR | 66.8% | R |  |
| f1c154 | DOUBLE | 68.8% | 4920993.0 |  |
| xf1c155 | VARCHAR | 66.8% | R |  |
| f1c155 | DOUBLE | 68.8% | 43245248.0 |  |
| xf1c161 | VARCHAR | 66.8% | R |  |
| f1c161 | DOUBLE | 68.8% | 2593617.0 |  |
| xf1c165 | VARCHAR | 66.8% | R |  |
| f1c165 | DOUBLE | 68.8% | 2593617.0 |  |
| xf1c171 | VARCHAR | 66.8% | R |  |
| f1c171 | DOUBLE | 68.8% | 0.0 |  |
| xf1c172 | VARCHAR | 66.8% | R |  |
| f1c172 | DOUBLE | 68.8% | 0.0 |  |
| xf1c173 | VARCHAR | 66.8% | R |  |
| f1c173 | DOUBLE | 68.8% | 0.0 |  |
| xf1c174 | VARCHAR | 66.8% | R |  |
| f1c174 | DOUBLE | 68.8% | 0.0 |  |
| xf1c175 | VARCHAR | 66.8% | R |  |
| f1c175 | DOUBLE | 68.8% | 0.0 |  |
| xf1c181 | VARCHAR | 66.8% | R |  |
| f1c181 | DOUBLE | 68.8% | 2593617.0 |  |
| xf1c182 | VARCHAR | 66.8% | R |  |
| f1c182 | DOUBLE | 68.8% | 0.0 |  |
| xf1c183 | VARCHAR | 66.8% | R |  |
| f1c183 | DOUBLE | 68.8% | 0.0 |  |
| xf1c184 | VARCHAR | 66.8% | R |  |
| f1c184 | DOUBLE | 68.8% | 0.0 |  |
| xf1c185 | VARCHAR | 66.8% | R |  |
| f1c185 | DOUBLE | 68.8% | 2593617.0 |  |

## f2

Rows: 44,704

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100690 | Primary institution ID, joins across all IPEDS tables |
| xf2a01 | VARCHAR | 0.0% | R |  |
| f2a01 | DOUBLE | 10.1% | 10536035.0 |  |
| xf2a19 | VARCHAR | 29.7% | R |  |
| f2a19 | DOUBLE | 42.9% | 2433432.0 |  |
| xf2a20 | VARCHAR | 29.7% | R |  |
| f2a20 | DOUBLE | 42.9% | 0.0 |  |
| xf2a02 | VARCHAR | 0.0% | R |  |
| f2a02 | DOUBLE | 10.1% | 16820592.0 |  |
| xf2a03 | VARCHAR | 0.0% | R |  |
| f2a03 | DOUBLE | 10.1% | 926932.0 |  |
| xf2a03a | VARCHAR | 29.7% | R |  |
| f2a03a | DOUBLE | 42.9% | 0.0 |  |
| xf2a04 | VARCHAR | 0.0% | R |  |
| f2a04 | DOUBLE | 10.1% | 15410339.0 |  |
| xf2a05 | VARCHAR | 0.0% | R |  |
| f2a05 | DOUBLE | 10.1% | 483321.0 |  |
| xf2a05a | VARCHAR | 12.8% | R |  |
| f2a05a | DOUBLE | 22.7% | 174864.0 |  |
| xf2a05b | VARCHAR | 29.7% | R |  |
| f2a05b | DOUBLE | 42.9% | 308457.0 |  |
| xf2a06 | VARCHAR | 0.0% | R |  |
| f2a06 | DOUBLE | 10.1% | 15893660.0 |  |
| xf2a11 | VARCHAR | 0.0% | R |  |
| f2a11 | DOUBLE | 10.1% | 1340625.0 |  |
| xf2a12 | VARCHAR | 0.0% | R |  |
| f2a12 | DOUBLE | 10.1% | 1065662.0 |  |
| xf2a13 | VARCHAR | 0.0% | R |  |
| f2a13 | DOUBLE | 10.1% | 3216469.0 |  |
| xf2a15 | VARCHAR | 29.7% | R |  |
| f2a15 | DOUBLE | 42.9% | 0.0 |  |
| xf2a16 | VARCHAR | 29.7% | R |  |
| f2a16 | DOUBLE | 42.9% | 0.0 |  |
| xf2a17 | VARCHAR | 29.7% | R |  |
| f2a17 | DOUBLE | 42.9% | 5622756.0 |  |
| xf2a18 | VARCHAR | 29.7% | R |  |
| f2a18 | DOUBLE | 42.9% | 3189324.0 |  |
| xf2b01 | VARCHAR | 0.0% | R |  |
| f2b01 | DOUBLE | 7.2% | 7840002.0 |  |
| xf2b02 | VARCHAR | 0.0% | R |  |
| f2b02 | DOUBLE | 7.2% | 7453320.0 |  |
| xf2b03 | VARCHAR | 0.0% | R |  |
| f2b03 | DOUBLE | 8.7% | 0.0 |  |
| xf2b04 | VARCHAR | 0.0% | R |  |
| f2b04 | DOUBLE | 9.9% | 386682.0 |  |
| xf2b05 | VARCHAR | 0.0% | R |  |
| f2b05 | DOUBLE | 9.9% | 15506978.0 |  |
| xf2b06 | VARCHAR | 0.0% | R |  |
| f2b06 | DOUBLE | 9.9% | 0.0 |  |
| xf2b07 | VARCHAR | 0.0% | R |  |
| f2b07 | DOUBLE | 9.9% | 15893660.0 |  |
| xf2c01 | VARCHAR | 0.0% | R |  |
| f2c01 | DOUBLE | 0.2% | 1.0 |  |
| xf2c02 | VARCHAR | 0.0% | R |  |
| f2c02 | DOUBLE | 0.2% | 13959.0 |  |
| xf2c03 | VARCHAR | 0.0% | R |  |
| f2c03 | DOUBLE | 0.2% | 0.0 |  |
| xf2c04 | VARCHAR | 0.0% | R |  |
| f2c04 | DOUBLE | 0.2% | 0.0 |  |
| xf2c05 | VARCHAR | 0.0% | R |  |
| f2c05 | DOUBLE | 0.2% | 0.0 |  |
| xf2c06 | VARCHAR | 0.0% | R |  |
| f2c06 | DOUBLE | 0.2% | 810026.0 |  |
| xf2c07 | VARCHAR | 0.0% | R |  |
| f2c07 | DOUBLE | 0.2% | 823986.0 |  |
| xf2c08 | VARCHAR | 0.0% | R |  |
| f2c08 | DOUBLE | 0.2% | 823985.0 |  |
| xf2c09 | VARCHAR | 0.0% | R |  |
| f2c09 | DOUBLE | 0.2% | 0.0 |  |
| xf2c10 | VARCHAR | 63.4% | R |  |
| f2c10 | DOUBLE | 63.4% | 823985.0 |  |
| xf2c12 | VARCHAR | 80.0% | R |  |
| f2c12 | DOUBLE | 80.1% | 0.0 |  |
| xf2c121 | VARCHAR | 80.0% | R |  |
| f2c121 | DOUBLE | 80.1% | 0.0 |  |
| xf2c122 | VARCHAR | 80.0% | R |  |
| f2c122 | DOUBLE | 80.1% | 0.0 |  |
| xf2c13 | VARCHAR | 80.0% | R |  |
| f2c13 | DOUBLE | 80.1% | 13959.0 |  |
| xf2c131 | VARCHAR | 80.0% | R |  |
| f2c131 | DOUBLE | 80.1% | 13959.0 |  |
| xf2c132 | VARCHAR | 80.0% | R |  |
| f2c132 | DOUBLE | 80.1% | 0.0 |  |
| xf2c14 | VARCHAR | 80.0% | R |  |
| f2c14 | DOUBLE | 80.1% | 0.0 |  |
| xf2c141 | VARCHAR | 80.0% | R |  |
| f2c141 | DOUBLE | 80.1% | 0.0 |  |
| xf2c142 | VARCHAR | 80.0% | R |  |
| f2c142 | DOUBLE | 80.1% | 0.0 |  |
| xf2c15 | VARCHAR | 80.0% | R |  |
| f2c15 | DOUBLE | 80.1% | 0.0 |  |
| xf2c151 | VARCHAR | 80.0% | R |  |
| f2c151 | DOUBLE | 80.1% | 0.0 |  |
| xf2c152 | VARCHAR | 80.0% | R |  |
| f2c152 | DOUBLE | 80.1% | 0.0 |  |
| xf2c16 | VARCHAR | 80.0% | R |  |
| f2c16 | DOUBLE | 80.1% | 0.0 |  |
| xf2c161 | VARCHAR | 80.0% | R |  |
| f2c161 | DOUBLE | 80.1% | 0.0 |  |
| xf2c162 | VARCHAR | 80.0% | R |  |
| f2c162 | DOUBLE | 80.1% | 0.0 |  |
| xf2c17 | VARCHAR | 80.0% | R |  |
| f2c17 | DOUBLE | 80.1% | 810026.0 |  |
| xf2c171 | VARCHAR | 80.0% | R |  |
| f2c171 | DOUBLE | 80.1% | 810026.0 |  |
| xf2c172 | VARCHAR | 80.0% | R |  |
| f2c172 | DOUBLE | 80.1% | 0.0 |  |
| xf2d01 | VARCHAR | 0.0% | R |  |
| f2d01 | DOUBLE | 0.0% | 7408702.0 |  |
| xf2d012 | VARCHAR | 29.7% | R |  |
| f2d012 | DOUBLE | 34.9% | 7408702.0 |  |
| xf2d013 | VARCHAR | 29.7% | R |  |
| f2d013 | DOUBLE | 34.9% | 0.0 |  |
| xf2d014 | VARCHAR | 29.7% | R |  |
| f2d014 | DOUBLE | 34.9% | 0.0 |  |
| xf2d02 | VARCHAR | 0.0% | R |  |
| f2d02 | BIGINT | 0.0% | 0 |  |
| xf2d022 | VARCHAR | 29.7% | R |  |
| f2d022 | DOUBLE | 34.9% | 0.0 |  |
| xf2d023 | VARCHAR | 29.7% | R |  |
| f2d023 | DOUBLE | 34.9% | 0.0 |  |
| xf2d024 | VARCHAR | 29.7% | R |  |
| f2d024 | DOUBLE | 34.9% | 0.0 |  |
| xf2d03 | VARCHAR | 0.0% | R |  |
| f2d03 | BIGINT | 0.0% | 0 |  |
| xf2d032 | VARCHAR | 29.7% | R |  |
| f2d032 | DOUBLE | 34.9% | 0.0 |  |
| xf2d033 | VARCHAR | 29.7% | R |  |
| f2d033 | DOUBLE | 34.9% | 0.0 |  |
| xf2d034 | VARCHAR | 29.7% | R |  |
| f2d034 | DOUBLE | 34.9% | 0.0 |  |
| xf2d04 | VARCHAR | 0.0% | R |  |
| f2d04 | BIGINT | 0.0% | 0 |  |
| xf2d042 | VARCHAR | 29.7% | R |  |
| f2d042 | DOUBLE | 34.9% | 0.0 |  |
| xf2d043 | VARCHAR | 29.7% | R |  |
| f2d043 | DOUBLE | 34.9% | 0.0 |  |
| xf2d044 | VARCHAR | 29.7% | R |  |
| f2d044 | DOUBLE | 34.9% | 0.0 |  |
| xf2d05 | VARCHAR | 0.0% | R |  |
| f2d05 | DOUBLE | 0.0% | 13959.0 |  |
| xf2d052 | VARCHAR | 29.7% | R |  |
| f2d052 | DOUBLE | 34.9% | 13959.0 |  |
| xf2d053 | VARCHAR | 29.7% | R |  |
| f2d053 | DOUBLE | 34.9% | 0.0 |  |
| xf2d054 | VARCHAR | 29.7% | R |  |
| f2d054 | DOUBLE | 34.9% | 0.0 |  |
| xf2d06 | VARCHAR | 0.0% | R |  |
| f2d06 | BIGINT | 0.0% | 0 |  |
| xf2d062 | VARCHAR | 29.7% | R |  |
| f2d062 | DOUBLE | 34.9% | 0.0 |  |
| xf2d063 | VARCHAR | 29.7% | R |  |
| f2d063 | DOUBLE | 34.9% | 0.0 |  |
| xf2d064 | VARCHAR | 29.7% | R |  |
| f2d064 | DOUBLE | 34.9% | 0.0 |  |
| xf2d07 | VARCHAR | 0.0% | R |  |
| f2d07 | BIGINT | 0.0% | 0 |  |
| xf2d072 | VARCHAR | 29.7% | R |  |
| f2d072 | DOUBLE | 34.9% | 0.0 |  |
| xf2d073 | VARCHAR | 29.7% | R |  |
| f2d073 | DOUBLE | 34.9% | 0.0 |  |
| xf2d074 | VARCHAR | 29.7% | R |  |
| f2d074 | DOUBLE | 34.9% | 0.0 |  |
| xf2d08 | VARCHAR | 0.0% | R |  |
| f2d08 | DOUBLE | 0.0% | 77845.0 |  |
| xf2d082 | VARCHAR | 29.7% | R |  |
| f2d082 | DOUBLE | 34.9% | 77845.0 |  |
| xf2d083 | VARCHAR | 29.7% | R |  |
| f2d083 | DOUBLE | 34.9% | 0.0 |  |
| xf2d084 | VARCHAR | 29.7% | R |  |
| f2d084 | DOUBLE | 34.9% | 0.0 |  |
| xf2d08a | VARCHAR | 29.7% | R |  |
| f2d08a | DOUBLE | 34.9% | 77845.0 |  |
| xf2d082a | VARCHAR | 29.7% | R |  |
| f2d082a | DOUBLE | 34.9% | 77845.0 |  |
| xf2d083a | VARCHAR | 29.7% | R |  |
| f2d083a | DOUBLE | 34.9% | 0.0 |  |
| xf2d084a | VARCHAR | 29.7% | R |  |
| f2d084a | DOUBLE | 34.9% | 0.0 |  |
| xf2d08b | VARCHAR | 29.7% | R |  |
| f2d08b | DOUBLE | 34.9% | 0.0 |  |
| xf2d082b | VARCHAR | 29.7% | R |  |
| f2d082b | DOUBLE | 34.9% | 0.0 |  |
| xf2d083b | VARCHAR | 29.7% | R |  |
| f2d083b | DOUBLE | 34.9% | 0.0 |  |
| xf2d084b | VARCHAR | 29.7% | R |  |
| f2d084b | DOUBLE | 34.9% | 0.0 |  |
| xf2d09 | VARCHAR | 0.0% | R |  |
| f2d09 | BIGINT | 0.0% | 0 |  |
| xf2d092 | VARCHAR | 29.7% | R |  |
| f2d092 | DOUBLE | 34.9% | 0.0 |  |
| xf2d093 | VARCHAR | 29.7% | R |  |
| f2d093 | DOUBLE | 34.9% | 0.0 |  |
| xf2d094 | VARCHAR | 29.7% | R |  |
| f2d094 | DOUBLE | 34.9% | 0.0 |  |
| xf2d10 | VARCHAR | 0.0% | R |  |
| f2d10 | DOUBLE | 0.0% | 140875.0 |  |
| xf2d102 | VARCHAR | 29.7% | R |  |
| f2d102 | DOUBLE | 34.9% | 143066.0 |  |
| xf2d103 | VARCHAR | 29.7% | R |  |
| f2d103 | DOUBLE | 34.9% | -2191.0 |  |
| xf2d104 | VARCHAR | 29.7% | R |  |
| f2d104 | DOUBLE | 34.9% | 0.0 |  |
| xf2d11 | VARCHAR | 0.0% | Z |  |
| f2d11 | DOUBLE | 0.0% | 0.0 |  |
| xf2d112 | VARCHAR | 29.7% | Z |  |
| f2d112 | DOUBLE | 34.9% | 0.0 |  |
| xf2d12 | VARCHAR | 0.0% | R |  |
| f2d12 | DOUBLE | 5.4% | 0.0 |  |
| xf2d122 | VARCHAR | 29.7% | R |  |
| f2d122 | DOUBLE | 40.3% | 0.0 |  |
| xf2d13 | VARCHAR | 0.0% | R |  |
| f2d13 | DOUBLE | 11.7% | 0.0 |  |
| xf2d132 | VARCHAR | 29.7% | R |  |
| f2d132 | DOUBLE | 43.7% | 0.0 |  |
| xf2d14 | VARCHAR | 0.0% | R |  |
| f2d14 | DOUBLE | 11.7% | 0.0 |  |
| xf2d142 | VARCHAR | 29.7% | R |  |
| f2d142 | DOUBLE | 43.7% | 0.0 |  |
| xf2d143 | VARCHAR | 29.7% | R |  |
| f2d143 | DOUBLE | 43.7% | 0.0 |  |
| xf2d144 | VARCHAR | 29.7% | R |  |
| f2d144 | DOUBLE | 43.7% | 0.0 |  |
| xf2d15 | VARCHAR | 0.0% | R |  |
| f2d15 | DOUBLE | 0.0% | 198621.0 |  |
| xf2d152 | VARCHAR | 29.7% | R |  |
| f2d152 | DOUBLE | 34.9% | 198621.0 |  |
| xf2d153 | VARCHAR | 29.7% | R |  |
| f2d153 | DOUBLE | 34.9% | 0.0 |  |
| xf2d154 | VARCHAR | 29.7% | R |  |
| f2d154 | DOUBLE | 34.9% | 0.0 |  |
| xf2d16 | VARCHAR | 0.0% | R |  |
| f2d16 | DOUBLE | 0.0% | 7840002.0 |  |
| xf2d162 | VARCHAR | 29.7% | R |  |
| f2d162 | DOUBLE | 34.9% | 7842193.0 |  |
| xf2d163 | VARCHAR | 29.7% | R |  |
| f2d163 | DOUBLE | 34.9% | -2191.0 |  |
| xf2d164 | VARCHAR | 29.7% | R |  |
| f2d164 | DOUBLE | 34.9% | 0.0 |  |
| xf2d17 | VARCHAR | 46.4% | R |  |
| f2d17 | BIGINT | 46.4% | 0 |  |
| xf2d172 | VARCHAR | 29.7% | R |  |
| f2d172 | DOUBLE | 34.9% | 0.0 |  |
| xf2d173 | VARCHAR | 29.7% | R |  |
| f2d173 | DOUBLE | 34.9% | 0.0 |  |
| xf2d174 | VARCHAR | 33.8% | R |  |
| f2d174 | DOUBLE | 36.0% | 0.0 |  |
| xf2d18 | VARCHAR | 33.8% | R |  |
| f2d18 | DOUBLE | 36.0% | 7840002.0 |  |
| xf2d182 | VARCHAR | 29.7% | R |  |
| f2d182 | DOUBLE | 34.9% | 7842193.0 |  |
| xf2d183 | VARCHAR | 29.7% | R |  |
| f2d183 | DOUBLE | 34.9% | -2191.0 |  |
| xf2d184 | VARCHAR | 29.7% | R |  |
| f2d184 | DOUBLE | 34.9% | 0.0 |  |
| xf2e011 | VARCHAR | 0.0% | R |  |
| f2e011 | DOUBLE | 0.0% | 2601674.0 |  |
| xf2e012 | VARCHAR | 0.0% | R |  |
| f2e012 | DOUBLE | 0.0% | 1922659.0 |  |
| xf2e021 | VARCHAR | 0.0% | R |  |
| f2e021 | DOUBLE | 0.0% | 0.0 |  |
| xf2e022 | VARCHAR | 0.0% | R |  |
| f2e022 | DOUBLE | 0.0% | 0.0 |  |
| xf2e031 | VARCHAR | 0.0% | R |  |
| f2e031 | DOUBLE | 0.0% | 0.0 |  |
| xf2e032 | VARCHAR | 0.0% | R |  |
| f2e032 | DOUBLE | 0.0% | 0.0 |  |
| xf2e041 | VARCHAR | 0.0% | R |  |
| f2e041 | DOUBLE | 0.0% | 714381.0 |  |
| xf2e042 | VARCHAR | 0.0% | R |  |
| f2e042 | DOUBLE | 0.0% | 494843.0 |  |
| xf2e051 | VARCHAR | 0.0% | R |  |
| f2e051 | DOUBLE | 0.0% | 1139153.0 |  |
| xf2e052 | VARCHAR | 0.0% | R |  |
| f2e052 | DOUBLE | 0.0% | 868305.0 |  |
| xf2e061 | VARCHAR | 0.0% | R |  |
| f2e061 | DOUBLE | 0.0% | 2998112.0 |  |
| xf2e062 | VARCHAR | 0.0% | R |  |
| f2e062 | DOUBLE | 0.0% | 1063879.0 |  |
| xf2e071 | VARCHAR | 0.0% | R |  |
| f2e071 | DOUBLE | 5.4% | 0.0 |  |
| xf2e072 | VARCHAR | 0.0% | R |  |
| f2e072 | DOUBLE | 5.4% | 0.0 |  |
| xf2e081 | VARCHAR | 0.0% | R |  |
| f2e081 | DOUBLE | 0.0% | 0.0 |  |
| xf2e091 | VARCHAR | 0.0% | R |  |
| f2e091 | DOUBLE | 11.7% | 0.0 |  |
| xf2e092 | VARCHAR | 0.0% | R |  |
| f2e092 | DOUBLE | 11.7% | 0.0 |  |
| xf2e101 | VARCHAR | 0.0% | R |  |
| f2e101 | DOUBLE | 11.7% | 0.0 |  |
| xf2e102 | VARCHAR | 0.0% | R |  |
| f2e102 | DOUBLE | 11.7% | 0.0 |  |
| xf2e121 | VARCHAR | 0.0% | R |  |
| f2e121 | DOUBLE | 0.0% | 0.0 |  |
| xf2e122 | VARCHAR | 0.0% | R |  |
| f2e122 | DOUBLE | 0.0% | 0.0 |  |
| xf2e131 | VARCHAR | 4.2% | R |  |
| f2e131 | DOUBLE | 4.2% | 7453320.0 |  |
| xf2e132 | VARCHAR | 4.2% | R |  |
| f2e132 | DOUBLE | 4.2% | 4349686.0 |  |
| xf2e133 | VARCHAR | 4.2% | R |  |
| f2e133 | DOUBLE | 4.2% | 582179.0 |  |
| xf2e134 | VARCHAR | 4.2% | R |  |
| f2e134 | DOUBLE | 12.7% | 147985.0 |  |
| xf2e135 | VARCHAR | 4.2% | R |  |
| f2e135 | DOUBLE | 4.2% | 99768.0 |  |
| xf2e136 | VARCHAR | 4.2% | R |  |
| f2e136 | DOUBLE | 4.2% | 0.0 |  |
| xf2e137 | VARCHAR | 4.2% | R |  |
| f2e137 | DOUBLE | 4.2% | 2273702.0 |  |
| f2fha | DOUBLE | 8.5% | 1.0 |  |
| xf2h01 | VARCHAR | 8.5% | R |  |
| f2h01 | DOUBLE | 31.8% | 174864.0 |  |
| xf2h02 | VARCHAR | 8.5% | R |  |
| f2h02 | DOUBLE | 31.8% | 174819.0 |  |
| xf2h03 | VARCHAR | 80.0% | R |  |
| f2h03 | DOUBLE | 85.1% | -45.0 |  |
| xf2h03a | VARCHAR | 80.0% | R |  |
| f2h03a | DOUBLE | 85.1% | 0.0 |  |
| xf2h03b | VARCHAR | 80.0% | R |  |
| f2h03b | DOUBLE | 85.1% | 0.0 |  |
| xf2h03c | VARCHAR | 80.0% | R |  |
| f2h03c | DOUBLE | 85.1% | 0.0 |  |
| xf2h03d | VARCHAR | 80.0% | R |  |
| f2h03d | DOUBLE | 85.1% | -45.0 |  |
| xf2i01 | VARCHAR | 80.0% | R |  |
| f2i01 | DOUBLE | 82.1% | 388873.0 |  |
| xf2i02 | VARCHAR | 80.0% | R |  |
| f2i02 | DOUBLE | 82.1% | 7408702.0 |  |
| xf2i03 | VARCHAR | 80.0% | R |  |
| f2i03 | DOUBLE | 82.1% | 386682.0 |  |
| xf2i04 | VARCHAR | 80.0% | R |  |
| f2i04 | DOUBLE | 82.1% | 15506978.0 |  |
| xf2i05 | VARCHAR | 80.0% | R |  |
| f2i05 | DOUBLE | 82.1% | 15893660.0 |  |
| xf2i06 | VARCHAR | 80.0% | R |  |
| f2i06 | DOUBLE | 82.1% | 0.0 |  |
| xf2i07 | VARCHAR | 80.0% | R |  |
| f2i07 | DOUBLE | 82.1% | 7453320.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xf2e013 | VARCHAR | 40.9% | R |  |
| f2e013 | DOUBLE | 40.9% | 290086.0 |  |
| xf2e014 | VARCHAR | 40.9% | R |  |
| f2e014 | DOUBLE | 40.9% | 136772.0 |  |
| xf2e015 | VARCHAR | 40.9% | R |  |
| f2e015 | DOUBLE | 40.9% | 0.0 |  |
| xf2e016 | VARCHAR | 40.9% | R |  |
| f2e016 | DOUBLE | 40.9% | 0.0 |  |
| xf2e017 | VARCHAR | 40.9% | R |  |
| f2e017 | DOUBLE | 40.9% | 657663.0 |  |
| xf2e023 | VARCHAR | 40.9% | R |  |
| f2e023 | DOUBLE | 40.9% | 0.0 |  |
| xf2e024 | VARCHAR | 40.9% | R |  |
| f2e024 | DOUBLE | 40.9% | 0.0 |  |
| xf2e025 | VARCHAR | 40.9% | R |  |
| f2e025 | DOUBLE | 40.9% | 0.0 |  |
| xf2e026 | VARCHAR | 40.9% | R |  |
| f2e026 | DOUBLE | 40.9% | 0.0 |  |
| xf2e027 | VARCHAR | 40.9% | R |  |
| f2e027 | DOUBLE | 40.9% | 0.0 |  |
| xf2e033 | VARCHAR | 40.9% | R |  |
| f2e033 | DOUBLE | 40.9% | 0.0 |  |
| xf2e034 | VARCHAR | 40.9% | R |  |
| f2e034 | DOUBLE | 40.9% | 0.0 |  |
| xf2e035 | VARCHAR | 40.9% | R |  |
| f2e035 | DOUBLE | 40.9% | 0.0 |  |
| xf2e036 | VARCHAR | 40.9% | R |  |
| f2e036 | DOUBLE | 40.9% | 0.0 |  |
| xf2e037 | VARCHAR | 40.9% | R |  |
| f2e037 | DOUBLE | 40.9% | 0.0 |  |
| xf2e043 | VARCHAR | 40.9% | R |  |
| f2e043 | DOUBLE | 40.9% | 7110.0 |  |
| xf2e044 | VARCHAR | 40.9% | R |  |
| f2e044 | DOUBLE | 40.9% | 13026.0 |  |
| xf2e045 | VARCHAR | 40.9% | R |  |
| f2e045 | DOUBLE | 40.9% | 0.0 |  |
| xf2e046 | VARCHAR | 40.9% | R |  |
| f2e046 | DOUBLE | 40.9% | 0.0 |  |
| xf2e047 | VARCHAR | 40.9% | R |  |
| f2e047 | DOUBLE | 40.9% | 37276.0 |  |
| xf2e053 | VARCHAR | 40.9% | R |  |
| f2e053 | DOUBLE | 40.9% | 80342.0 |  |
| xf2e054 | VARCHAR | 40.9% | R |  |
| f2e054 | DOUBLE | 40.9% | 35821.0 |  |
| xf2e055 | VARCHAR | 40.9% | R |  |
| f2e055 | DOUBLE | 40.9% | 0.0 |  |
| xf2e056 | VARCHAR | 40.9% | R |  |
| f2e056 | DOUBLE | 40.9% | 0.0 |  |
| xf2e057 | VARCHAR | 40.9% | R |  |
| f2e057 | DOUBLE | 40.9% | 74073.0 |  |
| xf2e063 | VARCHAR | 40.9% | R |  |
| f2e063 | DOUBLE | 40.9% | 510128.0 |  |
| xf2e064 | VARCHAR | 40.9% | R |  |
| f2e064 | DOUBLE | 40.9% | 140028.0 |  |
| xf2e065 | VARCHAR | 40.9% | R |  |
| f2e065 | DOUBLE | 40.9% | 139849.0 |  |
| xf2e066 | VARCHAR | 40.9% | R |  |
| f2e066 | DOUBLE | 40.9% | 118216.0 |  |
| xf2e067 | VARCHAR | 40.9% | R |  |
| f2e067 | DOUBLE | 40.9% | 2328503.0 |  |
| xf2e073 | VARCHAR | 40.9% | R |  |
| f2e073 | DOUBLE | 43.8% | 0.0 |  |
| xf2e074 | VARCHAR | 40.9% | R |  |
| f2e074 | DOUBLE | 43.8% | 0.0 |  |
| xf2e075 | VARCHAR | 40.9% | R |  |
| f2e075 | DOUBLE | 43.8% | 0.0 |  |
| xf2e076 | VARCHAR | 40.9% | R |  |
| f2e076 | DOUBLE | 43.8% | 0.0 |  |
| xf2e077 | VARCHAR | 40.9% | R |  |
| f2e077 | DOUBLE | 43.8% | 0.0 |  |
| xf2e087 | VARCHAR | 40.9% | R |  |
| f2e087 | DOUBLE | 40.9% | 0.0 |  |
| xf2e093 | VARCHAR | 40.9% | R |  |
| f2e093 | DOUBLE | 48.2% | 0.0 |  |
| xf2e094 | VARCHAR | 40.9% | R |  |
| f2e094 | DOUBLE | 48.2% | 0.0 |  |
| xf2e095 | VARCHAR | 40.9% | R |  |
| f2e095 | DOUBLE | 48.2% | 0.0 |  |
| xf2e096 | VARCHAR | 40.9% | R |  |
| f2e096 | DOUBLE | 48.2% | 0.0 |  |
| xf2e097 | VARCHAR | 40.9% | R |  |
| f2e097 | DOUBLE | 48.2% | 0.0 |  |
| xf2e103 | VARCHAR | 40.9% | R |  |
| f2e103 | DOUBLE | 48.2% | 0.0 |  |
| xf2e104 | VARCHAR | 40.9% | R |  |
| f2e104 | DOUBLE | 48.2% | 0.0 |  |
| xf2e105 | VARCHAR | 40.9% | R |  |
| f2e105 | DOUBLE | 48.2% | 0.0 |  |
| xf2e106 | VARCHAR | 40.9% | R |  |
| f2e106 | DOUBLE | 48.2% | 0.0 |  |
| xf2e107 | VARCHAR | 40.9% | R |  |
| f2e107 | DOUBLE | 48.2% | 0.0 |  |
| xf2e111 | VARCHAR | 36.6% | R |  |
| f2e111 | DOUBLE | 45.1% | 0.0 |  |
| xf2e112 | VARCHAR | 36.6% | R |  |
| f2e112 | DOUBLE | 36.6% | 0.0 |  |
| xf2e113 | VARCHAR | 40.9% | R |  |
| f2e113 | DOUBLE | 40.9% | 0.0 |  |
| xf2e114 | VARCHAR | 40.9% | R |  |
| f2e114 | DOUBLE | 40.9% | -325647.0 |  |
| xf2e115 | VARCHAR | 40.9% | R |  |
| f2e115 | DOUBLE | 40.9% | 0.0 |  |
| xf2e116 | VARCHAR | 40.9% | R |  |
| f2e116 | DOUBLE | 40.9% | 0.0 |  |
| xf2e117 | VARCHAR | 40.9% | R |  |
| f2e117 | DOUBLE | 40.9% | 325647.0 |  |
| xf2e123 | VARCHAR | 40.9% | R |  |
| f2e123 | DOUBLE | 40.9% | 0.0 |  |
| xf2e124 | VARCHAR | 40.9% | R |  |
| f2e124 | DOUBLE | 40.9% | 0.0 |  |
| xf2e125 | VARCHAR | 40.9% | R |  |
| f2e125 | DOUBLE | 40.9% | 0.0 |  |
| xf2e126 | VARCHAR | 40.9% | R |  |
| f2e126 | DOUBLE | 40.9% | 0.0 |  |
| xf2e127 | VARCHAR | 40.9% | R |  |
| f2e127 | DOUBLE | 40.9% | 0.0 |  |
| i | DOUBLE | 100.0% |  |  |
| xf2a14 | VARCHAR | 62.0% | Z |  |
| f2a14 | DOUBLE | 67.2% | 0.0 |  |
| xf2e082 | VARCHAR | 62.0% | A |  |
| f2e082 | DOUBLE | 87.2% | 0.0 |  |
| xf2e083 | VARCHAR | 66.2% | A |  |
| f2e083 | DOUBLE | 91.5% | 0.0 |  |
| xf2e084 | VARCHAR | 66.2% | A |  |
| f2e084 | DOUBLE | 91.5% | 0.0 |  |
| xf2e085 | VARCHAR | 66.2% | A |  |
| f2e085 | DOUBLE | 91.5% | 0.0 |  |
| xf2e086 | VARCHAR | 66.2% | A |  |
| f2e086 | DOUBLE | 91.5% | 0.0 |  |
| xf2e141 | VARCHAR | 95.8% | R |  |
| f2e141 | BIGINT | 95.8% | 269211 |  |
| xf2e151 | VARCHAR | 95.8% | R |  |
| f2e151 | BIGINT | 95.8% | 131249 |  |
| xf2e161 | VARCHAR | 95.8% | R |  |
| f2e161 | BIGINT | 95.8% | 79703 |  |
| xf2e171 | VARCHAR | 95.8% | R |  |
| f2e171 | BIGINT | 95.8% | 1010784 |  |

## f3

Rows: 61,533

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 101116 | Primary institution ID, joins across all IPEDS tables |
| xf3a01 | VARCHAR | 0.0% | R |  |
| f3a01 | DOUBLE | 51.8% | 6772738.0 |  |
| xf3a01a | VARCHAR | 56.2% | R |  |
| f3a01a | DOUBLE | 88.3% | 0.0 |  |
| xf3a01b | VARCHAR | 56.2% | R |  |
| f3a01b | DOUBLE | 88.3% | 542391.0 |  |
| xf3a01c | VARCHAR | 56.2% | R |  |
| f3a01c | DOUBLE | 88.3% | 0.0 |  |
| xf3a02 | VARCHAR | 0.0% | R |  |
| f3a02 | DOUBLE | 51.8% | 4303616.0 |  |
| xf3a02a | VARCHAR | 56.2% | R |  |
| f3a02a | DOUBLE | 88.3% | 0.0 |  |
| xf3a03 | VARCHAR | 0.0% | R |  |
| f3a03 | DOUBLE | 51.8% | 2469122.0 |  |
| xf3a04 | VARCHAR | 0.0% | R |  |
| f3a04 | DOUBLE | 51.8% | 6772738.0 |  |
| xf3a05 | VARCHAR | 56.2% | R |  |
| f3a05 | DOUBLE | 88.3% | 0.0 |  |
| xf3a06 | VARCHAR | 56.2% | R |  |
| f3a06 | DOUBLE | 88.3% | 1293557.0 |  |
| xf3a07 | VARCHAR | 56.2% | R |  |
| f3a07 | DOUBLE | 88.3% | 471595.0 |  |
| xf3a08 | VARCHAR | 56.2% | R |  |
| f3a08 | DOUBLE | 88.3% | 0.0 |  |
| xf3a09 | VARCHAR | 56.2% | R |  |
| f3a09 | DOUBLE | 88.3% | 134740.0 |  |
| xf3a10 | VARCHAR | 56.2% | R |  |
| f3a10 | DOUBLE | 88.3% | 1899892.0 |  |
| xf3a11 | VARCHAR | 56.2% | R |  |
| f3a11 | DOUBLE | 88.3% | 1357501.0 |  |
| xf3a12 | VARCHAR | 56.2% | R |  |
| f3a12 | DOUBLE | 88.3% | 542391.0 |  |
| xf3b01 | VARCHAR | 0.0% | R |  |
| f3b01 | DOUBLE | 43.3% | 6448031.0 |  |
| xf3b02 | VARCHAR | 0.0% | R |  |
| f3b02 | DOUBLE | 43.3% | 6477912.0 |  |
| xf3b03 | VARCHAR | 0.0% | R |  |
| f3b03 | DOUBLE | 51.5% | 0.0 |  |
| xf3b04 | VARCHAR | 0.0% | R |  |
| f3b04 | DOUBLE | 51.5% | -29881.0 |  |
| xf3b05 | VARCHAR | 0.0% | R |  |
| f3b05 | DOUBLE | 52.2% | 425599.0 |  |
| xf3b06 | VARCHAR | 0.0% | R |  |
| f3b06 | DOUBLE | 51.6% | 2073404.0 |  |
| xf3b07 | VARCHAR | 0.0% | R |  |
| f3b07 | DOUBLE | 51.5% | 0.0 |  |
| xf3b08 | VARCHAR | 0.0% | R |  |
| f3b08 | DOUBLE | 51.5% | 2469122.0 |  |
| xf3c01 | VARCHAR | 0.0% | R |  |
| f3c01 | DOUBLE | 0.2% | 1551934.0 |  |
| xf3c02 | VARCHAR | 0.0% | R |  |
| f3c02 | DOUBLE | 0.2% | 78140.0 |  |
| xf3c03 | VARCHAR | 0.0% | R |  |
| f3c03 | DOUBLE | 0.2% | 103506.0 |  |
| xf3c03a | VARCHAR | 56.2% | R |  |
| f3c03a | DOUBLE | 56.3% | 103506.0 |  |
| xf3c03b | VARCHAR | 56.2% | R |  |
| f3c03b | DOUBLE | 56.3% | 0.0 |  |
| xf3c04 | VARCHAR | 0.0% | R |  |
| f3c04 | DOUBLE | 0.2% | 969392.0 |  |
| xf3c05 | VARCHAR | 0.0% | R |  |
| f3c05 | DOUBLE | 0.2% | 2702972.0 |  |
| xf3c06 | VARCHAR | 0.0% | R |  |
| f3c06 | DOUBLE | 0.2% | 0.0 |  |
| xf3c07 | VARCHAR | 0.0% | R |  |
| f3c07 | DOUBLE | 0.2% | 0.0 |  |
| xf3c08 | VARCHAR | 66.3% | R |  |
| f3c08 | DOUBLE | 66.3% | 0.0 |  |
| xf3c12 | VARCHAR | 82.7% | R |  |
| f3c12 | DOUBLE | 82.7% | 0.0 |  |
| xf3c121 | VARCHAR | 82.7% | R |  |
| f3c121 | DOUBLE | 82.7% | 0.0 |  |
| xf3c122 | VARCHAR | 82.7% | R |  |
| f3c122 | DOUBLE | 82.7% | 0.0 |  |
| xf3c13 | VARCHAR | 82.7% | R |  |
| f3c13 | DOUBLE | 82.7% | 0.0 |  |
| xf3c131 | VARCHAR | 82.7% | R |  |
| f3c131 | DOUBLE | 82.7% | 0.0 |  |
| xf3c132 | VARCHAR | 82.7% | R |  |
| f3c132 | DOUBLE | 82.7% | 0.0 |  |
| xf3c14 | VARCHAR | 82.7% | R |  |
| f3c14 | DOUBLE | 82.7% | 0.0 |  |
| xf3c141 | VARCHAR | 82.7% | R |  |
| f3c141 | DOUBLE | 82.7% | 0.0 |  |
| xf3c142 | VARCHAR | 82.7% | R |  |
| f3c142 | DOUBLE | 82.7% | 0.0 |  |
| xf3c15 | VARCHAR | 82.7% | R |  |
| f3c15 | DOUBLE | 82.7% | 0.0 |  |
| xf3c151 | VARCHAR | 82.7% | R |  |
| f3c151 | DOUBLE | 82.7% | 0.0 |  |
| xf3c152 | VARCHAR | 82.7% | R |  |
| f3c152 | DOUBLE | 82.7% | 0.0 |  |
| xf3c16 | VARCHAR | 82.7% | R |  |
| f3c16 | DOUBLE | 82.7% | 0.0 |  |
| xf3c161 | VARCHAR | 82.7% | R |  |
| f3c161 | DOUBLE | 82.7% | 0.0 |  |
| xf3c162 | VARCHAR | 82.7% | R |  |
| f3c162 | DOUBLE | 82.7% | 0.0 |  |
| xf3c17 | VARCHAR | 82.7% | R |  |
| f3c17 | DOUBLE | 82.7% | 0.0 |  |
| xf3c171 | VARCHAR | 82.7% | R |  |
| f3c171 | DOUBLE | 82.7% | 0.0 |  |
| xf3c172 | VARCHAR | 82.7% | R |  |
| f3c172 | DOUBLE | 82.7% | 0.0 |  |
| xf3d01 | VARCHAR | 0.0% | R |  |
| f3d01 | DOUBLE | 0.1% | 4569436.0 |  |
| xf3d02 | VARCHAR | 0.0% | R |  |
| f3d02 | DOUBLE | 0.1% | 1630074.0 |  |
| xf3d02a | VARCHAR | 56.2% | R |  |
| f3d02a | BIGINT | 56.2% | 0 |  |
| xf3d02b | VARCHAR | 56.2% | R |  |
| f3d02b | BIGINT | 56.2% | 1630074 |  |
| xf3d03 | VARCHAR | 0.0% | R |  |
| f3d03 | DOUBLE | 0.1% | 103506.0 |  |
| xf3d03a | VARCHAR | 56.2% | R |  |
| f3d03a | BIGINT | 56.2% | 0 |  |
| xf3d03b | VARCHAR | 56.2% | R |  |
| f3d03b | BIGINT | 56.2% | 103506 |  |
| xf3d03c | VARCHAR | 56.2% | R |  |
| f3d03c | BIGINT | 56.2% | 0 |  |
| xf3d03d | VARCHAR | 56.2% | R |  |
| f3d03d | BIGINT | 56.2% | 0 |  |
| xf3d04 | VARCHAR | 0.0% | R |  |
| f3d04 | DOUBLE | 0.1% | 0.0 |  |
| xf3d05 | VARCHAR | 0.0% | R |  |
| f3d05 | DOUBLE | 0.1% | 0.0 |  |
| xf3d06 | VARCHAR | 0.0% | R |  |
| f3d06 | DOUBLE | 0.1% | 0.0 |  |
| xf3d07 | VARCHAR | 0.0% | R |  |
| f3d07 | DOUBLE | 43.9% | 134369.0 |  |
| xf3d12 | VARCHAR | 56.2% | R |  |
| f3d12 | DOUBLE | 92.7% | 0.0 |  |
| xf3d08 | VARCHAR | 0.0% | R |  |
| f3d08 | DOUBLE | 0.1% | 10646.0 |  |
| xf3d09 | VARCHAR | 0.0% | R |  |
| f3d09 | DOUBLE | 0.1% | 6448031.0 |  |
| xf3e011 | VARCHAR | 56.2% | R |  |
| f3e011 | BIGINT | 56.2% | 2335507 |  |
| xf3e012 | VARCHAR | 56.2% | R |  |
| f3e012 | BIGINT | 56.2% | 1496769 |  |
| xf3e02a1 | VARCHAR | 56.2% | Z |  |
| f3e02a1 | BIGINT | 56.2% | 0 |  |
| xf3e02a2 | VARCHAR | 56.2% | Z |  |
| f3e02a2 | BIGINT | 56.2% | 0 |  |
| xf3e02b1 | VARCHAR | 56.2% | Z |  |
| f3e02b1 | BIGINT | 56.2% | 0 |  |
| xf3e02b2 | VARCHAR | 56.2% | Z |  |
| f3e02b2 | BIGINT | 56.2% | 0 |  |
| xf3e03a1 | VARCHAR | 56.2% | R |  |
| f3e03a1 | BIGINT | 56.2% | 124416 |  |
| xf3e03a2 | VARCHAR | 56.2% | R |  |
| f3e03a2 | BIGINT | 56.2% | 73984 |  |
| xf3e03b1 | VARCHAR | 56.2% | R |  |
| f3e03b1 | BIGINT | 56.2% | 869774 |  |
| xf3e03b2 | VARCHAR | 56.2% | R |  |
| f3e03b2 | BIGINT | 56.2% | 735322 |  |
| xf3e03c1 | VARCHAR | 56.2% | R |  |
| f3e03c1 | BIGINT | 56.2% | 2964729 |  |
| xf3e03c2 | VARCHAR | 56.2% | R |  |
| f3e03c2 | BIGINT | 56.2% | 136884 |  |
| xf3e041 | VARCHAR | 56.2% | R |  |
| f3e041 | DOUBLE | 85.2% | 0.0 |  |
| xf3e042 | VARCHAR | 56.2% | R |  |
| f3e042 | DOUBLE | 85.2% | 0.0 |  |
| xf3e051 | VARCHAR | 56.2% | Z |  |
| f3e051 | BIGINT | 56.2% | 0 |  |
| xf3e101 | VARCHAR | 56.2% | Z |  |
| f3e101 | DOUBLE | 92.7% | 0.0 |  |
| xf3e102 | VARCHAR | 56.2% | Z |  |
| f3e102 | DOUBLE | 92.7% | 0.0 |  |
| xf3e061 | VARCHAR | 56.2% | R |  |
| f3e061 | BIGINT | 56.2% | 183486 |  |
| xf3e062 | VARCHAR | 56.2% | R |  |
| f3e062 | BIGINT | 56.2% | 0 |  |
| xf3e071 | VARCHAR | 56.2% | R |  |
| f3e071 | BIGINT | 56.2% | 6477912 |  |
| xf3e072 | VARCHAR | 56.2% | R |  |
| f3e072 | BIGINT | 56.2% | 2442959 |  |
| xf3e073 | VARCHAR | 56.2% | R |  |
| f3e073 | BIGINT | 56.2% | 186792 |  |
| xf3e074 | VARCHAR | 66.3% | R |  |
| f3e074 | BIGINT | 66.3% | 1486764 |  |
| xf3e075 | VARCHAR | 56.2% | R |  |
| f3e075 | BIGINT | 56.2% | 183487 |  |
| xf3e076 | VARCHAR | 56.2% | R |  |
| f3e076 | BIGINT | 56.2% | 0 |  |
| xf3e077 | VARCHAR | 56.2% | R |  |
| f3e077 | BIGINT | 56.2% | 2177910 |  |
| xf3f01 | VARCHAR | 56.2% | R |  |
| f3f01 | DOUBLE | 92.9% | 0.0 |  |
| xf3f02 | VARCHAR | 56.2% | R |  |
| f3f02 | DOUBLE | 92.9% | 0.0 |  |
| f3f03 | BIGINT | 56.2% | 1 |  |
| xf3g01 | VARCHAR | 82.7% | R |  |
| f3g01 | DOUBLE | 95.8% | -29881.0 |  |
| xf3g02 | VARCHAR | 82.7% | R |  |
| f3g02 | DOUBLE | 95.8% | 6448031.0 |  |
| xf3g03 | VARCHAR | 82.7% | R |  |
| f3g03 | DOUBLE | 95.8% | 2469122.0 |  |
| xf3g04 | VARCHAR | 82.7% | R |  |
| f3g04 | DOUBLE | 95.8% | 6772738.0 |  |
| xf3g05 | VARCHAR | 82.7% | R |  |
| f3g05 | DOUBLE | 95.8% | 1926731.0 |  |
| xf3g06 | VARCHAR | 82.7% | R |  |
| f3g06 | DOUBLE | 95.8% | 0.0 |  |
| xf3g07 | VARCHAR | 82.7% | R |  |
| f3g07 | DOUBLE | 95.8% | 6477912.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xf3e013 | VARCHAR | 89.9% | R |  |
| f3e013 | BIGINT | 89.9% | 276572 |  |
| xf3e014 | VARCHAR | 89.9% | R |  |
| f3e014 | BIGINT | 89.9% | 466612 |  |
| xf3e015 | VARCHAR | 89.9% | R |  |
| f3e015 | BIGINT | 89.9% | 147895 |  |
| xf3e016 | VARCHAR | 89.9% | Z |  |
| f3e016 | BIGINT | 89.9% | 0 |  |
| xf3e017 | VARCHAR | 89.9% | R |  |
| f3e017 | BIGINT | 89.9% | 512928 |  |
| xf3e02a3 | VARCHAR | 89.9% | Z |  |
| f3e02a3 | BIGINT | 89.9% | 0 |  |
| xf3e02a4 | VARCHAR | 89.9% | Z |  |
| f3e02a4 | BIGINT | 89.9% | 0 |  |
| xf3e02a5 | VARCHAR | 89.9% | Z |  |
| f3e02a5 | BIGINT | 89.9% | 0 |  |
| xf3e02a6 | VARCHAR | 89.9% | Z |  |
| f3e02a6 | BIGINT | 89.9% | 0 |  |
| xf3e02a7 | VARCHAR | 89.9% | Z |  |
| f3e02a7 | BIGINT | 89.9% | 0 |  |
| xf3e02b3 | VARCHAR | 89.9% | Z |  |
| f3e02b3 | BIGINT | 89.9% | 0 |  |
| xf3e02b4 | VARCHAR | 89.9% | Z |  |
| f3e02b4 | BIGINT | 89.9% | 0 |  |
| xf3e02b5 | VARCHAR | 89.9% | Z |  |
| f3e02b5 | BIGINT | 89.9% | 0 |  |
| xf3e02b6 | VARCHAR | 89.9% | Z |  |
| f3e02b6 | BIGINT | 89.9% | 0 |  |
| xf3e02b7 | VARCHAR | 89.9% | Z |  |
| f3e02b7 | BIGINT | 89.9% | 0 |  |
| xf3e03a3 | VARCHAR | 89.9% | R |  |
| f3e03a3 | BIGINT | 89.9% | 70465 |  |
| xf3e03a4 | VARCHAR | 89.9% | R |  |
| f3e03a4 | BIGINT | 89.9% | 82976 |  |
| xf3e03a5 | VARCHAR | 89.9% | R |  |
| f3e03a5 | BIGINT | 89.9% | 26300 |  |
| xf3e03a6 | VARCHAR | 89.9% | Z |  |
| f3e03a6 | BIGINT | 89.9% | 0 |  |
| xf3e03a7 | VARCHAR | 89.9% | R |  |
| f3e03a7 | BIGINT | 89.9% | 55583 |  |
| xf3e03b3 | VARCHAR | 89.9% | R |  |
| f3e03b3 | BIGINT | 89.9% | 185588 |  |
| xf3e03b4 | VARCHAR | 89.9% | R |  |
| f3e03b4 | BIGINT | 89.9% | 220489 |  |
| xf3e03b5 | VARCHAR | 89.9% | R |  |
| f3e03b5 | BIGINT | 89.9% | 69885 |  |
| xf3e03b6 | VARCHAR | 89.9% | Z |  |
| f3e03b6 | BIGINT | 89.9% | 0 |  |
| xf3e03b7 | VARCHAR | 89.9% | R |  |
| f3e03b7 | BIGINT | 89.9% | 1047902 |  |
| xf3e03c3 | VARCHAR | 89.9% | R |  |
| f3e03c3 | BIGINT | 89.9% | 216729 |  |
| xf3e03c4 | VARCHAR | 89.9% | R |  |
| f3e03c4 | BIGINT | 89.9% | 535449 |  |
| xf3e03c5 | VARCHAR | 89.9% | R |  |
| f3e03c5 | BIGINT | 89.9% | 169713 |  |
| xf3e03c6 | VARCHAR | 89.9% | Z |  |
| f3e03c6 | BIGINT | 89.9% | 0 |  |
| xf3e03c7 | VARCHAR | 89.9% | R |  |
| f3e03c7 | BIGINT | 89.9% | 2644406 |  |
| xf3e043 | VARCHAR | 89.9% | Z |  |
| f3e043 | DOUBLE | 96.0% | 0.0 |  |
| xf3e044 | VARCHAR | 89.9% | R |  |
| f3e044 | DOUBLE | 96.0% | 54729.0 |  |
| xf3e045 | VARCHAR | 89.9% | R |  |
| f3e045 | DOUBLE | 96.0% | 17347.0 |  |
| xf3e046 | VARCHAR | 89.9% | Z |  |
| f3e046 | DOUBLE | 96.0% | 0.0 |  |
| xf3e047 | VARCHAR | 89.9% | R |  |
| f3e047 | DOUBLE | 96.0% | 334697.0 |  |
| xf3e057 | VARCHAR | 89.9% | Z |  |
| f3e057 | BIGINT | 89.9% | 0 |  |
| xf3e103 | VARCHAR | 89.9% | Z |  |
| f3e103 | DOUBLE | 97.8% | 0.0 |  |
| xf3e104 | VARCHAR | 89.9% | Z |  |
| f3e104 | DOUBLE | 97.8% | 0.0 |  |
| xf3e105 | VARCHAR | 89.9% | Z |  |
| f3e105 | DOUBLE | 97.8% | 0.0 |  |
| xf3e106 | VARCHAR | 89.9% | Z |  |
| f3e106 | DOUBLE | 97.8% | 0.0 |  |
| xf3e107 | VARCHAR | 89.9% | Z |  |
| f3e107 | DOUBLE | 97.8% | 0.0 |  |
| xf3e111 | VARCHAR | 89.9% | R |  |
| f3e111 | BIGINT | 89.9% | 0 |  |
| xf3e112 | VARCHAR | 89.9% | R |  |
| f3e112 | BIGINT | 89.9% | 67421 |  |
| xf3e113 | VARCHAR | 89.9% | R |  |
| f3e113 | BIGINT | 89.9% | 12002 |  |
| xf3e114 | VARCHAR | 89.9% | R |  |
| f3e114 | BIGINT | 89.9% | -1360255 |  |
| xf3e115 | VARCHAR | 89.9% | R |  |
| f3e115 | BIGINT | 89.9% | 63817 |  |
| xf3e116 | VARCHAR | 89.9% | Z |  |
| f3e116 | BIGINT | 89.9% | 0 |  |
| xf3e117 | VARCHAR | 89.9% | R |  |
| f3e117 | BIGINT | 89.9% | 1217015 |  |
| xf3e063 | VARCHAR | 89.9% | R |  |
| f3e063 | BIGINT | 89.9% | 0 |  |
| xf3e064 | VARCHAR | 89.9% | R |  |
| f3e064 | BIGINT | 89.9% | 0 |  |
| xf3e065 | VARCHAR | 89.9% | R |  |
| f3e065 | BIGINT | 89.9% | 0 |  |
| xf3e066 | VARCHAR | 89.9% | Z |  |
| f3e066 | BIGINT | 89.9% | 0 |  |
| xf3e067 | VARCHAR | 89.9% | R |  |
| f3e067 | BIGINT | 89.9% | 0 |  |
| xf3e01 | VARCHAR | 43.8% | R |  |
| f3e01 | DOUBLE | 43.9% | 2959765.0 |  |
| xf3e02 | VARCHAR | 43.8% | R |  |
| f3e02 | DOUBLE | 43.9% | 0.0 |  |
| xf3e03 | VARCHAR | 43.8% | R |  |
| f3e03 | DOUBLE | 43.9% | 8697494.0 |  |
| xf3e04 | VARCHAR | 43.8% | R |  |
| f3e04 | DOUBLE | 58.7% | 463998.0 |  |
| xf3e05 | VARCHAR | 43.8% | R |  |
| f3e05 | DOUBLE | 43.9% | 0.0 |  |
| xf3e06 | VARCHAR | 43.8% | R |  |
| f3e06 | DOUBLE | 43.9% | 0.0 |  |
| xf3e07 | VARCHAR | 43.8% | R |  |
| f3e07 | DOUBLE | 43.9% | 12121257.0 |  |

## flags

Rows: 153,757

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| stat_ic | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| lock_ic | BIGINT | 0.0% | 8 | Appears in 3 tables, common join key |
| imp_ic | BIGINT | 0.0% | -2 |  |
| stat_c | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| lock_c | BIGINT | 0.0% | 8 | Appears in 3 tables, common join key |
| prch_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| idx_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| pcc_f | VARCHAR | 39.3% | 96.0 |  |
| imp_c | BIGINT | 0.0% | -2 | Appears in 3 tables, common join key |
| stat_e12 | BIGINT | 13.6% | 1 |  |
| lock_e12 | BIGINT | 13.6% | 8 |  |
| prch_e12 | BIGINT | 13.6% | -2 |  |
| idx_e12 | BIGINT | 13.6% | -2 |  |
| pce12_f | VARCHAR | 39.5% | 91.0 |  |
| imp_e12 | BIGINT | 13.6% | -2 |  |
| enrhsst | BIGINT | 92.2% | 1 |  |
| enrhsst1 | BIGINT | 92.2% | 1 |  |
| enrhsst2 | BIGINT | 92.2% | 0 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| stat_cos | BIGINT | 96.1% | 1 |  |
| stat_cos1 | BIGINT | 96.1% | 1 |  |
| lock_cos1 | BIGINT | 96.1% | 8 |  |
| prch_cos | BIGINT | 96.1% | -2 |  |
| idx_cos | BIGINT | 96.1% | -2 |  |
| pccos_f | DOUBLE | 100.0% |  |  |
| imp_cos1 | BIGINT | 96.1% | -2 |  |
| stat_cos2 | BIGINT | 96.1% | 1 |  |
| lock_cos2 | BIGINT | 96.1% | 8 |  |
| imp_cos2 | BIGINT | 96.1% | -2 |  |
| stat_sfa | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| lock_sfa | BIGINT | 3.9% | 8 | Appears in 3 tables, common join key |
| prch_sfa | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| idx_sfa | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| pcsfa_f | VARCHAR | 39.4% | 100.0 |  |
| imp_sfa | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| sfaform | BIGINT | 51.5% | 2 |  |
| stat_gr | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| lock_gr | BIGINT | 3.9% | 8 | Appears in 3 tables, common join key |
| prch_gr | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| idx_gr | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| pcgr_f | VARCHAR | 39.4% | . |  |
| imp_gr | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| cohrtstu | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| stat_gr2 | BIGINT | 26.8% | 1 |  |
| lock_gr2 | BIGINT | 26.8% | 8 |  |
| prch_gr2 | BIGINT | 26.8% | -2 |  |
| idx_gr2 | DOUBLE | 26.8% | -2.0 |  |
| pcgr2_f | VARCHAR | 64.4% | . |  |
| imp_gr2 | BIGINT | 26.8% | -2 |  |
| stat_om | BIGINT | 56.5% | 1 |  |
| lock_om | BIGINT | 56.5% | 8 |  |
| prch_om | BIGINT | 56.5% | -2 |  |
| idx_om | BIGINT | 56.5% | -2 |  |
| pcom_f | VARCHAR | 64.4% | . |  |
| imp_om | BIGINT | 56.5% | -2 |  |
| stat_adm | BIGINT | 51.5% | 1 |  |
| lock_adm | BIGINT | 51.5% | 8 |  |
| prch_adm | BIGINT | 75.4% | -2 |  |
| idx_adm | BIGINT | 75.4% | -2 |  |
| pcadm_f | VARCHAR | 83.4% | . |  |
| imp_adm | BIGINT | 51.5% | -2 |  |
| stat_hr | BIGINT | 8.4% | 1 |  |
| lock_hr | BIGINT | 8.4% | 8 |  |
| prch_hr | BIGINT | 8.4% | -2 |  |
| idx_hr | BIGINT | 8.4% | -2 |  |
| pchr_f | VARCHAR | 39.2% | 90.0 |  |
| imp_hr | BIGINT | 8.4% | -2 |  |
| ftemp15 | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| tenursys | BIGINT | 41.4% | 1 | Appears in 3 tables, common join key |
| sa_excl | BIGINT | 3.9% | 2 | Appears in 3 tables, common join key |
| stat_eap | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| stat_sa | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| stat_s | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| stat_ef | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| lock_ef | BIGINT | 3.9% | 8 | Appears in 3 tables, common join key |
| prch_ef | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| idx_ef | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| pcef_f | VARCHAR | 39.4% | 90.0 |  |
| imp_ef | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| pta99_ef | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| ptacipef | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| ptb_ef | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| ptc_ef | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| ptd_ef | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| stat_f | BIGINT | 3.9% | 1 | Appears in 3 tables, common join key |
| lock_f | BIGINT | 3.9% | 8 | Appears in 3 tables, common join key |
| prch_f | DOUBLE | 4.3% | -2.0 | Appears in 3 tables, common join key |
| idx_f | DOUBLE | 4.3% | -2.0 | Appears in 3 tables, common join key |
| pcf_f | VARCHAR | 37.1% | 45.0 |  |
| prchtp_f | BIGINT | 61.4% | -2 |  |
| imp_f | BIGINT | 3.9% | -2 | Appears in 3 tables, common join key |
| form_f | BIGINT | 3.9% | 4 | Appears in 3 tables, common join key |
| fybeg | BIGINT | 3.9% | 102023 | Appears in 3 tables, common join key |
| fyend | BIGINT | 3.9% | 92024 | Appears in 3 tables, common join key |
| gpfs | BIGINT | 3.9% | 3 | Appears in 3 tables, common join key |
| f1gasbal | BIGINT | 3.9% | 3 | Appears in 3 tables, common join key |
| f2pell | BIGINT | 8.4% | -2 |  |
| f3pell | BIGINT | 36.4% | -2 |  |
| fcolathl | BIGINT | 88.0% | 1 |  |
| f_athex1 | BIGINT | 88.0% | 1 |  |
| f_athex2 | BIGINT | 88.0% | 0 |  |
| f_athex9 | BIGINT | 88.0% | 0 |  |
| f_athrv | BIGINT | 88.0% | 1 |  |
| f_athrv1 | BIGINT | 79.7% | 0 |  |
| f_athrv2 | BIGINT | 79.7% | 1 |  |
| f_athrv9 | BIGINT | 79.7% | 0 |  |
| f3bist | BIGINT | 51.5% | -2 |  |
| stat_al | BIGINT | 51.5% | 1 |  |
| lock_al | BIGINT | 51.5% | 8 |  |
| prch_al | BIGINT | 51.5% | -2 |  |
| idx_al | BIGINT | 51.5% | -2 |  |
| pcal_f | VARCHAR | 58.9% | 100.0 |  |
| imp_al | BIGINT | 51.5% | -2 |  |
| hasal | BIGINT | 51.5% | 1 |  |
| ntrldstr | BIGINT | 22.1% | 0 |  |
| rev_c | BIGINT | 3.9% | 0 | Appears in 3 tables, common join key |
| rev_e12 | BIGINT | 17.5% | 0 |  |
| rev_ic | BIGINT | 22.1% | 0 |  |
| rev_gr | BIGINT | 7.8% | 0 | Appears in 3 tables, common join key |
| rev_gr2 | BIGINT | 30.7% | 0 |  |
| rev_om | BIGINT | 60.4% | 0 |  |
| rev_sfa | BIGINT | 7.8% | 0 | Appears in 3 tables, common join key |
| rev_adm | BIGINT | 55.4% | 0 |  |
| rev_hr | BIGINT | 12.3% | 0 |  |
| rev_f | BIGINT | 7.8% | 0 | Appears in 3 tables, common join key |
| rev_ef | BIGINT | 7.8% | 0 | Appears in 3 tables, common join key |
| rev_al | BIGINT | 55.4% | 0 |  |
| f_athltc | BIGINT | 20.4% | 1 |  |
| f_athrv3 | BIGINT | 91.7% | 0 |  |
| omflg1gr | BIGINT | 95.0% | -2 |  |
| omflg2gr | BIGINT | 95.0% | 0 |  |
| omflg3gr | BIGINT | 95.0% | -2 |  |
| omflg4 | BIGINT | 95.0% | 0 |  |
| omflg5 | BIGINT | 95.0% | 0 |  |
| omflg6gr | BIGINT | 95.0% | 0 |  |
| pcf_f_rv | VARCHAR | 85.1% | . |  |
| hasgrurl | BIGINT | 66.1% | 1 |  |
| grdisurl | VARCHAR | 66.1% | www.aamu.edu |  |
| re_c | BIGINT | 85.7% | 2 |  |
| re_e12 | BIGINT | 85.7% | -1 |  |
| fyrpyear | BIGINT | 67.5% | -1 | Appears in 4 tables, common join key |
| longpgm | BIGINT | 67.5% | -1 | Appears in 3 tables, common join key |
| re_gr | BIGINT | 85.7% | -1 |  |
| fp_c | BIGINT | 90.6% | -2 |  |
| fp_e12 | BIGINT | 90.6% | -2 |  |
| re_hr | BIGINT | 90.6% | -1 |  |
| re_ef | BIGINT | 90.6% | -1 |  |
| f_ver | BIGINT | 90.6% | -1 |  |
| cufasb | BIGINT | 72.4% | -1 | Appears in 3 tables, common join key |
| cugasb | BIGINT | 72.4% | -1 | Appears in 3 tables, common join key |
| f1systyp | BIGINT | 72.4% | 1 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 72.4% | Air University | Appears in 3 tables, common join key |
| fp_ic | BIGINT | 95.4% | -2 |  |
| fp_ef | BIGINT | 95.4% | -2 |  |
| pteeffy | BIGINT | 86.4% | 5 | Appears in 3 tables, common join key |
| pteefia | BIGINT | 86.4% | 5 | Appears in 3 tables, common join key |
| pyaid | BIGINT | 86.4% | 2 | Appears in 3 tables, common join key |
| sport1 | BIGINT | 86.4% | -1 | Appears in 4 tables, common join key |
| sport2 | BIGINT | 86.4% | -1 | Appears in 4 tables, common join key |
| sport3 | BIGINT | 86.4% | -1 | Appears in 4 tables, common join key |
| sport4 | BIGINT | 86.4% | -1 | Appears in 4 tables, common join key |
| sport5 | BIGINT | 86.4% | -1 | Appears in 3 tables, common join key |
| ndst2005 | BIGINT | 95.4% | 0 |  |
| lock_sa | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| prch_sa | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| idx_sa | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| imp_sa | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| lock_s | BIGINT | 95.5% | 0 | Appears in 3 tables, common join key |
| prch_s | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| idx_s | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| imp_s | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| lock_eap | BIGINT | 95.5% | 0 | Appears in 3 tables, common join key |
| prch_eap | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| idx_eap | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| imp_eap | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| cohrtaid | BIGINT | 95.5% | -1 | Appears in 3 tables, common join key |
| pcf_m | BIGINT | 95.5% | -2 |  |
| pcffp_m | BIGINT | 95.5% | -2 |  |
| pcffp_f | DOUBLE | 99.7% | 10.0 |  |
| pcc_m | BIGINT | 95.5% | -2 |  |
| pcef_m | BIGINT | 95.5% | -2 |  |
| pcgr_m | BIGINT | 95.5% | -2 |  |
| pcsfa_m | BIGINT | 95.5% | -2 |  |
| pceap_m | BIGINT | 95.5% | -2 |  |
| pceap_f | DOUBLE | 99.9% | 3.0 |  |
| pcsa_m | BIGINT | 95.5% | -2 |  |
| pcsa_f | DOUBLE | 100.0% | 3.0 |  |
| pcs_m | BIGINT | 95.5% | -2 |  |
| pcs_f | DOUBLE | 100.0% | 78.0 |  |
| rev_sa | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| rev_s | BIGINT | 95.5% | 0 | Appears in 3 tables, common join key |
| rev_eap | BIGINT | 95.5% | 0 | Appears in 3 tables, common join key |

## gr

Rows: 1,251,920

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| grtype | DOUBLE | 0.0% | 1.0 |  |
| chrtstat | DOUBLE | 0.2% | 10.0 |  |
| section | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| cohort | BIGINT | 0.0% | 1 |  |
| line | DOUBLE | 30.1% | 999.0 | Appears in 4 tables, common join key |
| xgrtotlt | VARCHAR | 30.7% | R |  |
| grtotlt | BIGINT | 30.7% | 1402 |  |
| xgrtotlm | VARCHAR | 30.7% | R |  |
| grtotlm | DOUBLE | 36.6% | 571.0 |  |
| xgrtotlw | VARCHAR | 30.7% | R |  |
| grtotlw | DOUBLE | 36.6% | 831.0 |  |
| xgraiant | VARCHAR | 30.7% | R |  |
| graiant | DOUBLE | 43.7% | 3.0 |  |
| xgraianm | VARCHAR | 30.7% | R |  |
| graianm | DOUBLE | 43.7% | 2.0 |  |
| xgraianw | VARCHAR | 30.7% | R |  |
| graianw | DOUBLE | 43.7% | 1.0 |  |
| xgrasiat | VARCHAR | 30.7% | R |  |
| grasiat | DOUBLE | 43.7% | 2.0 |  |
| xgrasiam | VARCHAR | 30.7% | R |  |
| grasiam | DOUBLE | 43.7% | 1.0 |  |
| xgrasiaw | VARCHAR | 30.7% | R |  |
| grasiaw | DOUBLE | 43.7% | 1.0 |  |
| xgrbkaat | VARCHAR | 30.7% | R |  |
| grbkaat | DOUBLE | 43.7% | 1297.0 |  |
| xgrbkaam | VARCHAR | 30.7% | R |  |
| grbkaam | DOUBLE | 43.7% | 522.0 |  |
| xgrbkaaw | VARCHAR | 30.7% | R |  |
| grbkaaw | DOUBLE | 43.7% | 775.0 |  |
| xgrhispt | VARCHAR | 30.7% | R |  |
| grhispt | DOUBLE | 43.7% | 11.0 |  |
| xgrhispm | VARCHAR | 30.7% | R |  |
| grhispm | DOUBLE | 43.7% | 6.0 |  |
| xgrhispw | VARCHAR | 30.7% | R |  |
| grhispw | DOUBLE | 43.7% | 5.0 |  |
| xgrnhpit | VARCHAR | 30.7% | R |  |
| grnhpit | DOUBLE | 43.7% | 1.0 |  |
| xgrnhpim | VARCHAR | 30.7% | Z |  |
| grnhpim | DOUBLE | 43.7% | 0.0 |  |
| xgrnhpiw | VARCHAR | 30.7% | R |  |
| grnhpiw | DOUBLE | 43.7% | 1.0 |  |
| xgrwhitt | VARCHAR | 30.7% | R |  |
| grwhitt | DOUBLE | 43.7% | 17.0 |  |
| xgrwhitm | VARCHAR | 30.7% | R |  |
| grwhitm | DOUBLE | 43.7% | 12.0 |  |
| xgrwhitw | VARCHAR | 30.7% | R |  |
| grwhitw | DOUBLE | 43.7% | 5.0 |  |
| xgr2mort | VARCHAR | 30.7% | R |  |
| gr2mort | DOUBLE | 43.7% | 18.0 |  |
| xgr2morm | VARCHAR | 30.7% | R |  |
| gr2morm | DOUBLE | 43.7% | 2.0 |  |
| xgr2morw | VARCHAR | 30.7% | R |  |
| gr2morw | DOUBLE | 43.7% | 16.0 |  |
| xgrunknt | VARCHAR | 30.7% | R |  |
| grunknt | DOUBLE | 36.6% | 50.0 |  |
| xgrunknm | VARCHAR | 30.7% | R |  |
| grunknm | DOUBLE | 36.6% | 25.0 |  |
| xgrunknw | VARCHAR | 30.7% | R |  |
| grunknw | DOUBLE | 36.6% | 25.0 |  |
| xgrnralt | VARCHAR | 30.7% | R |  |
| grnralt | DOUBLE | 36.6% | 3.0 |  |
| xgrnralm | VARCHAR | 30.7% | R |  |
| grnralm | DOUBLE | 36.6% | 1.0 |  |
| xgrnralw | VARCHAR | 30.7% | R |  |
| grnralw | DOUBLE | 36.6% | 2.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xgrrac03 | VARCHAR | 59.6% | R |  |
| grrace03 | DOUBLE | 61.8% | 576.0 |  |
| xgrrac04 | VARCHAR | 59.6% | R |  |
| grrace04 | DOUBLE | 61.8% | 595.0 |  |
| xgrrac05 | VARCHAR | 59.6% | Z |  |
| grrace05 | DOUBLE | 61.8% | 0.0 |  |
| xgrrac06 | VARCHAR | 59.6% | R |  |
| grrace06 | DOUBLE | 61.8% | 1.0 |  |
| xgrrac07 | VARCHAR | 59.6% | Z |  |
| grrace07 | DOUBLE | 61.8% | 0.0 |  |
| xgrrac08 | VARCHAR | 59.6% | Z |  |
| grrace08 | DOUBLE | 61.8% | 0.0 |  |
| xgrrac09 | VARCHAR | 59.6% | R |  |
| grrace09 | DOUBLE | 61.8% | 1.0 |  |
| xgrrac10 | VARCHAR | 59.6% | R |  |
| grrace10 | DOUBLE | 61.8% | 3.0 |  |
| xgrrac11 | VARCHAR | 59.6% | R |  |
| grrace11 | DOUBLE | 61.8% | 3.0 |  |
| xgrrac12 | VARCHAR | 59.6% | R |  |
| grrace12 | DOUBLE | 61.8% | 7.0 |  |
| xgrrac18 | VARCHAR | 59.6% | R |  |
| grrace18 | DOUBLE | 61.8% | 1171.0 |  |
| xgrrac19 | VARCHAR | 59.6% | R |  |
| grrace19 | DOUBLE | 61.8% | 1.0 |  |
| xgrrac20 | VARCHAR | 59.6% | Z |  |
| grrace20 | DOUBLE | 61.8% | 0.0 |  |
| xgrrac21 | VARCHAR | 59.6% | R |  |
| grrace21 | DOUBLE | 61.8% | 4.0 |  |
| xgrrac22 | VARCHAR | 59.6% | R |  |
| grrace22 | DOUBLE | 61.8% | 10.0 |  |
| xdvgrait | VARCHAR | 90.3% | R |  |
| dvgrait | DOUBLE | 91.1% | 1.0 |  |
| xdvgraim | VARCHAR | 90.3% | Z |  |
| dvgraim | DOUBLE | 91.1% | 0.0 |  |
| xdvgraiw | VARCHAR | 90.3% | R |  |
| dvgraiw | DOUBLE | 91.1% | 1.0 |  |
| xdvgrapt | VARCHAR | 90.3% | Z |  |
| dvgrapt | DOUBLE | 91.1% | 0.0 |  |
| xdvgrapm | VARCHAR | 90.3% | Z |  |
| dvgrapm | DOUBLE | 91.1% | 0.0 |  |
| xdvgrapw | VARCHAR | 90.3% | Z |  |
| dvgrapw | DOUBLE | 91.1% | 0.0 |  |
| xdvgrbkt | VARCHAR | 90.3% | R |  |
| dvgrbkt | DOUBLE | 91.1% | 1171.0 |  |
| xdvgrbkm | VARCHAR | 90.3% | R |  |
| dvgrbkm | DOUBLE | 91.1% | 576.0 |  |
| xdvgrbkw | VARCHAR | 90.3% | R |  |
| dvgrbkw | DOUBLE | 91.1% | 595.0 |  |
| xdvgrhst | VARCHAR | 90.3% | R |  |
| dvgrhst | DOUBLE | 91.1% | 4.0 |  |
| xdvgrhsm | VARCHAR | 90.3% | R |  |
| dvgrhsm | DOUBLE | 91.1% | 1.0 |  |
| xdvgrhsw | VARCHAR | 90.3% | R |  |
| dvgrhsw | DOUBLE | 91.1% | 3.0 |  |
| xdvgrwht | VARCHAR | 90.3% | R |  |
| dvgrwht | DOUBLE | 91.1% | 10.0 |  |
| xdvgrwhm | VARCHAR | 90.3% | R |  |
| dvgrwhm | DOUBLE | 91.1% | 3.0 |  |
| xdvgrwhw | VARCHAR | 90.3% | R |  |
| dvgrwhw | DOUBLE | 91.1% | 7.0 |  |
| xgrrac01 | VARCHAR | 69.3% | R |  |
| grrace01 | BIGINT | 69.3% | 13 |  |
| xgrrac02 | VARCHAR | 69.3% | R |  |
| grrace02 | BIGINT | 69.3% | 15 |  |
| xgrrac13 | VARCHAR | 69.3% | R |  |
| grrace13 | BIGINT | 69.3% | 0 |  |
| xgrrac14 | VARCHAR | 69.3% | R |  |
| grrace14 | BIGINT | 69.3% | 0 |  |
| xgrrac15 | VARCHAR | 69.3% | R |  |
| grrace15 | BIGINT | 69.3% | 497 |  |
| xgrrac16 | VARCHAR | 69.3% | R |  |
| grrace16 | BIGINT | 69.3% | 541 |  |
| xgrrac17 | VARCHAR | 69.3% | R |  |
| grrace17 | BIGINT | 69.3% | 28 |  |
| xgrrac23 | VARCHAR | 69.3% | R |  |
| grrace23 | BIGINT | 69.3% | 0 |  |
| xgrrac24 | VARCHAR | 69.3% | R |  |
| grrace24 | BIGINT | 69.3% | 1038 |  |

## gr200

Rows: 93,086

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xbarevct | VARCHAR | 0.0% | R |  |
| barevct | DOUBLE | 62.9% | 1407.0 |  |
| xbaexclu | VARCHAR | 0.0% | R |  |
| baexclu | DOUBLE | 62.9% | 3.0 |  |
| xbaac150 | VARCHAR | 0.0% | R |  |
| baac150 | DOUBLE | 62.9% | 1404.0 |  |
| xbanc100 | VARCHAR | 0.0% | R |  |
| banc100 | DOUBLE | 62.9% | 178.0 |  |
| xbagr100 | VARCHAR | 0.0% | R |  |
| bagr100 | DOUBLE | 62.9% | 13.0 |  |
| xbanc150 | VARCHAR | 0.0% | R |  |
| banc150 | DOUBLE | 62.9% | 376.0 |  |
| xbagr150 | VARCHAR | 0.0% | R |  |
| bagr150 | DOUBLE | 62.9% | 27.0 |  |
| xbaaexcl | VARCHAR | 0.0% | R |  |
| baaexcl | DOUBLE | 62.9% | 0.0 |  |
| xbaac200 | VARCHAR | 0.0% | R |  |
| baac200 | DOUBLE | 62.9% | 1404.0 |  |
| xbanc20a | VARCHAR | 0.0% | R |  |
| banc200a | DOUBLE | 62.9% | 43.0 |  |
| xbastend | VARCHAR | 18.3% | R |  |
| bastend | DOUBLE | 69.3% | 2.0 |  |
| xbanc200 | VARCHAR | 0.0% | R |  |
| banc200 | DOUBLE | 62.9% | 419.0 |  |
| xbagr200 | VARCHAR | 0.0% | R |  |
| bagr200 | DOUBLE | 62.9% | 30.0 |  |
| xl4revct | VARCHAR | 0.0% | A |  |
| l4revct | DOUBLE | 37.1% | 225.0 |  |
| xl4exclu | VARCHAR | 0.0% | A |  |
| l4exclu | DOUBLE | 37.1% | 0.0 |  |
| xl4ac150 | VARCHAR | 0.0% | A |  |
| l4ac150 | DOUBLE | 37.1% | 225.0 |  |
| xl4nc100 | VARCHAR | 0.0% | A |  |
| l4nc100 | DOUBLE | 37.1% | 42.0 |  |
| xl4gr100 | VARCHAR | 0.0% | A |  |
| l4gr100 | DOUBLE | 37.1% | 19.0 |  |
| xl4nc150 | VARCHAR | 0.0% | A |  |
| l4nc150 | DOUBLE | 37.1% | 54.0 |  |
| xl4gr150 | VARCHAR | 0.0% | A |  |
| l4gr150 | DOUBLE | 37.1% | 24.0 |  |
| xl4aexcl | VARCHAR | 0.0% | A |  |
| l4aexcl | DOUBLE | 37.1% | 0.0 |  |
| xl4ac200 | VARCHAR | 0.0% | A |  |
| l4ac200 | DOUBLE | 37.1% | 225.0 |  |
| xl4nc20a | VARCHAR | 0.0% | A |  |
| l4nc200a | DOUBLE | 37.1% | 17.0 |  |
| xl4stend | VARCHAR | 18.3% | A |  |
| l4stend | DOUBLE | 49.0% | 9.0 |  |
| xl4nc200 | VARCHAR | 0.0% | A |  |
| l4nc200 | DOUBLE | 37.1% | 71.0 |  |
| xl4gr200 | VARCHAR | 0.0% | A |  |
| l4gr200 | DOUBLE | 37.1% | 32.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |

## hd

Rows: 168,427

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| institution_name | VARCHAR | 0.0% | Alabama A & M University | Appears in 4 tables, common join key |
| ialias | VARCHAR | 23.1% | AAMU |  |
| addr | VARCHAR | 0.2% | 4900 Meridian Street |  |
| city | VARCHAR | 0.0% | Normal |  |
| state | VARCHAR | 0.0% | AL | Appears in 4 tables, common join key |
| zip_code | VARCHAR | 0.0% | 35762 |  |
| fips_state | BIGINT | 0.0% | 1 |  |
| region | BIGINT | 0.0% | 5 |  |
| chfnm | VARCHAR | 0.2% | Dr. Daniel K. Wims |  |
| chftitle | VARCHAR | 0.3% | President |  |
| gentele | DOUBLE | 0.9% | 2563725000.0 |  |
| ein | DOUBLE | 0.9% | 636001097.0 |  |
| ueis | VARCHAR | 86.4% | JDVGS67MSLH7 |  |
| opeid | DOUBLE | 0.9% | 100200.0 |  |
| opeflag | BIGINT | 0.0% | 1 |  |
| website | VARCHAR | 1.6% | www.aamu.edu/ |  |
| adminurl | VARCHAR | 25.2% | https://www.aamu.edu/admissions-aid/index.html |  |
| faidurl | VARCHAR | 25.3% | https://www.aamu.edu/admissions-aid/financial-aid/ |  |
| applurl | VARCHAR | 26.2% | https://www.aamu.edu/admissions-aid/undergraduate-admissions/apply-today.html |  |
| npricurl | VARCHAR | 38.7% | www.aamu.edu/admissions-aid/tuition-fees/net-price-calculator.html |  |
| veturl | VARCHAR | 56.2% | https://www.uab.edu/students/veterans |  |
| athurl | VARCHAR | 59.9% | https://www.uab.edu/registrar/students |  |
| disaurl | VARCHAR | 61.4% | https://www.aamu.edu/administrativeoffices/VADS/Pages/Disability-Services.aspx |  |
| sector | BIGINT | 0.0% | 1 | Appears in 3 tables, common join key |
| level | BIGINT | 0.0% | 1 |  |
| control | BIGINT | 0.0% | 1 |  |
| hloffer | BIGINT | 0.0% | 9 |  |
| ugoffer | BIGINT | 0.0% | 1 |  |
| groffer | BIGINT | 0.0% | 1 |  |
| hdegofr1 | BIGINT | 29.6% | 12 |  |
| degree_granting | BIGINT | 0.0% | 1 |  |
| hbcu | BIGINT | 0.0% | 1 |  |
| hospital | BIGINT | 0.0% | 2 |  |
| medical | BIGINT | 0.0% | 2 |  |
| tribal | BIGINT | 0.0% | 2 |  |
| locale_code | BIGINT | 0.0% | 12 |  |
| openpubl | BIGINT | 0.0% | 1 |  |
| act | VARCHAR | 0.0% | A |  |
| newid | DOUBLE | 0.1% | -2.0 |  |
| deathyr | BIGINT | 0.0% | -2 |  |
| close_date | DOUBLE | 1.6% | -2.0 |  |
| currently_active | BIGINT | 0.0% | 1 |  |
| postsec | BIGINT | 0.0% | 1 |  |
| pseflag | BIGINT | 0.0% | 1 |  |
| pset4flg | BIGINT | 0.0% | 1 |  |
| rptmth | BIGINT | 8.7% | 1 |  |
| instcat | BIGINT | 8.7% | 2 |  |
| c00carnegie | BIGINT | 92.8% | 16 |  |
| carnegie_basic | BIGINT | 0.0% | 18 |  |
| carnegieic | BIGINT | 92.8% | 9 |  |
| carnegiesaec | BIGINT | 92.8% | 4 |  |
| carnegiersch | BIGINT | 92.8% | 3 |  |
| carnegiesize | BIGINT | 92.8% | 3 |  |
| carnegiealf | BIGINT | 92.8% | 4 |  |
| carnegieapm | BIGINT | 92.8% | 1 |  |
| carnegiegpm | BIGINT | 92.8% | 2 |  |
| land_grant | BIGINT | 12.8% | 1 |  |
| size_category | BIGINT | 12.8% | 3 |  |
| f1systyp | BIGINT | 29.8% | 2 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 32.0% | The University of Alabama System | Appears in 3 tables, common join key |
| f1syscod | BIGINT | 47.5% | -2 |  |
| cbsa | BIGINT | 21.2% | 26620 |  |
| cbsatype | BIGINT | 21.2% | 1 |  |
| csa | BIGINT | 21.2% | 290 |  |
| county_fips | BIGINT | 29.6% | 1089 |  |
| county_name | VARCHAR | 29.7% | Madison County |  |
| cngdstcd | BIGINT | 29.6% | 105 |  |
| longitude | DOUBLE | 29.6% | -86.568502 |  |
| latitude | DOUBLE | 29.6% | 34.783368 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| dfrcgid | BIGINT | 29.7% | 106 |  |
| dfrcuscg | BIGINT | 51.1% | 1 |  |
| c21ipug | BIGINT | 88.9% | 16 |  |
| c21ipgrd | BIGINT | 88.9% | 18 |  |
| c21ugprf | BIGINT | 88.9% | 10 |  |
| c21enprf | BIGINT | 88.9% | 4 |  |
| c21szset | BIGINT | 88.9% | 14 |  |
| c18basic | BIGINT | 88.9% | 18 |  |
| c15basic | BIGINT | 77.1% | 18 |  |
| ccbasic | BIGINT | 63.9% | 18 |  |
| carnegie | BIGINT | 20.0% | 16 |  |
| duns | DOUBLE | 59.3% | 197216455.0 |  |
| necta | BIGINT | 35.7% | -2 |  |
| c18ipug | BIGINT | 88.2% | 16 |  |
| c18ipgrd | BIGINT | 88.2% | 17 |  |
| c18ugprf | BIGINT | 88.2% | 10 |  |
| c18enprf | BIGINT | 88.2% | 4 |  |
| c18szset | BIGINT | 88.2% | 14 |  |
| c15ipug | BIGINT | 86.7% | 16 |  |
| c15ipgrd | BIGINT | 86.7% | 18 |  |
| c15ugprf | BIGINT | 86.7% | 10 |  |
| c15enprf | BIGINT | 86.7% | 4 |  |
| c15szset | BIGINT | 86.7% | 13 |  |
| ccipug | BIGINT | 56.1% | -3 |  |
| ccipgrad | BIGINT | 56.1% | -3 |  |
| ccugprof | BIGINT | 56.1% | -3 |  |
| ccenrprf | BIGINT | 56.1% | -3 |  |
| ccsizset | BIGINT | 56.1% | -3 |  |
| faxtele | DOUBLE | 85.6% | 2563725030.0 |  |
| tenursys | BIGINT | 65.8% | -1 | Appears in 3 tables, common join key |
| fpoffer | BIGINT | 70.4% | 2 |  |
| hdegoffr | BIGINT | 70.4% | 40 |  |
| fintele | DOUBLE | 79.1% | 3349532223.0 |  |
| admtele | DOUBLE | 79.0% | 3349532223.0 |  |
| stat_fa | BIGINT | 91.3% | 1 |  |
| stat_ic | BIGINT | 91.3% | 1 | Appears in 3 tables, common join key |
| lock_ic | BIGINT | 91.3% | 3 | Appears in 3 tables, common join key |
| stat_c | BIGINT | 91.3% | 1 | Appears in 3 tables, common join key |
| lock_c | BIGINT | 91.3% | 8 | Appears in 3 tables, common join key |
| prch_c | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_c | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_c | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_wi | BIGINT | 91.3% | 5 |  |
| stat_ef | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_ef | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_ef | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_ef | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_ef | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| pta99_ef | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| ptb_ef | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| ptc_ef | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| ptd_ef | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| pteeffy | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| pteefia | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| fyrpyear | BIGINT | 91.3% | -1 | Appears in 4 tables, common join key |
| stat_sa | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_sa | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_sa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_sa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_sa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_s | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_s | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_s | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_s | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_s | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_eap | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_eap | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_eap | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_eap | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_eap | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| ftemp15 | BIGINT | 91.3% | 1 | Appears in 3 tables, common join key |
| sa_excl | BIGINT | 91.3% | 2 | Appears in 3 tables, common join key |
| stat_sp | BIGINT | 91.3% | 5 |  |
| form_f | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_f | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_f | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_f | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_f | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_f | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| fybeg | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| fyend | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| gpfs | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| f1gasbcr | BIGINT | 91.3% | -2 |  |
| f1gasbal | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_sfa | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_sfa | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_sfa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_sfa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_sfa | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| stat_gr | BIGINT | 91.3% | 5 | Appears in 3 tables, common join key |
| lock_gr | BIGINT | 91.3% | 0 | Appears in 3 tables, common join key |
| prch_gr | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| idx_gr | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| imp_gr | BIGINT | 91.3% | -2 | Appears in 3 tables, common join key |
| cohrtstu | BIGINT | 91.3% | 1 | Appears in 3 tables, common join key |
| pyaid | BIGINT | 91.3% | 2 | Appears in 3 tables, common join key |
| cohrtaid | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| sport1 | BIGINT | 91.3% | -1 | Appears in 4 tables, common join key |
| sport2 | BIGINT | 91.3% | -1 | Appears in 4 tables, common join key |
| sport3 | BIGINT | 91.3% | -1 | Appears in 4 tables, common join key |
| sport4 | BIGINT | 91.3% | -1 | Appears in 4 tables, common join key |
| sport5 | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| longpgm | BIGINT | 91.3% | -1 | Appears in 3 tables, common join key |
| cohrtmt | BIGINT | 91.3% | 1 |  |
| tpr | BIGINT | 91.3% | -1 |  |
| hpr | BIGINT | 91.3% | -1 |  |
| cufasb | BIGINT | 95.8% | -2 | Appears in 3 tables, common join key |
| cugasb | BIGINT | 95.8% | -2 | Appears in 3 tables, common join key |
| fte | DOUBLE | 92.2% | 5881.0 |  |
| ocrmsi | BIGINT | 91.3% | -2 |  |
| ocrhsi | BIGINT | 91.3% | -2 |  |
| twoyrcat | BIGINT | 95.8% | -4 |  |
| rev_c | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_ef | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_sa | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_s | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_eap | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| r_form_f | BIGINT | 95.8% | -2 |  |
| rev_f | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_sfa | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| rev_gr | BIGINT | 95.8% | 0 | Appears in 3 tables, common join key |
| affil | BIGINT | 95.5% | -3 |  |
| pctmin1 | BIGINT | 95.5% | -1 |  |
| pctmin2 | BIGINT | 95.5% | -1 |  |
| pctmin3 | BIGINT | 95.5% | -1 |  |
| pctmin4 | BIGINT | 95.5% | -1 |  |
| ptacipef | BIGINT | 95.5% | -2 | Appears in 3 tables, common join key |
| transver | BIGINT | 95.5% | -1 |  |
| cindon | DOUBLE | 97.7% | 9340.0 | Appears in 3 tables, common join key |
| cinson | DOUBLE | 97.7% | 9340.0 | Appears in 3 tables, common join key |
| cotson | DOUBLE | 97.7% | 11860.0 | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 97.8% | 11340.0 | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 97.8% | 11340.0 | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 97.8% | 13860.0 | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 97.7% | 4440.0 | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 97.7% | 4440.0 | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 97.7% | 6960.0 | Appears in 3 tables, common join key |

## ic

Rows: 180,346

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| peo1istr | BIGINT | 0.0% | 0 |  |
| peo2istr | BIGINT | 0.0% | 1 |  |
| peo3istr | BIGINT | 0.0% | 0 |  |
| peo4istr | BIGINT | 0.0% | 0 |  |
| peo5istr | BIGINT | 0.0% | 0 |  |
| peo6istr | BIGINT | 0.0% | 0 |  |
| peo7istr | BIGINT | 86.7% | 0 |  |
| cntlaffi | BIGINT | 0.0% | 1 |  |
| pubprime | BIGINT | 0.0% | 2 |  |
| pubsecon | BIGINT | 0.0% | 0 |  |
| relaffil | BIGINT | 0.0% | -2 |  |
| level1 | BIGINT | 0.0% | 0 |  |
| level1a | BIGINT | 79.8% | 0 |  |
| level1b | BIGINT | 79.8% | 0 |  |
| level2 | BIGINT | 0.0% | 0 |  |
| level3 | BIGINT | 0.0% | 0 |  |
| level4 | BIGINT | 0.0% | 0 |  |
| level5 | BIGINT | 0.0% | 1 |  |
| level6 | BIGINT | 0.0% | 0 |  |
| level7 | BIGINT | 0.0% | 1 |  |
| level8 | BIGINT | 0.0% | 1 |  |
| level12 | BIGINT | 0.0% | 0 |  |
| level17 | BIGINT | 31.9% | 1 |  |
| level18 | BIGINT | 31.9% | 0 |  |
| level19 | BIGINT | 31.9% | 0 |  |
| calsys | BIGINT | 0.0% | 1 |  |
| ft_ug | BIGINT | 0.0% | 1 |  |
| ft_ftug | BIGINT | 0.0% | 1 |  |
| ftgdnidp | BIGINT | 48.1% | 1 |  |
| pt_ug | BIGINT | 9.1% | 1 |  |
| pt_ftug | BIGINT | 9.1% | 1 |  |
| ptgdnidp | BIGINT | 48.1% | 1 |  |
| docpp | BIGINT | 48.1% | -2 |  |
| docppsp | BIGINT | 48.1% | -2 |  |
| openadmp | DOUBLE | 3.2% | -2.0 |  |
| noncrdt1 | BIGINT | 86.7% | 0 |  |
| noncrdt2 | BIGINT | 86.7% | 0 |  |
| noncrdt3 | BIGINT | 86.7% | 1 |  |
| noncrdt4 | BIGINT | 86.7% | 0 |  |
| noncrdt5 | BIGINT | 86.7% | 0 |  |
| noncrdt6 | BIGINT | 86.7% | 0 |  |
| noncrdt7 | BIGINT | 86.7% | 0 |  |
| noncrdt8 | BIGINT | 86.7% | 0 |  |
| noncrdt9 | BIGINT | 86.7% | 0 |  |
| vet1 | BIGINT | 56.5% | 0 |  |
| vet2 | BIGINT | 56.5% | 1 |  |
| vet3 | BIGINT | 56.5% | 1 |  |
| vet4 | BIGINT | 56.5% | 1 |  |
| vet5 | BIGINT | 56.5% | 1 |  |
| vet9 | BIGINT | 56.5% | 0 |  |
| credits2 | BIGINT | 5.3% | 0 |  |
| credits3 | BIGINT | 5.3% | 1 |  |
| credits4 | BIGINT | 5.3% | 0 |  |
| slo5 | BIGINT | 5.3% | 1 |  |
| slo51 | BIGINT | 5.3% | 1 |  |
| slo52 | BIGINT | 5.3% | 0 |  |
| slo521 | BIGINT | 86.7% | 0 |  |
| slo53 | BIGINT | 5.3% | 0 |  |
| slo6 | BIGINT | 5.3% | 1 |  |
| slo7 | BIGINT | 5.3% | 1 |  |
| sloa | BIGINT | 86.7% | 1 |  |
| slo8 | BIGINT | 5.3% | 1 |  |
| slo81 | BIGINT | 5.3% | 1 |  |
| slo82 | BIGINT | 5.3% | 0 |  |
| slo83 | BIGINT | 5.3% | 1 |  |
| slob | BIGINT | 86.7% | 0 |  |
| slo9 | BIGINT | 5.3% | 0 |  |
| yrscoll | BIGINT | 0.0% | -2 |  |
| stusrv2 | BIGINT | 0.0% | 1 |  |
| stusrv3 | BIGINT | 0.0% | 1 |  |
| stusrv4 | BIGINT | 0.0% | 1 |  |
| stusrv8 | BIGINT | 0.0% | 1 |  |
| stusrv9 | BIGINT | 0.0% | 0 |  |
| libres1 | BIGINT | 64.8% | 1 |  |
| libres2 | BIGINT | 64.8% | 1 |  |
| libres3 | BIGINT | 64.8% | 1 |  |
| libres4 | BIGINT | 64.8% | 1 |  |
| libres5 | BIGINT | 64.8% | 1 |  |
| libres6 | BIGINT | 64.8% | 1 |  |
| libres9 | BIGINT | 64.8% | 0 |  |
| dstnugc | BIGINT | 68.7% | 1 |  |
| dstnugp | BIGINT | 68.7% | 1 |  |
| dstnugn | BIGINT | 68.7% | 0 |  |
| dstngc | BIGINT | 68.7% | 1 |  |
| dstngp | BIGINT | 68.7% | 1 |  |
| dstngn | BIGINT | 68.7% | 0 |  |
| distcrs | BIGINT | 64.8% | 1 |  |
| distpgs | BIGINT | 68.7% | 1 |  |
| dstnced1 | BIGINT | 48.1% | 1 |  |
| dstnced2 | BIGINT | 48.1% | 1 |  |
| dstnced3 | BIGINT | 48.1% | 0 |  |
| distnced | BIGINT | 43.9% | 2 |  |
| disab | BIGINT | 35.8% | 2 |  |
| xdisabpc | VARCHAR | 35.8% | R |  |
| disabpct | VARCHAR | 42.8% | 3.14 |  |
| athassoc | BIGINT | 0.0% | 1 |  |
| assoc1 | BIGINT | 0.0% | 1 |  |
| assoc2 | BIGINT | 0.0% | 0 |  |
| assoc3 | BIGINT | 0.0% | 0 |  |
| assoc4 | BIGINT | 0.0% | 0 |  |
| assoc5 | BIGINT | 0.0% | 0 |  |
| assoc6 | BIGINT | 0.0% | 0 |  |
| sport1 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno1 | BIGINT | 0.0% | 133 |  |
| sport2 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno2 | BIGINT | 0.0% | 133 |  |
| sport3 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno3 | BIGINT | 0.0% | 133 |  |
| sport4 | BIGINT | 0.0% | 1 | Appears in 4 tables, common join key |
| confno4 | BIGINT | 0.0% | 133 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| enrhsst | BIGINT | 96.6% | 1 |  |
| enrhsst1 | BIGINT | 96.6% | 1 |  |
| enrhsst2 | BIGINT | 96.6% | 0 |  |
| tuitpl | BIGINT | 38.5% | 1 |  |
| tuitpl1 | BIGINT | 38.5% | 0 |  |
| tuitpl2 | BIGINT | 38.5% | 0 |  |
| tuitpl3 | BIGINT | 38.5% | 1 |  |
| tuitpl4 | BIGINT | 38.5% | 0 |  |
| prmpgm | BIGINT | 93.2% | 2 |  |
| alloncam | DOUBLE | 23.3% | 2.0 |  |
| tuitvary | BIGINT | 6.6% | 1 |  |
| room | BIGINT | 6.6% | 1 |  |
| xroomcap | VARCHAR | 6.6% | R |  |
| roomcap | VARCHAR | 20.7% | 3620.0 |  |
| board | BIGINT | 6.6% | 1 |  |
| xmealswk | VARCHAR | 6.6% | R |  |
| mealswk | VARCHAR | 23.2% | 21.0 |  |
| xroomamt | VARCHAR | 6.6% | R |  |
| roomamt | VARCHAR | 21.9% | 3790.0 |  |
| xbordamt | VARCHAR | 6.6% | R |  |
| boardamt | VARCHAR | 22.6% | 4202.0 |  |
| xrmbdamt | VARCHAR | 6.6% | A |  |
| rmbrdamt | VARCHAR | 25.5% | 11122.0 |  |
| xappfeeu | VARCHAR | 6.6% | R |  |
| applfeeu | DOUBLE | 24.2% | 30.0 |  |
| xappfeeg | VARCHAR | 6.6% | R |  |
| applfeeg | VARCHAR | 21.3% | 45.0 |  |
| credits1 | BIGINT | 15.2% | 1 |  |
| stusrv1 | BIGINT | 13.3% | 1 |  |
| libfac | BIGINT | 35.2% | 1 |  |
| admcon1 | BIGINT | 43.5% | 1 |  |
| admcon2 | BIGINT | 43.5% | 2 |  |
| admcon3 | BIGINT | 43.5% | 1 |  |
| admcon4 | BIGINT | 43.5% | 2 |  |
| admcon5 | BIGINT | 43.5% | 3 |  |
| admcon6 | BIGINT | 43.5% | 2 |  |
| admcon7 | BIGINT | 43.5% | 1 |  |
| admcon8 | BIGINT | 43.5% | 1 |  |
| admcon9 | BIGINT | 63.9% | 3 |  |
| appdate | BIGINT | 48.8% | 2 |  |
| xapplcnm | VARCHAR | 48.8% | R |  |
| applcnm | VARCHAR | 55.6% | 2401 |  |
| xapplcnw | VARCHAR | 48.8% | R |  |
| applcnw | VARCHAR | 55.6% | 3741 |  |
| xadmssnm | VARCHAR | 48.8% | R |  |
| admssnm | VARCHAR | 55.5% | 2100 |  |
| xadmssnw | VARCHAR | 48.8% | R |  |
| admssnw | VARCHAR | 55.5% | 3421 |  |
| xenrlftm | VARCHAR | 48.8% | R |  |
| enrlftm | VARCHAR | 55.5% | 533 |  |
| xenrlftw | VARCHAR | 48.8% | R |  |
| enrlftw | VARCHAR | 55.5% | 556 |  |
| xenrlptm | VARCHAR | 48.8% | R |  |
| enrlptm | VARCHAR | 55.9% | 9 |  |
| xenrlptw | VARCHAR | 48.8% | R |  |
| enrlptw | VARCHAR | 55.9% | 6 |  |
| satactdt | BIGINT | 48.8% | 2 |  |
| xsatnum | VARCHAR | 48.8% | R |  |
| satnum | VARCHAR | 57.7% | 167 |  |
| xsatpct | VARCHAR | 48.8% | R |  |
| satpct | VARCHAR | 57.7% | 15 |  |
| xactnum | VARCHAR | 48.8% | R |  |
| actnum | VARCHAR | 57.8% | 968 |  |
| xactpct | VARCHAR | 48.8% | R |  |
| actpct | VARCHAR | 57.8% | 88 |  |
| xsatvr25 | VARCHAR | 48.8% | R |  |
| satvr25 | VARCHAR | 58.4% | 370 |  |
| xsatvr75 | VARCHAR | 48.8% | R |  |
| satvr75 | VARCHAR | 58.4% | 450 |  |
| xsatmt25 | VARCHAR | 48.8% | R |  |
| satmt25 | VARCHAR | 58.4% | 350 |  |
| xsatmt75 | VARCHAR | 48.8% | R |  |
| satmt75 | VARCHAR | 58.4% | 450 |  |
| xsatwr25 | VARCHAR | 67.7% | B |  |
| satwr25 | VARCHAR | 67.7% | . |  |
| xsatwr75 | VARCHAR | 67.7% | B |  |
| satwr75 | VARCHAR | 67.7% | . |  |
| xactcm25 | VARCHAR | 48.8% | R |  |
| actcm25 | VARCHAR | 58.6% | 15 |  |
| xactcm75 | VARCHAR | 48.8% | R |  |
| actcm75 | VARCHAR | 58.6% | 19 |  |
| xacten25 | VARCHAR | 48.8% | R |  |
| acten25 | VARCHAR | 58.9% | 14 |  |
| xacten75 | VARCHAR | 48.8% | R |  |
| acten75 | VARCHAR | 58.9% | 19 |  |
| xactmt25 | VARCHAR | 48.8% | R |  |
| actmt25 | VARCHAR | 59.0% | 15 |  |
| xactmt75 | VARCHAR | 48.8% | R |  |
| actmt75 | VARCHAR | 59.0% | 18 |  |
| xactwr25 | VARCHAR | 75.4% | B |  |
| actwr25 | VARCHAR | 75.4% | . |  |
| xactwr75 | VARCHAR | 75.4% | B |  |
| actwr75 | VARCHAR | 75.4% | . |  |
| xenrlm | VARCHAR | 52.6% | R |  |
| enrlm | VARCHAR | 54.8% | 542 |  |
| xenrlw | VARCHAR | 52.6% | R |  |
| enrlw | VARCHAR | 54.8% | 562 |  |
| xenrlt | VARCHAR | 52.6% | R |  |
| enrlt | VARCHAR | 54.8% | 1104 |  |
| xapplcn | VARCHAR | 52.6% | R |  |
| applcn | VARCHAR | 54.8% | 6142 |  |
| xadmssn | VARCHAR | 52.6% | R |  |
| admssn | VARCHAR | 54.8% | 5521 |  |
| xenrlft | VARCHAR | 52.6% | R |  |
| enrlft | VARCHAR | 54.8% | 1089 |  |
| xenrlpt | VARCHAR | 52.6% | R |  |
| enrlpt | VARCHAR | 54.9% | 15 |  |
| slo3 | BIGINT | 57.2% | 1 |  |
| ft_gd | BIGINT | 51.9% | 2 |  |
| pt_gd | BIGINT | 61.0% | 2 |  |
| pctpost | BIGINT | 60.2% | -2 |  |
| level9 | BIGINT | 64.2% | -2 |  |
| level10 | BIGINT | 64.2% | -2 |  |
| level11 | BIGINT | 64.2% | -2 |  |
| xappfeep | VARCHAR | 64.2% | A |  |
| applfeep | VARCHAR | 79.2% | . |  |
| ft_fp | BIGINT | 64.2% | -2 |  |
| pt_fp | BIGINT | 80.9% | -2 |  |
| apfee | BIGINT | 71.9% | 2 |  |
| accrd1 | BIGINT | 79.5% | 1 |  |
| accrd2 | BIGINT | 79.5% | 1 |  |
| regaccrd | BIGINT | 79.5% | 8 |  |
| accrd3 | BIGINT | 79.5% | 1 |  |
| accrd4 | BIGINT | 79.5% | 0 |  |
| saccr | BIGINT | 79.5% | 1 |  |
| slo1 | BIGINT | 84.8% | 1 |  |
| slo2 | BIGINT | 84.8% | 1 |  |
| slo4 | BIGINT | 84.8% | 1 |  |
| insttoyr | BIGINT | 79.5% | -2 |  |
| fopna | BIGINT | 83.3% | 2 |  |
| fopna1 | BIGINT | 83.3% | 0 |  |
| fopna2 | BIGINT | 83.3% | 0 |  |
| ftstu | BIGINT | 87.1% | 1 |  |
| ptstu | BIGINT | 96.2% | 1 |  |
| rotc | BIGINT | 94.7% | 2 |  |
| rotc1 | BIGINT | 94.7% | -2 |  |
| rotc2 | BIGINT | 94.7% | -2 |  |
| rotc3 | BIGINT | 94.7% | -2 |  |

## ic_ay

Rows: 90,151

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xtuit1 | VARCHAR | 0.0% | R |  |
| tuition_in_district | DOUBLE | 9.9% | 8610.0 |  |
| xfee1 | VARCHAR | 0.0% | R |  |
| fee1 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg1 | VARCHAR | 0.0% | R |  |
| hrchg1 | DOUBLE | 20.9% | 287.0 |  |
| xtuit2 | VARCHAR | 0.0% | R |  |
| tuition_in_state | DOUBLE | 9.9% | 8610.0 |  |
| xfee2 | VARCHAR | 0.0% | R |  |
| fee2 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg2 | VARCHAR | 0.0% | R |  |
| hrchg2 | DOUBLE | 20.9% | 287.0 |  |
| xtuit3 | VARCHAR | 0.0% | R |  |
| tuition_out_state | DOUBLE | 9.9% | 17220.0 |  |
| xfee3 | VARCHAR | 0.0% | R |  |
| fee3 | DOUBLE | 10.1% | 1414.0 |  |
| xhrchg3 | VARCHAR | 0.0% | R |  |
| hrchg3 | DOUBLE | 20.6% | 574.0 |  |
| xtuit5 | VARCHAR | 0.0% | R |  |
| tuition5 | VARCHAR | 17.6% | 10128.0 |  |
| xfee5 | VARCHAR | 0.0% | R |  |
| fee5 | VARCHAR | 17.7% | 1414.0 |  |
| xhrchg5 | VARCHAR | 0.0% | R |  |
| hrchg5 | VARCHAR | 18.0% | 422.0 |  |
| xtuit6 | VARCHAR | 0.0% | R |  |
| tuition6 | VARCHAR | 17.6% | 10128.0 |  |
| xfee6 | VARCHAR | 0.0% | R |  |
| fee6 | VARCHAR | 17.7% | 1414.0 |  |
| xhrchg6 | VARCHAR | 0.0% | R |  |
| hrchg6 | VARCHAR | 18.0% | 422.0 |  |
| xtuit7 | VARCHAR | 0.0% | R |  |
| tuition7 | VARCHAR | 17.6% | 20160.0 |  |
| xfee7 | VARCHAR | 0.0% | R |  |
| fee7 | VARCHAR | 17.7% | 1414.0 |  |
| xhrchg7 | VARCHAR | 0.0% | R |  |
| hrchg7 | VARCHAR | 17.9% | 840.0 |  |
| xispro1 | VARCHAR | 0.0% | A |  |
| isprof1 | VARCHAR | 27.3% | 0.0 |  |
| xispfe1 | VARCHAR | 0.0% | A |  |
| ispfee1 | VARCHAR | 27.3% | 0.0 |  |
| xospro1 | VARCHAR | 0.0% | A |  |
| osprof1 | VARCHAR | 27.3% | 0.0 |  |
| xospfe1 | VARCHAR | 0.0% | A |  |
| ospfee1 | VARCHAR | 27.3% | 0.0 |  |
| xispro2 | VARCHAR | 0.0% | A |  |
| isprof2 | VARCHAR | 27.1% | 31902.0 |  |
| xispfe2 | VARCHAR | 0.0% | A |  |
| ispfee2 | VARCHAR | 27.1% | 0.0 |  |
| xospro2 | VARCHAR | 0.0% | A |  |
| osprof2 | VARCHAR | 27.1% | 74362.0 |  |
| xospfe2 | VARCHAR | 0.0% | A |  |
| ospfee2 | VARCHAR | 27.1% | 0.0 |  |
| xispro3 | VARCHAR | 0.0% | A |  |
| isprof3 | VARCHAR | 26.7% | 32134.0 |  |
| xispfe3 | VARCHAR | 0.0% | A |  |
| ispfee3 | VARCHAR | 26.7% | 0.0 |  |
| xospro3 | VARCHAR | 0.0% | A |  |
| osprof3 | VARCHAR | 26.7% | 62714.0 |  |
| xospfe3 | VARCHAR | 0.0% | A |  |
| ospfee3 | VARCHAR | 26.7% | 0.0 |  |
| xispro4 | VARCHAR | 0.0% | A |  |
| isprof4 | VARCHAR | 27.3% | 29841.0 |  |
| xispfe4 | VARCHAR | 0.0% | A |  |
| ispfee4 | VARCHAR | 27.3% | 0.0 |  |
| xospro4 | VARCHAR | 0.0% | A |  |
| osprof4 | VARCHAR | 27.3% | 54012.0 |  |
| xospfe4 | VARCHAR | 0.0% | A |  |
| ospfee4 | VARCHAR | 27.3% | 0.0 |  |
| xispro5 | VARCHAR | 0.0% | A |  |
| isprof5 | VARCHAR | 27.3% | 65500.0 |  |
| xispfe5 | VARCHAR | 0.0% | A |  |
| ispfee5 | VARCHAR | 27.3% | 1133.0 |  |
| xospro5 | VARCHAR | 0.0% | A |  |
| osprof5 | VARCHAR | 27.3% | 65500.0 |  |
| xospfe5 | VARCHAR | 0.0% | A |  |
| ospfee5 | VARCHAR | 27.3% | 1133.0 |  |
| xispro6 | VARCHAR | 0.0% | A |  |
| isprof6 | VARCHAR | 26.9% | 10692.0 |  |
| xispfe6 | VARCHAR | 0.0% | A |  |
| ispfee6 | VARCHAR | 26.9% | 13832.0 |  |
| xospro6 | VARCHAR | 0.0% | A |  |
| osprof6 | VARCHAR | 26.9% | 32076.0 |  |
| xospfe6 | VARCHAR | 0.0% | A |  |
| ospfee6 | VARCHAR | 26.9% | 13832.0 |  |
| xispro7 | VARCHAR | 0.0% | A |  |
| isprof7 | VARCHAR | 27.4% | 43791.0 |  |
| xispfe7 | VARCHAR | 0.0% | A |  |
| ispfee7 | VARCHAR | 27.4% | 1319.0 |  |
| xospro7 | VARCHAR | 0.0% | A |  |
| osprof7 | VARCHAR | 27.4% | 43791.0 |  |
| xospfe7 | VARCHAR | 0.0% | A |  |
| ospfee7 | VARCHAR | 27.4% | 1319.0 |  |
| xispro8 | VARCHAR | 0.0% | A |  |
| isprof8 | VARCHAR | 27.2% | 10692.0 |  |
| xispfe8 | VARCHAR | 0.0% | A |  |
| ispfee8 | VARCHAR | 27.2% | 18916.0 |  |
| xospro8 | VARCHAR | 0.0% | A |  |
| osprof8 | VARCHAR | 27.2% | 32076.0 |  |
| xospfe8 | VARCHAR | 0.0% | A |  |
| ospfee8 | VARCHAR | 27.2% | 18916.0 |  |
| xispro9 | VARCHAR | 0.0% | A |  |
| isprof9 | VARCHAR | 26.2% | 24080.0 |  |
| xispfe9 | VARCHAR | 0.0% | A |  |
| ispfee9 | VARCHAR | 26.3% | 300.0 |  |
| xospro9 | VARCHAR | 0.0% | A |  |
| osprof9 | VARCHAR | 26.2% | 45570.0 |  |
| xospfe9 | VARCHAR | 0.0% | A |  |
| ospfee9 | VARCHAR | 26.3% | 300.0 |  |
| xchg1at0 | VARCHAR | 48.6% | R |  |
| chg1at0 | DOUBLE | 54.9% | 8610.0 |  |
| xchg1af0 | VARCHAR | 48.6% | R |  |
| chg1af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg1ay0 | VARCHAR | 48.6% | R |  |
| chg1ay0 | DOUBLE | 54.9% | 10024.0 |  |
| xchg1at1 | VARCHAR | 48.6% | R |  |
| chg1at1 | DOUBLE | 54.7% | 8610.0 |  |
| xchg1af1 | VARCHAR | 48.6% | R |  |
| chg1af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg1ay1 | VARCHAR | 0.0% | R |  |
| chg1ay1 | DOUBLE | 15.1% | 10024.0 |  |
| xchg1at2 | VARCHAR | 48.6% | R |  |
| chg1at2 | DOUBLE | 54.5% | 8610.0 |  |
| xchg1af2 | VARCHAR | 48.6% | R |  |
| chg1af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg1ay2 | VARCHAR | 0.0% | R |  |
| chg1ay2 | DOUBLE | 14.4% | 10024.0 |  |
| xchg1at3 | VARCHAR | 48.6% | R |  |
| chg1at3 | DOUBLE | 54.4% | 8610.0 |  |
| xchg1af3 | VARCHAR | 48.6% | R |  |
| chg1af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg1ay3 | VARCHAR | 0.0% | R |  |
| chg1ay3 | DOUBLE | 13.8% | 10024.0 |  |
| chg1tgtd | VARCHAR | 52.6% | 0.0 |  |
| chg1fgtd | VARCHAR | 52.8% | 0.0 |  |
| xchg2at0 | VARCHAR | 48.6% | R |  |
| chg2at0 | DOUBLE | 54.9% | 8610.0 |  |
| xchg2af0 | VARCHAR | 48.6% | R |  |
| chg2af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg2ay0 | VARCHAR | 48.6% | R |  |
| chg2ay0 | DOUBLE | 54.9% | 10024.0 |  |
| xchg2at1 | VARCHAR | 48.6% | R |  |
| chg2at1 | DOUBLE | 54.7% | 8610.0 |  |
| xchg2af1 | VARCHAR | 48.6% | R |  |
| chg2af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg2ay1 | VARCHAR | 0.0% | R |  |
| chg2ay1 | DOUBLE | 14.7% | 10024.0 |  |
| xchg2at2 | VARCHAR | 48.6% | R |  |
| chg2at2 | DOUBLE | 54.5% | 8610.0 |  |
| xchg2af2 | VARCHAR | 48.6% | R |  |
| chg2af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg2ay2 | VARCHAR | 0.0% | R |  |
| chg2ay2 | DOUBLE | 14.1% | 10024.0 |  |
| xchg2at3 | VARCHAR | 48.6% | R |  |
| chg2at3 | DOUBLE | 54.4% | 8610.0 |  |
| xchg2af3 | VARCHAR | 48.6% | R |  |
| chg2af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg2ay3 | VARCHAR | 0.0% | R |  |
| chg2ay3 | DOUBLE | 13.8% | 10024.0 |  |
| chg2tgtd | VARCHAR | 52.6% | 0.0 |  |
| chg2fgtd | VARCHAR | 52.8% | 0.0 |  |
| xchg3at0 | VARCHAR | 48.6% | R |  |
| chg3at0 | DOUBLE | 54.9% | 17220.0 |  |
| xchg3af0 | VARCHAR | 48.6% | R |  |
| chg3af0 | DOUBLE | 54.9% | 1414.0 |  |
| xchg3ay0 | VARCHAR | 48.6% | R |  |
| chg3ay0 | DOUBLE | 54.9% | 18634.0 |  |
| xchg3at1 | VARCHAR | 48.6% | R |  |
| chg3at1 | DOUBLE | 54.7% | 17220.0 |  |
| xchg3af1 | VARCHAR | 48.6% | R |  |
| chg3af1 | DOUBLE | 54.7% | 1414.0 |  |
| xchg3ay1 | VARCHAR | 0.0% | R |  |
| chg3ay1 | DOUBLE | 14.8% | 18634.0 |  |
| xchg3at2 | VARCHAR | 48.6% | R |  |
| chg3at2 | DOUBLE | 54.5% | 17220.0 |  |
| xchg3af2 | VARCHAR | 48.6% | R |  |
| chg3af2 | DOUBLE | 54.5% | 1414.0 |  |
| xchg3ay2 | VARCHAR | 0.0% | R |  |
| chg3ay2 | DOUBLE | 14.1% | 18634.0 |  |
| xchg3at3 | VARCHAR | 48.6% | R |  |
| chg3at3 | DOUBLE | 54.4% | 17220.0 |  |
| xchg3af3 | VARCHAR | 48.6% | R |  |
| chg3af3 | DOUBLE | 54.4% | 1414.0 |  |
| xchg3ay3 | VARCHAR | 0.0% | R |  |
| chg3ay3 | DOUBLE | 13.8% | 18634.0 |  |
| chg3tgtd | VARCHAR | 52.7% | 0.0 |  |
| chg3fgtd | VARCHAR | 52.8% | 0.0 |  |
| xchg4ay0 | VARCHAR | 48.6% | R |  |
| chg4ay0 | DOUBLE | 56.4% | 1600.0 |  |
| xchg4ay1 | VARCHAR | 0.0% | R |  |
| chg4ay1 | DOUBLE | 16.7% | 1600.0 |  |
| xchg4ay2 | VARCHAR | 0.0% | R |  |
| chg4ay2 | DOUBLE | 16.1% | 1600.0 |  |
| xchg4ay3 | VARCHAR | 0.0% | R |  |
| chg4ay3 | DOUBLE | 16.0% | 2192.0 |  |
| xchg5ay0 | VARCHAR | 48.6% | R |  |
| chg5ay0 | VARCHAR | 50.7% | 9240.0 |  |
| xchg5ay1 | VARCHAR | 0.0% | R |  |
| chg5ay1 | VARCHAR | 16.7% | 9520.0 |  |
| xchg5ay2 | VARCHAR | 0.0% | R |  |
| chg5ay2 | VARCHAR | 16.6% | 9520.0 |  |
| xchg5ay3 | VARCHAR | 0.0% | R |  |
| chg5ay3 | VARCHAR | 16.7% | 11402.0 |  |
| xchg6ay0 | VARCHAR | 48.6% | R |  |
| chg6ay0 | VARCHAR | 50.7% | 3090.0 |  |
| xchg6ay1 | VARCHAR | 0.0% | R |  |
| chg6ay1 | VARCHAR | 16.9% | 3090.0 |  |
| xchg6ay2 | VARCHAR | 0.0% | R |  |
| chg6ay2 | VARCHAR | 16.8% | 3090.0 |  |
| xchg6ay3 | VARCHAR | 0.0% | R |  |
| chg6ay3 | VARCHAR | 16.9% | 3864.0 |  |
| xchg7ay0 | VARCHAR | 48.6% | R |  |
| chg7ay0 | DOUBLE | 56.5% | 9240.0 |  |
| xchg7ay1 | VARCHAR | 0.0% | R |  |
| chg7ay1 | DOUBLE | 20.9% | 9520.0 |  |
| xchg7ay2 | VARCHAR | 0.0% | R |  |
| chg7ay2 | DOUBLE | 20.0% | 9520.0 |  |
| xchg7ay3 | VARCHAR | 0.0% | R |  |
| chg7ay3 | DOUBLE | 19.3% | 11402.0 |  |
| xchg8ay0 | VARCHAR | 48.6% | R |  |
| chg8ay0 | DOUBLE | 56.5% | 3090.0 |  |
| xchg8ay1 | VARCHAR | 0.0% | R |  |
| chg8ay1 | DOUBLE | 21.1% | 3090.0 |  |
| xchg8ay2 | VARCHAR | 0.0% | R |  |
| chg8ay2 | DOUBLE | 20.2% | 3090.0 |  |
| xchg8ay3 | VARCHAR | 0.0% | R |  |
| chg8ay3 | DOUBLE | 19.4% | 3864.0 |  |
| xchg9ay0 | VARCHAR | 48.6% | R |  |
| chg9ay0 | DOUBLE | 56.4% | 3440.0 |  |
| xchg9ay1 | VARCHAR | 0.0% | R |  |
| chg9ay1 | DOUBLE | 21.1% | 3440.0 |  |
| xchg9ay2 | VARCHAR | 0.0% | R |  |
| chg9ay2 | DOUBLE | 19.9% | 3440.0 |  |
| xchg9ay3 | VARCHAR | 0.0% | R |  |
| chg9ay3 | DOUBLE | 19.1% | 4271.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xcmpfee1 | VARCHAR | 51.4% | A |  |
| cmpfee1 | VARCHAR | 74.5% | . |  |
| xcmpfee2 | VARCHAR | 51.4% | A |  |
| cmpfee2 | VARCHAR | 74.5% | . |  |
| xcmpfee3 | VARCHAR | 51.4% | A |  |
| cmpfee3 | VARCHAR | 74.5% | . |  |
| xcmp1ay0 | VARCHAR | 100.0% |  |  |
| cmp1ay0 | VARCHAR | 100.0% |  |  |
| xcmp1ay1 | VARCHAR | 74.6% | A |  |
| cmp1ay1 | VARCHAR | 74.6% | . |  |
| xcmp1ay2 | VARCHAR | 74.6% | A |  |
| cmp1ay2 | VARCHAR | 74.6% | . |  |
| xcmp1ay3 | VARCHAR | 74.6% | A |  |
| cmp1ay3 | VARCHAR | 74.6% | . |  |
| cmp1gtd | VARCHAR | 100.0% |  |  |
| xcmp2ay0 | VARCHAR | 100.0% |  |  |
| cmp2ay0 | VARCHAR | 100.0% |  |  |
| xcmp2ay1 | VARCHAR | 74.6% | A |  |
| cmp2ay1 | VARCHAR | 74.6% | . |  |
| xcmp2ay2 | VARCHAR | 74.6% | A |  |
| cmp2ay2 | VARCHAR | 74.6% | . |  |
| xcmp2ay3 | VARCHAR | 74.6% | A |  |
| cmp2ay3 | VARCHAR | 74.6% | . |  |
| cmp2gtd | VARCHAR | 100.0% |  |  |
| xcmp3ay0 | VARCHAR | 100.0% |  |  |
| cmp3ay0 | VARCHAR | 100.0% |  |  |
| xcmp3ay1 | VARCHAR | 74.6% | A |  |
| cmp3ay1 | VARCHAR | 74.6% | . |  |
| xcmp3ay2 | VARCHAR | 74.6% | A |  |
| cmp3ay2 | VARCHAR | 74.6% | . |  |
| xcmp3ay3 | VARCHAR | 74.6% | A |  |
| cmp3ay3 | VARCHAR | 74.6% | . |  |
| cmp3gtd | DOUBLE | 100.0% |  |  |
| xispro10 | VARCHAR | 51.4% | A |  |
| isprof10 | VARCHAR | 73.6% | . |  |
| xispfe10 | VARCHAR | 51.4% | A |  |
| ispfee10 | VARCHAR | 73.6% | . |  |
| xospro10 | VARCHAR | 51.4% | A |  |
| osprof10 | VARCHAR | 73.6% | . |  |
| xospfe10 | VARCHAR | 51.4% | A |  |
| ospfee10 | VARCHAR | 73.6% | . |  |
| xispro11 | VARCHAR | 51.4% | A |  |
| isprof11 | VARCHAR | 74.4% | . |  |
| xispfe11 | VARCHAR | 51.4% | A |  |
| ispfee11 | VARCHAR | 74.4% | . |  |
| xospro11 | VARCHAR | 51.4% | A |  |
| osprof11 | VARCHAR | 74.4% | . |  |
| xospfe11 | VARCHAR | 51.4% | A |  |
| ospfee11 | VARCHAR | 74.4% | . |  |
| cindon | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 86.9% | 13590.0 | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 86.9% | 7520.0 | Appears in 3 tables, common join key |
| cinson | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 86.9% | 13590.0 | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 86.9% | 7520.0 | Appears in 3 tables, common join key |
| cotson | VARCHAR | 87.6% | . | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 86.9% | 17490.0 | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 86.9% | 11420.0 | Appears in 3 tables, common join key |

## ic_py

Rows: 61,317

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 101277 | Primary institution ID, joins across all IPEDS tables |
| prgmofr | DOUBLE | 0.0% | 3.0 |  |
| cipcode1 | VARCHAR | 0.0% | 12.0401 |  |
| xciptui1 | VARCHAR | 28.1% | A |  |
| ciptuit1 | VARCHAR | 31.5% | 14990.0 |  |
| xcipsup1 | VARCHAR | 28.1% | A |  |
| cipsupp1 | VARCHAR | 31.5% | 1350.0 |  |
| xciplgt1 | DOUBLE | 24.7% | 1500.0 |  |
| ciplgth1 | DOUBLE | 15.1% | 1500.0 |  |
| prgmsr1 | VARCHAR | 28.1% | 1 |  |
| xmthcmp1 | DOUBLE | 31.8% | 12.0 |  |
| mthcmp1 | VARCHAR | 28.1% | 12 |  |
| xwkcmp1 | DOUBLE | 51.9% | 47.0 |  |
| wkcmp1 | VARCHAR | 47.4% | 47.0 |  |
| xlnayhr1 | DOUBLE | 51.9% | 900.0 |  |
| lnayhr1 | VARCHAR | 47.4% | 900.0 |  |
| xlnaywk1 | DOUBLE | 51.9% | 28.0 |  |
| lnaywk1 | VARCHAR | 47.4% | 28.0 |  |
| xchg1py0 | DOUBLE | 45.7% | 11040.0 |  |
| chg1py0 | VARCHAR | 39.4% | 12000.0 |  |
| xchg1py1 | DOUBLE | 27.9% | 12000.0 |  |
| chg1py1 | VARCHAR | 9.3% | 12150.0 |  |
| xchg1py2 | DOUBLE | 26.7% | 12150.0 |  |
| chg1py2 | VARCHAR | 8.8% | 15150.0 |  |
| xchg1py3 | DOUBLE | 26.2% | 15150.0 |  |
| chg1py3 | VARCHAR | 8.3% | 15150.0 |  |
| xchg4py0 | DOUBLE | 48.3% | 2503.0 |  |
| chg4py0 | VARCHAR | 39.6% | 2503.0 |  |
| xchg4py1 | VARCHAR | 0.0% | R |  |
| chg4py1 | VARCHAR | 10.5% | 2649.0 |  |
| xchg4py2 | DOUBLE | 29.4% | 2649.0 |  |
| chg4py2 | VARCHAR | 10.1% | 3040.0 |  |
| xchg4py3 | DOUBLE | 28.8% | 3040.0 |  |
| chg4py3 | VARCHAR | 9.3% | 3258.0 |  |
| xchg5py0 | VARCHAR | 39.2% | A |  |
| chg5py0 | VARCHAR | 42.7% | 10811.0 |  |
| xchg5py1 | VARCHAR | 0.0% | A |  |
| chg5py1 | VARCHAR | 24.3% | 11248.0 |  |
| xchg5py2 | VARCHAR | 0.0% | A |  |
| chg5py2 | VARCHAR | 24.2% | 11695.0 |  |
| xchg5py3 | VARCHAR | 0.0% | A |  |
| chg5py3 | VARCHAR | 24.4% | 11695.0 |  |
| xchg6py0 | VARCHAR | 39.2% | A |  |
| chg6py0 | VARCHAR | 42.7% | 2375.0 |  |
| xchg6py1 | VARCHAR | 0.0% | A |  |
| chg6py1 | VARCHAR | 24.3% | 2375.0 |  |
| xchg6py2 | VARCHAR | 0.0% | A |  |
| chg6py2 | VARCHAR | 24.2% | 2375.0 |  |
| xchg6py3 | VARCHAR | 0.0% | A |  |
| chg6py3 | VARCHAR | 24.5% | 2375.0 |  |
| xchg7py0 | DOUBLE | 45.8% | 11268.0 |  |
| chg7py0 | VARCHAR | 39.4% | 11268.0 |  |
| xchg7py1 | DOUBLE | 28.6% | 11268.0 |  |
| chg7py1 | VARCHAR | 14.1% | 11268.0 |  |
| xchg7py2 | DOUBLE | 27.0% | 11268.0 |  |
| chg7py2 | VARCHAR | 13.5% | 14171.0 |  |
| xchg7py3 | DOUBLE | 26.3% | 14171.0 |  |
| chg7py3 | VARCHAR | 12.1% | 18483.0 |  |
| xchg8py0 | DOUBLE | 45.9% | 7978.0 |  |
| chg8py0 | VARCHAR | 39.4% | 7978.0 |  |
| xchg8py1 | DOUBLE | 28.7% | 7978.0 |  |
| chg8py1 | VARCHAR | 14.2% | 7978.0 |  |
| xchg8py2 | DOUBLE | 27.0% | 7978.0 |  |
| chg8py2 | VARCHAR | 13.6% | 6239.0 |  |
| xchg8py3 | DOUBLE | 26.3% | 6239.0 |  |
| chg8py3 | VARCHAR | 12.2% | 10963.0 |  |
| xchg9py0 | DOUBLE | 45.9% | 7508.0 |  |
| chg9py0 | VARCHAR | 39.4% | 7508.0 |  |
| xchg9py1 | DOUBLE | 28.6% | 7508.0 |  |
| chg9py1 | VARCHAR | 14.2% | 7508.0 |  |
| xchg9py2 | DOUBLE | 27.0% | 7508.0 |  |
| chg9py2 | VARCHAR | 13.5% | 8531.0 |  |
| xchg9py3 | DOUBLE | 26.3% | 8531.0 |  |
| chg9py3 | VARCHAR | 12.2% | 8531.0 |  |
| cipcode2 | VARCHAR | 0.0% | 12.0409 |  |
| xciptui2 | VARCHAR | 0.0% | R |  |
| ciptuit2 | VARCHAR | 11.0% | 10150.0 |  |
| xcipsup2 | VARCHAR | 0.0% | R |  |
| cipsupp2 | VARCHAR | 11.8% | 1735.0 |  |
| xciplgt2 | VARCHAR | 0.0% | R |  |
| ciplgth2 | DOUBLE | 11.2% | 1000.0 |  |
| prgmsr2 | VARCHAR | 28.1% | 1 |  |
| xmthcmp2 | DOUBLE | 45.7% | 12.0 |  |
| mthcmp2 | DOUBLE | 28.7% | 10.0 |  |
| cipcode3 | VARCHAR | 0.0% | 12.0413 |  |
| xciptui3 | VARCHAR | 0.0% | R |  |
| ciptuit3 | VARCHAR | 13.7% | 2150.0 |  |
| xcipsup3 | VARCHAR | 0.0% | R |  |
| cipsupp3 | VARCHAR | 14.5% | 755.0 |  |
| xciplgt3 | VARCHAR | 0.0% | R |  |
| ciplgth3 | DOUBLE | 14.9% | 650.0 |  |
| prgmsr3 | VARCHAR | 28.1% | 1 |  |
| xmthcmp3 | VARCHAR | 28.1% | R |  |
| mthcmp3 | DOUBLE | 29.3% | 5.0 |  |
| cipcode4 | VARCHAR | 0.0% | -2.0 |  |
| xciptui4 | VARCHAR | 0.0% | A |  |
| ciptuit4 | VARCHAR | 16.5% | 4736.0 |  |
| xcipsup4 | VARCHAR | 0.0% | A |  |
| cipsupp4 | VARCHAR | 17.1% | 1809.0 |  |
| xciplgt4 | VARCHAR | 0.0% | A |  |
| ciplgth4 | DOUBLE | 18.8% | 1260.0 |  |
| prgmsr4 | VARCHAR | 28.1% | -2 |  |
| xmthcmp4 | VARCHAR | 28.1% | A |  |
| mthcmp4 | DOUBLE | 29.8% | 10.0 |  |
| cipcode5 | VARCHAR | 0.0% | -2.0 |  |
| xciptui5 | VARCHAR | 0.0% | A |  |
| ciptuit5 | VARCHAR | 18.7% | 4736.0 |  |
| xcipsup5 | VARCHAR | 0.0% | A |  |
| cipsupp5 | VARCHAR | 19.2% | 4550.0 |  |
| xciplgt5 | VARCHAR | 0.0% | A |  |
| ciplgth5 | DOUBLE | 22.0% | 1340.0 |  |
| prgmsr5 | VARCHAR | 28.1% | -2 |  |
| xmthcmp5 | VARCHAR | 28.1% | A |  |
| mthcmp5 | DOUBLE | 30.3% | 10.0 |  |
| cipcode6 | VARCHAR | 0.0% | -2.0 |  |
| xciptui6 | VARCHAR | 0.0% | A |  |
| ciptuit6 | VARCHAR | 20.2% | 4736.0 |  |
| xcipsup6 | VARCHAR | 0.0% | A |  |
| cipsupp6 | VARCHAR | 20.6% | 3850.0 |  |
| xciplgt6 | VARCHAR | 0.0% | A |  |
| ciplgth6 | DOUBLE | 31.1% | 1080.0 |  |
| prgmsr6 | VARCHAR | 28.1% | -2 |  |
| xmthcmp6 | VARCHAR | 28.1% | A |  |
| mthcmp6 | DOUBLE | 98.9% | 10.0 |  |
| year | BIGINT | 0.0% | 2023 | Appears in 26 tables, common join key |
| xcmp1py0 | VARCHAR | 83.0% | . |  |
| cmp1py0 | VARCHAR | 83.0% | A |  |
| xcmp1py1 | VARCHAR | 68.5% | . |  |
| cmp1py1 | VARCHAR | 68.5% | A |  |
| xcmp1py2 | VARCHAR | 68.5% | . |  |
| cmp1py2 | VARCHAR | 68.5% | A |  |
| xcmp1py3 | VARCHAR | 68.5% | . |  |
| cmp1py3 | DOUBLE | 71.9% | -2.0 |  |
| pg300 | BIGINT | 78.8% | 1 |  |

## om

Rows: 415,178

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| omchrt | BIGINT | 0.0% | 10 |  |
| xomrchrt | VARCHAR | 6.4% | R |  |
| omrchrt | BIGINT | 6.4% | 1658 |  |
| xomexcls | VARCHAR | 6.4% | R |  |
| omexcls | BIGINT | 6.4% | 6 |  |
| xomachrt | VARCHAR | 6.4% | R |  |
| omachrt | BIGINT | 6.4% | 1652 |  |
| xomcert4 | VARCHAR | 6.4% | R |  |
| omcert4 | BIGINT | 6.4% | 0 |  |
| xomassc4 | VARCHAR | 6.4% | R |  |
| omassc4 | BIGINT | 6.4% | 0 |  |
| xombach4 | VARCHAR | 6.4% | R |  |
| ombach4 | DOUBLE | 39.0% | 197.0 |  |
| xomawdn4 | VARCHAR | 6.4% | R |  |
| omawdn4 | BIGINT | 6.4% | 197 |  |
| xomawdp4 | VARCHAR | 6.4% | R |  |
| omawdp4 | DOUBLE | 6.5% | 12.0 |  |
| xomcert6 | VARCHAR | 6.4% | R |  |
| omcert6 | BIGINT | 6.4% | 0 |  |
| xomassc6 | VARCHAR | 6.4% | R |  |
| omassc6 | BIGINT | 6.4% | 0 |  |
| xombach6 | VARCHAR | 6.4% | R |  |
| ombach6 | DOUBLE | 39.0% | 426.0 |  |
| xomawdn6 | VARCHAR | 0.0% | R |  |
| omawdn6 | BIGINT | 0.0% | 426 |  |
| xomawdp6 | VARCHAR | 0.0% | R |  |
| omawdp6 | DOUBLE | 0.0% | 26.0 |  |
| xomcert8 | VARCHAR | 6.4% | R |  |
| omcert8 | BIGINT | 6.4% | 0 |  |
| xomassc8 | VARCHAR | 6.4% | R |  |
| omassc8 | BIGINT | 6.4% | 0 |  |
| xombach8 | VARCHAR | 6.4% | R |  |
| ombach8 | DOUBLE | 39.0% | 475.0 |  |
| xomawdn8 | VARCHAR | 0.0% | R |  |
| omawdn8 | BIGINT | 0.0% | 475 |  |
| xomenryi | VARCHAR | 0.0% | R |  |
| omenryi | BIGINT | 0.0% | 2 |  |
| xomenrai | VARCHAR | 0.0% | R |  |
| omenrai | BIGINT | 0.0% | 596 |  |
| xomenrun | VARCHAR | 0.0% | R |  |
| omenrun | BIGINT | 0.0% | 579 |  |
| xomnoawd | VARCHAR | 0.0% | R |  |
| omnoawd | BIGINT | 0.0% | 1177 |  |
| xomawdp8 | VARCHAR | 0.0% | R |  |
| omawdp8 | DOUBLE | 0.0% | 29.0 |  |
| xomenrtp | VARCHAR | 0.0% | R |  |
| omenrtp | DOUBLE | 0.0% | 36.0 |  |
| xomenryp | VARCHAR | 0.0% | R |  |
| omenryp | DOUBLE | 0.0% | 0.0 |  |
| xomenrap | VARCHAR | 0.0% | R |  |
| omenrap | DOUBLE | 0.0% | 36.0 |  |
| xomenrup | VARCHAR | 6.4% | R |  |
| omenrup | DOUBLE | 6.5% | 35.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xomrcht6 | VARCHAR | 93.6% | R |  |
| omrcht6 | BIGINT | 93.6% | 1044 |  |
| xomexcl6 | VARCHAR | 93.6% | R |  |
| omexcl6 | BIGINT | 93.6% | 0 |  |
| xomacht6 | VARCHAR | 93.6% | R |  |
| omacht6 | BIGINT | 93.6% | 1044 |  |
| xomexcl8 | VARCHAR | 93.6% | R |  |
| omexcl8 | BIGINT | 93.6% | 0 |  |
| xomacht8 | VARCHAR | 93.6% | R |  |
| omacht8 | BIGINT | 93.6% | 1044 |  |
| xomrcht8 | VARCHAR | 96.7% | R |  |
| omrcht8 | BIGINT | 96.7% | 882 |  |
| omflag | BIGINT | 96.7% | 0 |  |

## sal_is

Rows: 209,792

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| arank | BIGINT | 0.0% | 1 |  |
| xsainstt | VARCHAR | 32.6% | R |  |
| sainstt | BIGINT | 32.6% | 47 |  |
| xsainstm | VARCHAR | 32.6% | R |  |
| sainstm | BIGINT | 32.6% | 37 |  |
| xsainstw | VARCHAR | 32.6% | R |  |
| sainstw | BIGINT | 32.6% | 10 |  |
| xsa_9mct | VARCHAR | 32.6% | R |  |
| sa_9mct | DOUBLE | 32.6% | 8.0 |  |
| xsa_9mcm | VARCHAR | 32.6% | R |  |
| sa_9mcm | DOUBLE | 32.6% | 7.0 |  |
| xsa_9mcw | VARCHAR | 32.6% | R |  |
| sa_9mcw | DOUBLE | 32.6% | 1.0 |  |
| xsatotlt | VARCHAR | 0.0% | R |  |
| satotlt | BIGINT | 0.0% | 39 |  |
| xsatotlm | VARCHAR | 0.0% | R |  |
| satotlm | BIGINT | 0.0% | 30 |  |
| xsatotlw | VARCHAR | 0.0% | R |  |
| satotlw | BIGINT | 0.0% | 9 |  |
| xsa09mct | VARCHAR | 0.0% | R |  |
| sa09mct | DOUBLE | 0.0% | 37.0 |  |
| xsa09mcm | VARCHAR | 0.0% | R |  |
| sa09mcm | DOUBLE | 0.0% | 29.0 |  |
| xsa09mcw | VARCHAR | 0.0% | R |  |
| sa09mcw | DOUBLE | 0.0% | 8.0 |  |
| xsa10mct | VARCHAR | 0.0% | R |  |
| sa10mct | DOUBLE | 0.0% | 0.0 |  |
| xsa10mcm | VARCHAR | 0.0% | Z |  |
| sa10mcm | DOUBLE | 0.0% | 0.0 |  |
| xsa10mcw | VARCHAR | 0.0% | Z |  |
| sa10mcw | DOUBLE | 0.0% | 0.0 |  |
| xsa11mct | VARCHAR | 0.0% | R |  |
| sa11mct | DOUBLE | 0.0% | 0.0 |  |
| xsa11mcm | VARCHAR | 0.0% | Z |  |
| sa11mcm | DOUBLE | 0.0% | 0.0 |  |
| xsa11mcw | VARCHAR | 0.0% | Z |  |
| sa11mcw | DOUBLE | 0.0% | 0.0 |  |
| xsa12mct | VARCHAR | 0.0% | R |  |
| sa12mct | DOUBLE | 0.0% | 2.0 |  |
| xsa12mcm | VARCHAR | 0.0% | R |  |
| sa12mcm | DOUBLE | 0.0% | 1.0 |  |
| xsa12mcw | VARCHAR | 0.0% | R |  |
| sa12mcw | DOUBLE | 0.0% | 1.0 |  |
| xsaoutlt | VARCHAR | 0.0% | R |  |
| saoutlt | BIGINT | 0.0% | 4239265 |  |
| xsaoutlm | VARCHAR | 0.0% | R |  |
| saoutlm | BIGINT | 0.0% | 3300618 |  |
| xsaoutlw | VARCHAR | 0.0% | R |  |
| saoutlw | BIGINT | 0.0% | 938647 |  |
| xsa09mot | VARCHAR | 32.6% | R |  |
| sa09mot | DOUBLE | 32.6% | 3949476.0 |  |
| xsa09mom | VARCHAR | 32.6% | R |  |
| sa09mom | DOUBLE | 32.6% | 3145514.0 |  |
| xsa09mow | VARCHAR | 32.6% | R |  |
| sa09mow | DOUBLE | 32.6% | 803962.0 |  |
| xsa10mot | VARCHAR | 32.6% | R |  |
| sa10mot | DOUBLE | 32.6% | 0.0 |  |
| xsa10mom | VARCHAR | 32.6% | Z |  |
| sa10mom | DOUBLE | 32.6% | 0.0 |  |
| xsa10mow | VARCHAR | 32.6% | Z |  |
| sa10mow | DOUBLE | 32.6% | 0.0 |  |
| xsa11mot | VARCHAR | 32.6% | R |  |
| sa11mot | DOUBLE | 32.6% | 0.0 |  |
| xsa11mom | VARCHAR | 32.6% | Z |  |
| sa11mom | DOUBLE | 32.6% | 0.0 |  |
| xsa11mow | VARCHAR | 32.6% | Z |  |
| sa11mow | DOUBLE | 32.6% | 0.0 |  |
| xsa12mot | VARCHAR | 32.6% | R |  |
| sa12mot | DOUBLE | 32.6% | 289789.0 |  |
| xsa12mom | VARCHAR | 32.6% | R |  |
| sa12mom | DOUBLE | 32.6% | 155104.0 |  |
| xsa12mow | VARCHAR | 32.6% | R |  |
| sa12mow | DOUBLE | 32.6% | 134685.0 |  |
| xsaeq9ot | VARCHAR | 32.6% | R |  |
| saeq9ot | BIGINT | 32.6% | 4166818 |  |
| xsaeq9om | VARCHAR | 32.6% | R |  |
| saeq9om | BIGINT | 32.6% | 3261842 |  |
| xsaeq9ow | VARCHAR | 32.6% | R |  |
| saeq9ow | BIGINT | 32.6% | 904976 |  |
| xsaeq9at | VARCHAR | 32.6% | R |  |
| saeq9at | DOUBLE | 32.7% | 106841.0 |  |
| xsaeq9am | VARCHAR | 32.6% | R |  |
| saeq9am | DOUBLE | 37.0% | 108728.0 |  |
| xsaeq9aw | VARCHAR | 32.6% | R |  |
| saeq9aw | DOUBLE | 37.2% | 100553.0 |  |
| xsa09mat | VARCHAR | 32.6% | R |  |
| sa09mat | DOUBLE | 59.5% | 106743.0 |  |
| xsa09mam | VARCHAR | 32.6% | R |  |
| sa09mam | DOUBLE | 61.4% | 108466.0 |  |
| xsa09maw | VARCHAR | 32.6% | R |  |
| sa09maw | DOUBLE | 60.9% | 100495.0 |  |
| xsa10mat | VARCHAR | 32.6% | A |  |
| sa10mat | DOUBLE | 82.0% | 32000.0 |  |
| xsa10mam | VARCHAR | 32.6% | A |  |
| sa10mam | DOUBLE | 84.7% | 32000.0 |  |
| xsa10maw | VARCHAR | 32.6% | A |  |
| sa10maw | DOUBLE | 84.0% | 98843.0 |  |
| xsa11mat | VARCHAR | 32.6% | A |  |
| sa11mat | DOUBLE | 93.0% | 74248.0 |  |
| xsa11mam | VARCHAR | 32.6% | A |  |
| sa11mam | DOUBLE | 94.8% | 74248.0 |  |
| xsa11maw | VARCHAR | 32.6% | A |  |
| sa11maw | DOUBLE | 94.4% | 69591.0 |  |
| xsa12mat | VARCHAR | 32.6% | R |  |
| sa12mat | DOUBLE | 60.8% | 144895.0 |  |
| xsa12mam | VARCHAR | 32.6% | R |  |
| sa12mam | DOUBLE | 67.1% | 155104.0 |  |
| xsa12maw | VARCHAR | 32.6% | R |  |
| sa12maw | DOUBLE | 66.2% | 134685.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xsamntht | VARCHAR | 59.5% | R |  |
| samntht | BIGINT | 59.5% | 396 |  |
| xsamnthm | VARCHAR | 59.5% | R |  |
| samnthm | BIGINT | 59.5% | 321 |  |
| xsamnthw | VARCHAR | 59.5% | R |  |
| samnthw | BIGINT | 59.5% | 75 |  |
| xsaavmnt | VARCHAR | 59.5% | R |  |
| saavmnt | DOUBLE | 59.5% | 9613.0 |  |
| xsaavmnm | VARCHAR | 59.5% | R |  |
| saavmnm | DOUBLE | 62.0% | 9629.0 |  |
| xsaavmnw | VARCHAR | 59.5% | R |  |
| saavmnw | DOUBLE | 62.3% | 9544.0 |  |

## sfa

Rows: 138,503

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 100654 | Primary institution ID, joins across all IPEDS tables |
| xscugrad | VARCHAR | 26.3% | R |  |
| scugrad | DOUBLE | 26.3% | 5845.0 |  |
| xscugdgsk | VARCHAR | 87.8% | R |  |
| scugdgsk | BIGINT | 87.8% | 5726 |  |
| xscugndgs | VARCHAR | 87.8% | R |  |
| scugndgs | BIGINT | 87.8% | 119 |  |
| xscugffn | VARCHAR | 26.3% | R |  |
| scugffn | DOUBLE | 26.3% | 1976.0 |  |
| xscugffp | VARCHAR | 26.3% | R |  |
| scugffp | DOUBLE | 26.4% | 34.0 |  |
| xscfa2 | VARCHAR | 0.0% | R |  |
| scfa2 | DOUBLE | 36.8% | 5845.0 |  |
| xscfa2dg | VARCHAR | 87.8% | R |  |
| scfa2dg | DOUBLE | 92.3% | 5726.0 |  |
| xscfa2nd | VARCHAR | 87.8% | R |  |
| scfa2nd | DOUBLE | 92.3% | 119.0 |  |
| xscfa1n | VARCHAR | 0.0% | R |  |
| scfa1n | DOUBLE | 36.8% | 1976.0 |  |
| xscfa1p | VARCHAR | 0.0% | R |  |
| scfa1p | DOUBLE | 37.0% | 34.0 |  |
| xscfy2 | VARCHAR | 0.0% | A |  |
| scfy2 | DOUBLE | 63.2% | 54.0 |  |
| xscfy2dg | VARCHAR | 87.8% | A |  |
| scfy2dg | DOUBLE | 95.4% | 54.0 |  |
| xscfy2nd | VARCHAR | 87.8% | A |  |
| scfy2nd | DOUBLE | 95.4% | 0.0 |  |
| xscfy1n | VARCHAR | 0.0% | A |  |
| scfy1n | DOUBLE | 63.2% | 19.0 |  |
| xscfy1p | VARCHAR | 0.0% | A |  |
| scfy1p | DOUBLE | 63.2% | 35.0 |  |
| xuagrntn | VARCHAR | 31.0% | R |  |
| uagrntn | DOUBLE | 31.0% | 4660.0 |  |
| xuagrntp | VARCHAR | 31.0% | R |  |
| uagrntp | DOUBLE | 31.0% | 80.0 |  |
| xuagrntt | VARCHAR | 31.0% | R |  |
| uagrntt | DOUBLE | 31.0% | 58226923.0 |  |
| xuagrnta | VARCHAR | 31.0% | R |  |
| uagrnta | DOUBLE | 31.5% | 12495.0 |  |
| xudgagrntn | VARCHAR | 87.8% | R |  |
| udgagrntn | BIGINT | 87.8% | 4660 |  |
| xudgagrntp | VARCHAR | 87.8% | R |  |
| udgagrntp | BIGINT | 87.8% | 81 |  |
| xudgagrntt | VARCHAR | 87.8% | R |  |
| udgagrntt | BIGINT | 87.8% | 58226923 |  |
| xudgagrnta | VARCHAR | 87.8% | R |  |
| udgagrnta | DOUBLE | 87.9% | 12495.0 |  |
| xundagrntn | VARCHAR | 87.8% | R |  |
| undagrntn | BIGINT | 87.8% | 0 |  |
| xundagrntp | VARCHAR | 87.8% | R |  |
| undagrntp | BIGINT | 87.8% | 0 |  |
| xundagrntt | VARCHAR | 87.8% | R |  |
| undagrntt | BIGINT | 87.8% | 0 |  |
| xundagrnta | VARCHAR | 87.8% | A |  |
| undagrnta | DOUBLE | 95.8% | 4080.0 |  |
| xupgrntn | VARCHAR | 31.0% | R |  |
| upgrntn | DOUBLE | 31.0% | 3681.0 |  |
| xupgrntp | VARCHAR | 31.0% | R |  |
| upgrntp | DOUBLE | 31.0% | 63.0 |  |
| xupgrntt | VARCHAR | 31.0% | R |  |
| upgrntt | DOUBLE | 31.0% | 23657349.0 |  |
| xupgrnta | VARCHAR | 31.0% | R |  |
| upgrnta | DOUBLE | 32.0% | 6427.0 |  |
| xudgpgrntn | VARCHAR | 91.9% | R |  |
| udgpgrntn | BIGINT | 91.9% | 3681 |  |
| xudgpgrntp | VARCHAR | 87.8% | R |  |
| udgpgrntp | DOUBLE | 87.8% | 64.0 |  |
| xudgpgrntt | VARCHAR | 91.9% | R |  |
| udgpgrntt | BIGINT | 91.9% | 23657349 |  |
| xudgpgrnta | VARCHAR | 91.9% | R |  |
| udgpgrnta | DOUBLE | 92.0% | 6427.0 |  |
| xundpgrntn | VARCHAR | 91.9% | R |  |
| undpgrntn | BIGINT | 91.9% | 0 |  |
| xundpgrntp | VARCHAR | 91.9% | R |  |
| undpgrntp | DOUBLE | 91.9% | 0.0 |  |
| xundpgrntt | VARCHAR | 91.9% | R |  |
| undpgrntt | DOUBLE | 91.9% | 0.0 |  |
| xundpgrnta | VARCHAR | 91.9% | A |  |
| undpgrnta | DOUBLE | 98.6% | 6545.0 |  |
| xufloann | VARCHAR | 31.0% | R |  |
| ufloann | DOUBLE | 31.0% | 4357.0 |  |
| xufloanp | VARCHAR | 31.0% | R |  |
| ufloanp | DOUBLE | 31.0% | 75.0 |  |
| xufloant | VARCHAR | 31.0% | R |  |
| ufloant | DOUBLE | 31.0% | 30301705.0 |  |
| xufloana | VARCHAR | 31.0% | R |  |
| ufloana | DOUBLE | 38.7% | 6955.0 |  |
| xudgfloann | VARCHAR | 91.9% | R |  |
| udgfloann | BIGINT | 91.9% | 4357 |  |
| xudgfloanp | VARCHAR | 87.8% | R |  |
| udgfloanp | DOUBLE | 87.8% | 76.0 |  |
| xudgfloant | VARCHAR | 91.9% | R |  |
| udgfloant | BIGINT | 91.9% | 30301705 |  |
| xudgfloana | VARCHAR | 91.9% | R |  |
| udgfloana | DOUBLE | 92.8% | 6955.0 |  |
| xundfloann | VARCHAR | 91.9% | R |  |
| undfloann | BIGINT | 91.9% | 0 |  |
| xundfloanp | VARCHAR | 91.9% | R |  |
| undfloanp | DOUBLE | 91.9% | 0.0 |  |
| xundfloant | VARCHAR | 91.9% | R |  |
| undfloant | BIGINT | 91.9% | 0 |  |
| xundfloana | VARCHAR | 91.9% | A |  |
| undfloana | DOUBLE | 98.8% | 12500.0 |  |
| xanyaidn | VARCHAR | 0.0% | R |  |
| anyaidn | DOUBLE | 3.2% | 1769.0 |  |
| xanyaidp | VARCHAR | 0.0% | R |  |
| anyaidp | DOUBLE | 3.2% | 90.0 |  |
| xaidfsin | VARCHAR | 35.8% | R |  |
| aidfsin | DOUBLE | 38.7% | 1769.0 |  |
| xaidfsip | VARCHAR | 35.8% | R |  |
| aidfsip | DOUBLE | 38.7% | 90.0 |  |
| xagrnt_n | VARCHAR | 26.3% | R |  |
| agrnt_n | DOUBLE | 29.6% | 1698.0 |  |
| xagrnt_p | VARCHAR | 26.3% | R |  |
| agrnt_p | DOUBLE | 29.6% | 86.0 |  |
| xagrnt_t | VARCHAR | 31.0% | R |  |
| agrnt_t | DOUBLE | 34.1% | 21809164.0 |  |
| xagrnt_a | VARCHAR | 26.3% | R |  |
| agrnt_a | DOUBLE | 30.3% | 12844.0 |  |
| xfgrnt_n | VARCHAR | 0.0% | R |  |
| fgrnt_n | DOUBLE | 3.3% | 1332.0 |  |
| xfgrnt_p | VARCHAR | 0.0% | R |  |
| fgrnt_p | DOUBLE | 3.3% | 67.0 |  |
| xfgrnt_t | VARCHAR | 31.0% | R |  |
| fgrnt_t | DOUBLE | 34.1% | 9021849.0 |  |
| xfgrnt_a | VARCHAR | 0.0% | R |  |
| fgrnt_a | DOUBLE | 5.1% | 6773.0 |  |
| xpgrnt_n | VARCHAR | 26.3% | R |  |
| pgrnt_n | DOUBLE | 29.6% | 1328.0 |  |
| xpgrnt_p | VARCHAR | 26.3% | R |  |
| pgrnt_p | DOUBLE | 29.6% | 67.0 |  |
| xpgrnt_t | VARCHAR | 31.0% | R |  |
| pgrnt_t | DOUBLE | 34.1% | 8756692.0 |  |
| xpgrnt_a | VARCHAR | 26.3% | R |  |
| pgrnt_a | DOUBLE | 30.8% | 6594.0 |  |
| xofgrt_n | VARCHAR | 26.3% | R |  |
| ofgrt_n | DOUBLE | 29.6% | 123.0 |  |
| xofgrt_p | VARCHAR | 26.3% | R |  |
| ofgrt_p | DOUBLE | 29.6% | 6.0 |  |
| xofgrt_t | VARCHAR | 31.0% | R |  |
| ofgrt_t | DOUBLE | 34.1% | 265157.0 |  |
| xofgrt_a | VARCHAR | 26.3% | R |  |
| ofgrt_a | DOUBLE | 49.2% | 2156.0 |  |
| xsgrnt_n | VARCHAR | 0.0% | R |  |
| sgrnt_n | DOUBLE | 3.3% | 66.0 |  |
| xsgrnt_p | VARCHAR | 0.0% | R |  |
| sgrnt_p | DOUBLE | 3.3% | 3.0 |  |
| xsgrnt_t | VARCHAR | 31.0% | R |  |
| sgrnt_t | DOUBLE | 34.1% | 112137.0 |  |
| xsgrnt_a | VARCHAR | 0.0% | R |  |
| sgrnt_a | DOUBLE | 33.4% | 1699.0 |  |
| xigrnt_n | VARCHAR | 0.0% | R |  |
| igrnt_n | DOUBLE | 3.3% | 1330.0 |  |
| xigrnt_p | VARCHAR | 0.0% | R |  |
| igrnt_p | DOUBLE | 3.3% | 67.0 |  |
| xigrnt_t | VARCHAR | 31.0% | R |  |
| igrnt_t | DOUBLE | 34.1% | 12675178.0 |  |
| xigrnt_a | VARCHAR | 0.0% | R |  |
| igrnt_a | DOUBLE | 33.3% | 9530.0 |  |
| xloan_n | VARCHAR | 0.0% | R |  |
| loan_n | DOUBLE | 3.3% | 1503.0 |  |
| xloan_p | VARCHAR | 0.0% | R |  |
| loan_p | DOUBLE | 3.3% | 76.0 |  |
| xloan_t | VARCHAR | 31.0% | R |  |
| loan_t | DOUBLE | 34.1% | 10345864.0 |  |
| xloan_a | VARCHAR | 0.0% | R |  |
| loan_a | DOUBLE | 14.9% | 6883.0 |  |
| xfloan_n | VARCHAR | 26.3% | R |  |
| floan_n | DOUBLE | 29.6% | 1493.0 |  |
| xfloan_p | VARCHAR | 26.3% | R |  |
| floan_p | DOUBLE | 29.6% | 76.0 |  |
| xfloan_t | VARCHAR | 31.0% | R |  |
| floan_t | DOUBLE | 34.1% | 9292472.0 |  |
| xfloan_a | VARCHAR | 26.3% | R |  |
| floan_a | DOUBLE | 38.2% | 6224.0 |  |
| xoloan_n | VARCHAR | 26.3% | R |  |
| oloan_n | DOUBLE | 29.6% | 108.0 |  |
| xoloan_p | VARCHAR | 26.3% | R |  |
| oloan_p | DOUBLE | 29.6% | 5.0 |  |
| xoloan_t | VARCHAR | 31.0% | R |  |
| oloan_t | DOUBLE | 34.1% | 1053392.0 |  |
| xoloan_a | VARCHAR | 26.3% | R |  |
| oloan_a | DOUBLE | 66.5% | 9754.0 |  |
| year | BIGINT | 0.0% | 2024 | Appears in 26 tables, common join key |
| xscfa11n | VARCHAR | 4.0% | R |  |
| scfa11n | DOUBLE | 74.9% | 0.0 |  |
| xscfa11p | VARCHAR | 4.0% | R |  |
| scfa11p | DOUBLE | 74.9% | 0.0 |  |
| xscfa12n | VARCHAR | 4.0% | R |  |
| scfa12n | DOUBLE | 74.9% | 810.0 |  |
| xscfa12p | VARCHAR | 4.0% | R |  |
| scfa12p | DOUBLE | 74.9% | 52.0 |  |
| xscfa13n | VARCHAR | 4.0% | R |  |
| scfa13n | DOUBLE | 74.9% | 737.0 |  |
| xscfa13p | VARCHAR | 4.0% | R |  |
| scfa13p | DOUBLE | 74.9% | 48.0 |  |
| xscfa14n | VARCHAR | 4.0% | R |  |
| scfa14n | DOUBLE | 74.9% | 0.0 |  |
| xscfa14p | VARCHAR | 4.0% | R |  |
| scfa14p | DOUBLE | 74.9% | 0.0 |  |
| xgistn2 | VARCHAR | 35.0% | R |  |
| gistn2 | DOUBLE | 81.0% | 712.0 |  |
| xgiston2 | VARCHAR | 35.0% | R |  |
| giston2 | DOUBLE | 91.3% | 619.0 |  |
| xgistwf2 | VARCHAR | 35.0% | R |  |
| gistwf2 | DOUBLE | 81.2% | 70.0 |  |
| xgistof2 | VARCHAR | 35.0% | R |  |
| gistof2 | DOUBLE | 81.2% | 22.0 |  |
| xgistun2 | VARCHAR | 35.0% | R |  |
| gistun2 | DOUBLE | 81.1% | 1.0 |  |
| xgistt2 | VARCHAR | 35.0% | R |  |
| gistt2 | DOUBLE | 81.0% | 6598275.0 |  |
| xgista2 | VARCHAR | 35.0% | R |  |
| gista2 | DOUBLE | 81.0% | 9267.0 |  |
| xgistn1 | VARCHAR | 35.0% | R |  |
| gistn1 | DOUBLE | 81.0% | 612.0 |  |
| xgiston1 | VARCHAR | 35.0% | R |  |
| giston1 | DOUBLE | 91.4% | 471.0 |  |
| xgistwf1 | VARCHAR | 35.0% | R |  |
| gistwf1 | DOUBLE | 81.3% | 78.0 |  |
| xgistof1 | VARCHAR | 35.0% | R |  |
| gistof1 | DOUBLE | 81.3% | 63.0 |  |
| xgistun1 | VARCHAR | 35.0% | R |  |
| gistun1 | DOUBLE | 81.2% | 0.0 |  |
| xgistt1 | VARCHAR | 35.0% | R |  |
| gistt1 | DOUBLE | 81.1% | 5180341.0 |  |
| xgista1 | VARCHAR | 35.0% | R |  |
| gista1 | DOUBLE | 81.1% | 8465.0 |  |
| xgistn0 | VARCHAR | 35.0% | R |  |
| gistn0 | DOUBLE | 81.0% | 693.0 |  |
| xgiston0 | VARCHAR | 35.0% | R |  |
| giston0 | DOUBLE | 91.4% | 482.0 |  |
| xgistwf0 | VARCHAR | 35.0% | R |  |
| gistwf0 | DOUBLE | 81.4% | 158.0 |  |
| xgistof0 | VARCHAR | 35.0% | R |  |
| gistof0 | DOUBLE | 81.4% | 53.0 |  |
| xgistun0 | VARCHAR | 35.0% | R |  |
| gistun0 | DOUBLE | 81.3% | 0.0 |  |
| xgistt0 | VARCHAR | 35.0% | R |  |
| gistt0 | DOUBLE | 81.2% | 6240985.0 |  |
| xgista0 | VARCHAR | 35.0% | R |  |
| gista0 | DOUBLE | 81.2% | 9006.0 |  |
| xgis4n2 | VARCHAR | 35.0% | R |  |
| gis4n2 | DOUBLE | 81.1% | 645.0 |  |
| xgis4on2 | VARCHAR | 35.0% | R |  |
| gis4on2 | DOUBLE | 91.4% | 592.0 |  |
| xgis4wf2 | VARCHAR | 35.0% | R |  |
| gis4wf2 | DOUBLE | 81.3% | 34.0 |  |
| xgis4of2 | VARCHAR | 35.0% | R |  |
| gis4of2 | DOUBLE | 81.3% | 19.0 |  |
| xgis4un2 | VARCHAR | 35.0% | R |  |
| gis4un2 | DOUBLE | 81.2% | 0.0 |  |
| xgis4g2 | VARCHAR | 39.8% | R |  |
| gis4g2 | DOUBLE | 82.3% | 636.0 |  |
| xgis4t2 | VARCHAR | 35.0% | R |  |
| gis4t2 | DOUBLE | 81.1% | 5928907.0 |  |
| xgis4a2 | VARCHAR | 35.0% | R |  |
| gis4a2 | DOUBLE | 81.1% | 9192.0 |  |
| xgis4n12 | VARCHAR | 35.0% | R |  |
| gis4n12 | DOUBLE | 81.1% | 328.0 |  |
| xgis4g12 | VARCHAR | 39.8% | R |  |
| gis4g12 | DOUBLE | 82.3% | 328.0 |  |
| xgis4t12 | VARCHAR | 35.0% | R |  |
| gis4t12 | DOUBLE | 81.1% | 3271951.0 |  |
| xgis4a12 | VARCHAR | 35.0% | R |  |
| gis4a12 | DOUBLE | 81.2% | 9975.0 |  |
| xgis4n22 | VARCHAR | 35.0% | R |  |
| gis4n22 | DOUBLE | 81.1% | 176.0 |  |
| xgis4g22 | VARCHAR | 39.8% | R |  |
| gis4g22 | DOUBLE | 82.3% | 176.0 |  |
| xgis4t22 | VARCHAR | 35.0% | R |  |
| gis4t22 | DOUBLE | 81.1% | 1729702.0 |  |
| xgis4a22 | VARCHAR | 35.0% | R |  |
| gis4a22 | DOUBLE | 82.3% | 9828.0 |  |
| xgis4n32 | VARCHAR | 35.0% | R |  |
| gis4n32 | DOUBLE | 81.1% | 94.0 |  |
| xgis4g32 | VARCHAR | 39.8% | R |  |
| gis4g32 | DOUBLE | 82.3% | 91.0 |  |
| xgis4t32 | VARCHAR | 35.0% | R |  |
| gis4t32 | DOUBLE | 81.1% | 684364.0 |  |
| xgis4a32 | VARCHAR | 35.0% | R |  |
| gis4a32 | DOUBLE | 82.9% | 7280.0 |  |
| xgis4n42 | VARCHAR | 35.0% | R |  |
| gis4n42 | DOUBLE | 81.1% | 21.0 |  |
| xgis4g42 | VARCHAR | 39.8% | R |  |
| gis4g42 | DOUBLE | 82.3% | 18.0 |  |
| xgis4t42 | VARCHAR | 35.0% | R |  |
| gis4t42 | DOUBLE | 81.1% | 98566.0 |  |
| xgis4a42 | VARCHAR | 35.0% | R |  |
| gis4a42 | DOUBLE | 84.7% | 4694.0 |  |
| xgis4n52 | VARCHAR | 35.0% | R |  |
| gis4n52 | DOUBLE | 81.1% | 26.0 |  |
| xgis4g52 | VARCHAR | 39.8% | R |  |
| gis4g52 | DOUBLE | 82.3% | 23.0 |  |
| xgis4t52 | VARCHAR | 35.0% | R |  |
| gis4t52 | DOUBLE | 81.1% | 144324.0 |  |
| xgis4a52 | VARCHAR | 35.0% | R |  |
| gis4a52 | DOUBLE | 87.0% | 5551.0 |  |
| xgis4n1 | VARCHAR | 39.8% | R |  |
| gis4n1 | DOUBLE | 82.3% | 567.0 |  |
| xgis4on1 | VARCHAR | 39.8% | R |  |
| gis4on1 | DOUBLE | 92.6% | 439.0 |  |
| xgis4wf1 | VARCHAR | 39.8% | R |  |
| gis4wf1 | DOUBLE | 82.6% | 66.0 |  |
| xgis4of1 | VARCHAR | 39.8% | R |  |
| gis4of1 | DOUBLE | 82.6% | 62.0 |  |
| xgis4un1 | VARCHAR | 39.8% | R |  |
| gis4un1 | DOUBLE | 82.5% | 0.0 |  |
| xgis4g1 | VARCHAR | 39.8% | R |  |
| gis4g1 | DOUBLE | 82.4% | 549.0 |  |
| xgis4t1 | VARCHAR | 39.8% | R |  |
| gis4t1 | DOUBLE | 82.5% | 4640730.0 |  |
| xgis4a1 | VARCHAR | 39.8% | R |  |
| gis4a1 | DOUBLE | 82.5% | 8185.0 |  |
| xgis4n11 | VARCHAR | 39.8% | R |  |
| gis4n11 | DOUBLE | 82.5% | 311.0 |  |
| xgis4g11 | VARCHAR | 39.8% | R |  |
| gis4g11 | DOUBLE | 82.5% | 307.0 |  |
| xgis4t11 | VARCHAR | 39.8% | R |  |
| gis4t11 | DOUBLE | 82.5% | 2787106.0 |  |
| xgis4a11 | VARCHAR | 39.8% | R |  |
| gis4a11 | DOUBLE | 82.5% | 8962.0 |  |
| xgis4n21 | VARCHAR | 39.8% | R |  |
| gis4n21 | DOUBLE | 82.5% | 143.0 |  |
| xgis4g21 | VARCHAR | 39.8% | R |  |
| gis4g21 | DOUBLE | 82.5% | 142.0 |  |
| xgis4t21 | VARCHAR | 39.8% | R |  |
| gis4t21 | DOUBLE | 82.5% | 1235673.0 |  |
| xgis4a21 | VARCHAR | 39.8% | R |  |
| gis4a21 | DOUBLE | 83.5% | 8641.0 |  |
| xgis4n31 | VARCHAR | 39.8% | R |  |
| gis4n31 | DOUBLE | 82.5% | 57.0 |  |
| xgis4g31 | VARCHAR | 39.8% | R |  |
| gis4g31 | DOUBLE | 82.5% | 53.0 |  |
| xgis4t31 | VARCHAR | 39.8% | R |  |
| gis4t31 | DOUBLE | 82.5% | 378171.0 |  |
| xgis4a31 | VARCHAR | 39.8% | R |  |
| gis4a31 | DOUBLE | 84.0% | 6635.0 |  |
| xgis4n41 | VARCHAR | 39.8% | R |  |
| gis4n41 | DOUBLE | 82.5% | 29.0 |  |
| xgis4g41 | VARCHAR | 39.8% | R |  |
| gis4g41 | DOUBLE | 82.5% | 22.0 |  |
| xgis4t41 | VARCHAR | 39.8% | R |  |
| gis4t41 | DOUBLE | 82.5% | 87821.0 |  |
| xgis4a41 | VARCHAR | 39.8% | R |  |
| gis4a41 | DOUBLE | 85.8% | 3028.0 |  |
| xgis4n51 | VARCHAR | 39.8% | R |  |
| gis4n51 | DOUBLE | 82.5% | 27.0 |  |
| xgis4g51 | VARCHAR | 39.8% | R |  |
| gis4g51 | DOUBLE | 82.5% | 25.0 |  |
| xgis4t51 | VARCHAR | 39.8% | R |  |
| gis4t51 | DOUBLE | 82.5% | 151959.0 |  |
| xgis4a51 | VARCHAR | 39.8% | R |  |
| gis4a51 | DOUBLE | 87.9% | 5628.0 |  |
| xgis4n0 | VARCHAR | 39.8% | R |  |
| gis4n0 | DOUBLE | 82.3% | 657.0 |  |
| xgis4on0 | VARCHAR | 39.8% | R |  |
| gis4on0 | DOUBLE | 92.6% | 457.0 |  |
| xgis4wf0 | VARCHAR | 39.8% | R |  |
| gis4wf0 | DOUBLE | 82.7% | 150.0 |  |
| xgis4of0 | VARCHAR | 39.8% | R |  |
| gis4of0 | DOUBLE | 82.7% | 50.0 |  |
| xgis4un0 | VARCHAR | 39.8% | R |  |
| gis4un0 | DOUBLE | 82.6% | 0.0 |  |
| xgis4g0 | VARCHAR | 39.8% | R |  |
| gis4g0 | DOUBLE | 82.4% | 642.0 |  |
| xgis4t0 | VARCHAR | 39.8% | R |  |
| gis4t0 | DOUBLE | 82.6% | 5825299.0 |  |
| xgis4a0 | VARCHAR | 39.8% | R |  |
| gis4a0 | DOUBLE | 82.6% | 8867.0 |  |
| xgis4n10 | VARCHAR | 39.8% | R |  |
| gis4n10 | DOUBLE | 82.6% | 381.0 |  |
| xgis4g10 | VARCHAR | 39.8% | R |  |
| gis4g10 | DOUBLE | 82.6% | 380.0 |  |
| xgis4t10 | VARCHAR | 39.8% | R |  |
| gis4t10 | DOUBLE | 82.6% | 3713735.0 |  |
| xgis4a10 | VARCHAR | 39.8% | R |  |
| gis4a10 | DOUBLE | 82.6% | 9747.0 |  |
| xgis4n20 | VARCHAR | 39.8% | R |  |
| gis4n20 | DOUBLE | 82.6% | 141.0 |  |
| xgis4g20 | VARCHAR | 39.8% | R |  |
| gis4g20 | DOUBLE | 82.6% | 141.0 |  |
| xgis4t20 | VARCHAR | 39.8% | R |  |
| gis4t20 | DOUBLE | 82.6% | 1357002.0 |  |
| xgis4a20 | VARCHAR | 39.8% | R |  |
| gis4a20 | DOUBLE | 83.5% | 9624.0 |  |
| xgis4n30 | VARCHAR | 39.8% | R |  |
| gis4n30 | DOUBLE | 82.6% | 76.0 |  |
| xgis4g30 | VARCHAR | 39.8% | R |  |
| gis4g30 | DOUBLE | 82.6% | 73.0 |  |
| xgis4t30 | VARCHAR | 39.8% | R |  |
| gis4t30 | DOUBLE | 82.6% | 487604.0 |  |
| xgis4a30 | VARCHAR | 39.8% | R |  |
| gis4a30 | DOUBLE | 84.1% | 6416.0 |  |
| xgis4n40 | VARCHAR | 39.8% | R |  |
| gis4n40 | DOUBLE | 82.6% | 40.0 |  |
| xgis4g40 | VARCHAR | 39.8% | R |  |
| gis4g40 | DOUBLE | 82.6% | 34.0 |  |
| xgis4t40 | VARCHAR | 39.8% | R |  |
| gis4t40 | DOUBLE | 82.6% | 208688.0 |  |
| xgis4a40 | VARCHAR | 39.8% | R |  |
| gis4a40 | DOUBLE | 86.0% | 5217.0 |  |
| xgis4n50 | VARCHAR | 39.8% | R |  |
| gis4n50 | DOUBLE | 82.6% | 19.0 |  |
| xgis4g50 | VARCHAR | 39.8% | R |  |
| gis4g50 | DOUBLE | 82.6% | 14.0 |  |
| xgis4t50 | VARCHAR | 39.8% | R |  |
| gis4t50 | DOUBLE | 82.6% | 58270.0 |  |
| xgis4a50 | VARCHAR | 39.8% | R |  |
| gis4a50 | DOUBLE | 88.1% | 3067.0 |  |
| xnpist2 | VARCHAR | 35.0% | R |  |
| npist2 | DOUBLE | 81.0% | 14064.0 |  |
| xnpist1 | VARCHAR | 35.0% | R |  |
| npist1 | DOUBLE | 81.1% | 14600.0 |  |
| xnpist0 | VARCHAR | 35.0% | R |  |
| npist0 | DOUBLE | 81.2% | 12921.0 |  |
| xnpis412 | VARCHAR | 35.0% | R |  |
| npis412 | DOUBLE | 81.2% | 13776.0 |  |
| xnpis422 | VARCHAR | 35.0% | R |  |
| npis422 | DOUBLE | 82.3% | 13923.0 |  |
| xnpis432 | VARCHAR | 35.0% | R |  |
| npis432 | DOUBLE | 82.9% | 16471.0 |  |
| xnpis442 | VARCHAR | 35.0% | R |  |
| npis442 | DOUBLE | 84.7% | 19057.0 |  |
| xnpis452 | VARCHAR | 35.0% | R |  |
| npis452 | DOUBLE | 87.0% | 18200.0 |  |
| xnpis411 | VARCHAR | 39.8% | R |  |
| npis411 | DOUBLE | 82.5% | 14205.0 |  |
| xnpis421 | VARCHAR | 39.8% | R |  |
| npis421 | DOUBLE | 83.5% | 14526.0 |  |
| xnpis431 | VARCHAR | 39.8% | R |  |
| npis431 | DOUBLE | 84.1% | 16532.0 |  |
| xnpis441 | VARCHAR | 39.8% | R |  |
| npis441 | DOUBLE | 85.8% | 20139.0 |  |
| xnpis451 | VARCHAR | 39.8% | R |  |
| npis451 | DOUBLE | 88.0% | 17539.0 |  |
| xnpis410 | VARCHAR | 39.8% | R |  |
| npis410 | DOUBLE | 82.6% | 12177.0 |  |
| xnpis420 | VARCHAR | 39.8% | R |  |
| npis420 | DOUBLE | 83.5% | 12300.0 |  |
| xnpis430 | VARCHAR | 39.8% | R |  |
| npis430 | DOUBLE | 84.1% | 15508.0 |  |
| xnpis440 | VARCHAR | 39.8% | R |  |
| npis440 | DOUBLE | 86.0% | 16707.0 |  |
| xnpis450 | VARCHAR | 39.8% | R |  |
| npis450 | DOUBLE | 88.1% | 18857.0 |  |
| xgrntn2 | VARCHAR | 35.0% | A |  |
| grntn2 | DOUBLE | 57.9% | 244.0 |  |
| xgrnton2 | VARCHAR | 35.0% | A |  |
| grnton2 | DOUBLE | 85.2% | 231.0 |  |
| xgrntwf2 | VARCHAR | 35.0% | A |  |
| grntwf2 | DOUBLE | 58.9% | 13.0 |  |
| xgrntof2 | VARCHAR | 35.0% | A |  |
| grntof2 | DOUBLE | 58.9% | 0.0 |  |
| xgrntun2 | VARCHAR | 35.0% | A |  |
| grntun2 | DOUBLE | 58.7% | 0.0 |  |
| xgrntt2 | VARCHAR | 35.0% | A |  |
| grntt2 | DOUBLE | 58.1% | 3470354.0 |  |
| xgrnta2 | VARCHAR | 35.0% | A |  |
| grnta2 | DOUBLE | 58.1% | 14223.0 |  |
| xgrntn1 | VARCHAR | 35.0% | A |  |
| grntn1 | DOUBLE | 58.0% | 244.0 |  |
| xgrnton1 | VARCHAR | 35.0% | A |  |
| grnton1 | DOUBLE | 85.5% | 199.0 |  |
| xgrntwf1 | VARCHAR | 35.0% | A |  |
| grntwf1 | DOUBLE | 60.3% | 45.0 |  |
| xgrntof1 | VARCHAR | 35.0% | A |  |
| grntof1 | DOUBLE | 60.3% | 0.0 |  |
| xgrntun1 | VARCHAR | 35.0% | A |  |
| grntun1 | DOUBLE | 60.2% | 0.0 |  |
| xgrntt1 | VARCHAR | 35.0% | A |  |
| grntt1 | DOUBLE | 59.6% | 3455829.0 |  |
| xgrnta1 | VARCHAR | 35.0% | A |  |
| grnta1 | DOUBLE | 59.5% | 14163.0 |  |
| xgrntn0 | VARCHAR | 35.0% | A |  |
| grntn0 | DOUBLE | 58.0% | 249.0 |  |
| xgrnton0 | VARCHAR | 35.0% | A |  |
| grnton0 | DOUBLE | 85.7% | 200.0 |  |
| xgrntwf0 | VARCHAR | 35.0% | A |  |
| grntwf0 | DOUBLE | 61.6% | 49.0 |  |
| xgrntof0 | VARCHAR | 35.0% | A |  |
| grntof0 | DOUBLE | 61.6% | 0.0 |  |
| xgrntun0 | VARCHAR | 35.0% | A |  |
| grntun0 | DOUBLE | 61.5% | 0.0 |  |
| xgrntt0 | VARCHAR | 35.0% | A |  |
| grntt0 | DOUBLE | 60.9% | 2684585.0 |  |
| xgrnta0 | VARCHAR | 35.0% | A |  |
| grnta0 | DOUBLE | 60.8% | 10781.0 |  |
| xgrn4n2 | VARCHAR | 35.0% | A |  |
| grn4n2 | DOUBLE | 58.1% | 204.0 |  |
| xgrn4on2 | VARCHAR | 35.0% | A |  |
| grn4on2 | DOUBLE | 85.4% | 193.0 |  |
| xgrn4wf2 | VARCHAR | 35.0% | A |  |
| grn4wf2 | DOUBLE | 59.1% | 11.0 |  |
| xgrn4of2 | VARCHAR | 35.0% | A |  |
| grn4of2 | DOUBLE | 59.1% | 0.0 |  |
| xgrn4un2 | VARCHAR | 35.0% | A |  |
| grn4un2 | DOUBLE | 58.9% | 0.0 |  |
| xgrn4g2 | VARCHAR | 39.8% | A |  |
| grn4g2 | DOUBLE | 61.6% | 204.0 |  |
| xgrn4t2 | VARCHAR | 35.0% | A |  |
| grn4t2 | DOUBLE | 58.3% | 3066885.0 |  |
| xgrn4a2 | VARCHAR | 35.0% | A |  |
| grn4a2 | DOUBLE | 58.3% | 15034.0 |  |
| xgrn4n12 | VARCHAR | 35.0% | A |  |
| grn4n12 | DOUBLE | 58.3% | 32.0 |  |
| xgrn4g12 | VARCHAR | 39.8% | A |  |
| grn4g12 | DOUBLE | 61.6% | 32.0 |  |
| xgrn4t12 | VARCHAR | 35.0% | A |  |
| grn4t12 | DOUBLE | 58.3% | 602338.0 |  |
| xgrn4a12 | VARCHAR | 35.0% | A |  |
| grn4a12 | DOUBLE | 58.9% | 18823.0 |  |
| xgrn4n22 | VARCHAR | 35.0% | A |  |
| grn4n22 | DOUBLE | 58.3% | 15.0 |  |
| xgrn4g22 | VARCHAR | 39.8% | A |  |
| grn4g22 | DOUBLE | 61.6% | 15.0 |  |
| xgrn4t22 | VARCHAR | 35.0% | A |  |
| grn4t22 | DOUBLE | 58.3% | 267347.0 |  |
| xgrn4a22 | VARCHAR | 35.0% | A |  |
| grn4a22 | DOUBLE | 65.9% | 17823.0 |  |
| xgrn4n32 | VARCHAR | 35.0% | A |  |
| grn4n32 | DOUBLE | 58.3% | 24.0 |  |
| xgrn4g32 | VARCHAR | 39.8% | A |  |
| grn4g32 | DOUBLE | 61.6% | 24.0 |  |
| xgrn4t32 | VARCHAR | 35.0% | A |  |
| grn4t32 | DOUBLE | 58.3% | 402016.0 |  |
| xgrn4a32 | VARCHAR | 35.0% | A |  |
| grn4a32 | DOUBLE | 69.3% | 16751.0 |  |
| xgrn4n42 | VARCHAR | 35.0% | A |  |
| grn4n42 | DOUBLE | 58.3% | 28.0 |  |
| xgrn4g42 | VARCHAR | 39.8% | A |  |
| grn4g42 | DOUBLE | 61.6% | 28.0 |  |
| xgrn4t42 | VARCHAR | 35.0% | A |  |
| grn4t42 | DOUBLE | 58.3% | 433748.0 |  |
| xgrn4a42 | VARCHAR | 35.0% | A |  |
| grn4a42 | DOUBLE | 75.0% | 15491.0 |  |
| xgrn4n52 | VARCHAR | 35.0% | A |  |
| grn4n52 | DOUBLE | 58.3% | 105.0 |  |
| xgrn4g52 | VARCHAR | 39.8% | A |  |
| grn4g52 | DOUBLE | 61.6% | 105.0 |  |
| xgrn4t52 | VARCHAR | 35.0% | A |  |
| grn4t52 | DOUBLE | 58.3% | 1361436.0 |  |
| xgrn4a52 | VARCHAR | 35.0% | A |  |
| grn4a52 | DOUBLE | 79.4% | 12966.0 |  |
| xgrn4n1 | VARCHAR | 39.8% | A |  |
| grn4n1 | DOUBLE | 61.5% | 207.0 |  |
| xgrn4on1 | VARCHAR | 39.8% | A |  |
| grn4on1 | DOUBLE | 88.8% | 172.0 |  |
| xgrn4wf1 | VARCHAR | 39.8% | A |  |
| grn4wf1 | DOUBLE | 63.0% | 35.0 |  |
| xgrn4of1 | VARCHAR | 39.8% | A |  |
| grn4of1 | DOUBLE | 63.0% | 0.0 |  |
| xgrn4un1 | VARCHAR | 39.8% | A |  |
| grn4un1 | DOUBLE | 62.9% | 0.0 |  |
| xgrn4g1 | VARCHAR | 39.8% | A |  |
| grn4g1 | DOUBLE | 62.2% | 207.0 |  |
| xgrn4t1 | VARCHAR | 39.8% | A |  |
| grn4t1 | DOUBLE | 62.2% | 3264837.0 |  |
| xgrn4a1 | VARCHAR | 39.8% | A |  |
| grn4a1 | DOUBLE | 63.0% | 15772.0 |  |
| xgrn4n11 | VARCHAR | 39.8% | A |  |
| grn4n11 | DOUBLE | 62.2% | 31.0 |  |
| xgrn4g11 | VARCHAR | 39.8% | A |  |
| grn4g11 | DOUBLE | 62.2% | 31.0 |  |
| xgrn4t11 | VARCHAR | 39.8% | A |  |
| grn4t11 | DOUBLE | 62.2% | 556903.0 |  |
| xgrn4a11 | VARCHAR | 39.8% | A |  |
| grn4a11 | DOUBLE | 63.4% | 17965.0 |  |
| xgrn4n21 | VARCHAR | 39.8% | A |  |
| grn4n21 | DOUBLE | 62.2% | 18.0 |  |
| xgrn4g21 | VARCHAR | 39.8% | A |  |
| grn4g21 | DOUBLE | 62.2% | 18.0 |  |
| xgrn4t21 | VARCHAR | 39.8% | A |  |
| grn4t21 | DOUBLE | 62.2% | 329373.0 |  |
| xgrn4a21 | VARCHAR | 39.8% | A |  |
| grn4a21 | DOUBLE | 69.4% | 18299.0 |  |
| xgrn4n31 | VARCHAR | 39.8% | A |  |
| grn4n31 | DOUBLE | 62.2% | 32.0 |  |
| xgrn4g31 | VARCHAR | 39.8% | A |  |
| grn4g31 | DOUBLE | 62.2% | 32.0 |  |
| xgrn4t31 | VARCHAR | 39.8% | A |  |
| grn4t31 | DOUBLE | 62.2% | 539065.0 |  |
| xgrn4a31 | VARCHAR | 39.8% | A |  |
| grn4a31 | DOUBLE | 72.4% | 16846.0 |  |
| xgrn4n41 | VARCHAR | 39.8% | A |  |
| grn4n41 | DOUBLE | 62.2% | 40.0 |  |
| xgrn4g41 | VARCHAR | 39.8% | A |  |
| grn4g41 | DOUBLE | 62.2% | 40.0 |  |
| xgrn4t41 | VARCHAR | 39.8% | A |  |
| grn4t41 | DOUBLE | 62.2% | 595967.0 |  |
| xgrn4a41 | VARCHAR | 39.8% | A |  |
| grn4a41 | DOUBLE | 77.4% | 14899.0 |  |
| xgrn4n51 | VARCHAR | 39.8% | A |  |
| grn4n51 | DOUBLE | 62.2% | 86.0 |  |
| xgrn4g51 | VARCHAR | 39.8% | A |  |
| grn4g51 | DOUBLE | 62.2% | 86.0 |  |
| xgrn4t51 | VARCHAR | 39.8% | A |  |
| grn4t51 | DOUBLE | 62.2% | 1243529.0 |  |
| xgrn4a51 | VARCHAR | 39.8% | A |  |
| grn4a51 | DOUBLE | 81.3% | 14460.0 |  |
| xgrn4n0 | VARCHAR | 39.8% | A |  |
| grn4n0 | DOUBLE | 61.5% | 207.0 |  |
| xgrn4on0 | VARCHAR | 39.8% | A |  |
| grn4on0 | DOUBLE | 88.8% | 171.0 |  |
| xgrn4wf0 | VARCHAR | 39.8% | A |  |
| grn4wf0 | DOUBLE | 63.6% | 36.0 |  |
| xgrn4of0 | VARCHAR | 39.8% | A |  |
| grn4of0 | DOUBLE | 63.6% | 0.0 |  |
| xgrn4un0 | VARCHAR | 39.8% | A |  |
| grn4un0 | DOUBLE | 63.4% | 0.0 |  |
| xgrn4g0 | VARCHAR | 39.8% | A |  |
| grn4g0 | DOUBLE | 62.8% | 207.0 |  |
| xgrn4t0 | VARCHAR | 39.8% | A |  |
| grn4t0 | DOUBLE | 62.8% | 2654119.0 |  |
| xgrn4a0 | VARCHAR | 39.8% | A |  |
| grn4a0 | DOUBLE | 64.3% | 12822.0 |  |
| xgrn4n10 | VARCHAR | 39.8% | A |  |
| grn4n10 | DOUBLE | 62.8% | 26.0 |  |
| xgrn4g10 | VARCHAR | 39.8% | A |  |
| grn4g10 | DOUBLE | 62.8% | 26.0 |  |
| xgrn4t10 | VARCHAR | 39.8% | A |  |
| grn4t10 | DOUBLE | 62.8% | 426922.0 |  |
| xgrn4a10 | VARCHAR | 39.8% | A |  |
| grn4a10 | DOUBLE | 64.7% | 16420.0 |  |
| xgrn4n20 | VARCHAR | 39.8% | A |  |
| grn4n20 | DOUBLE | 62.8% | 20.0 |  |
| xgrn4g20 | VARCHAR | 39.8% | A |  |
| grn4g20 | DOUBLE | 62.8% | 20.0 |  |
| xgrn4t20 | VARCHAR | 39.8% | A |  |
| grn4t20 | DOUBLE | 62.8% | 332355.0 |  |
| xgrn4a20 | VARCHAR | 39.8% | A |  |
| grn4a20 | DOUBLE | 70.2% | 16618.0 |  |
| xgrn4n30 | VARCHAR | 39.8% | A |  |
| grn4n30 | DOUBLE | 62.8% | 20.0 |  |
| xgrn4g30 | VARCHAR | 39.8% | A |  |
| grn4g30 | DOUBLE | 62.8% | 20.0 |  |
| xgrn4t30 | VARCHAR | 39.8% | A |  |
| grn4t30 | DOUBLE | 62.8% | 326359.0 |  |
| xgrn4a30 | VARCHAR | 39.8% | A |  |
| grn4a30 | DOUBLE | 73.1% | 16318.0 |  |
| xgrn4n40 | VARCHAR | 39.8% | A |  |
| grn4n40 | DOUBLE | 62.8% | 34.0 |  |
| xgrn4g40 | VARCHAR | 39.8% | A |  |
| grn4g40 | DOUBLE | 62.8% | 34.0 |  |
| xgrn4t40 | VARCHAR | 39.8% | A |  |
| grn4t40 | DOUBLE | 62.8% | 407830.0 |  |
| xgrn4a40 | VARCHAR | 39.8% | A |  |
| grn4a40 | DOUBLE | 78.0% | 11995.0 |  |
| xgrn4n50 | VARCHAR | 39.8% | A |  |
| grn4n50 | DOUBLE | 62.8% | 107.0 |  |
| xgrn4g50 | VARCHAR | 39.8% | A |  |
| grn4g50 | DOUBLE | 62.8% | 107.0 |  |
| xgrn4t50 | VARCHAR | 39.8% | A |  |
| grn4t50 | DOUBLE | 62.8% | 1160653.0 |  |
| xgrn4a50 | VARCHAR | 39.8% | A |  |
| grn4a50 | DOUBLE | 81.8% | 10847.0 |  |
| xnpgrn2 | VARCHAR | 35.0% | A |  |
| npgrn2 | DOUBLE | 58.1% | 24170.0 |  |
| xnpgrn1 | VARCHAR | 35.0% | A |  |
| npgrn1 | DOUBLE | 59.7% | 21153.0 |  |
| xnpgrn0 | VARCHAR | 35.0% | A |  |
| npgrn0 | DOUBLE | 61.0% | 22888.0 |  |
| xnpt412 | VARCHAR | 35.0% | A |  |
| npt412 | DOUBLE | 59.0% | 19562.0 |  |
| xnpt422 | VARCHAR | 35.0% | A |  |
| npt422 | DOUBLE | 65.9% | 20562.0 |  |
| xnpt432 | VARCHAR | 35.0% | A |  |
| npt432 | DOUBLE | 69.3% | 21634.0 |  |
| xnpt442 | VARCHAR | 35.0% | A |  |
| npt442 | DOUBLE | 75.1% | 22894.0 |  |
| xnpt452 | VARCHAR | 35.0% | A |  |
| npt452 | DOUBLE | 79.4% | 25419.0 |  |
| xnpt411 | VARCHAR | 39.8% | A |  |
| npt411 | DOUBLE | 63.5% | 17530.0 |  |
| xnpt421 | VARCHAR | 39.8% | A |  |
| npt421 | DOUBLE | 69.4% | 17196.0 |  |
| xnpt431 | VARCHAR | 39.8% | A |  |
| npt431 | DOUBLE | 72.4% | 18649.0 |  |
| xnpt441 | VARCHAR | 39.8% | A |  |
| npt441 | DOUBLE | 77.4% | 20596.0 |  |
| xnpt451 | VARCHAR | 39.8% | A |  |
| npt451 | DOUBLE | 81.3% | 21035.0 |  |
| xnpt410 | VARCHAR | 39.8% | A |  |
| npt410 | DOUBLE | 64.8% | 17500.0 |  |
| xnpt420 | VARCHAR | 39.8% | A |  |
| npt420 | DOUBLE | 70.3% | 17302.0 |  |
| xnpt430 | VARCHAR | 39.8% | A |  |
| npt430 | DOUBLE | 73.2% | 17602.0 |  |
| xnpt440 | VARCHAR | 39.8% | A |  |
| npt440 | DOUBLE | 78.0% | 21925.0 |  |
| xnpt450 | VARCHAR | 39.8% | A |  |
| npt450 | DOUBLE | 81.8% | 23073.0 |  |
| xscfy11n | VARCHAR | 60.7% | A |  |
| scfy11n | DOUBLE | 98.2% | 0.0 |  |
| xscfy11p | VARCHAR | 60.7% | A |  |
| scfy11p | DOUBLE | 98.2% | 0.0 |  |
| xscfy12n | VARCHAR | 60.7% | A |  |
| scfy12n | DOUBLE | 98.2% | 0.0 |  |
| xscfy12p | VARCHAR | 60.7% | A |  |
| scfy12p | DOUBLE | 98.2% | 0.0 |  |
| xscfy13n | VARCHAR | 60.7% | A |  |
| scfy13n | DOUBLE | 98.2% | 0.0 |  |
| xscfy13p | VARCHAR | 60.7% | A |  |
| scfy13p | DOUBLE | 98.2% | 0.0 |  |
| xscfy14n | VARCHAR | 60.7% | A |  |
| scfy14n | DOUBLE | 98.2% | 0.0 |  |
| xscfy14p | VARCHAR | 60.7% | A |  |
| scfy14p | DOUBLE | 98.2% | 0.0 |  |
| xtotgrnt | VARCHAR | 95.3% | R |  |
| totgrnt | BIGINT | 95.3% | 17473759 |  |
| xtstdpel | VARCHAR | 95.3% | R |  |
| tstdpel | BIGINT | 95.3% | 1607 |  |

## v_admission_rates

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 101541 | Primary institution ID, joins across all IPEDS tables |
| year | BIGINT | 0.0% | 2017 | Appears in 26 tables, common join key |
| institution_name | VARCHAR | 0.0% | University of Mobile | Appears in 4 tables, common join key |
| state | VARCHAR | 0.0% | AL | Appears in 4 tables, common join key |
| applicants_total | BIGINT | 0.0% | 1009 |  |
| admissions_total | DOUBLE | 1.0% | 7750.0 |  |
| enrolled_total | DOUBLE | 1.3% | 1869.0 |  |
| admit_rate_pct | DOUBLE | 1.0% | 58.4 |  |
| yield_rate_pct | DOUBLE | 1.3% | 23.0 |  |

## v_institutions

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 101693 | Primary institution ID, joins across all IPEDS tables |
| institution_name | VARCHAR | 0.0% | Capri College-Cedar Rapids | Appears in 4 tables, common join key |
| ialias | VARCHAR | 46.1% | Sherman Kendall Academy |  |
| addr | VARCHAR | 0.1% | 175 Fulton Ave |  |
| city | VARCHAR | 0.0% | Mobile |  |
| state | VARCHAR | 0.0% | IA | Appears in 4 tables, common join key |
| zip_code | VARCHAR | 0.0% | 36613-2842 |  |
| fips_state | BIGINT | 0.0% | 19 |  |
| region | BIGINT | 0.0% | 5 |  |
| chfnm | VARCHAR | 2.1% | Dr. Charles Smith |  |
| chftitle | VARCHAR | 2.3% | President |  |
| gentele | DOUBLE | 11.8% | 3193641541206.0 |  |
| ein | DOUBLE | 0.9% | 630417508.0 |  |
| ueis | VARCHAR | 49.3% | MEMJEJHP6KZ6 |  |
| opeid | DOUBLE | 1.0% | 2090300.0 |  |
| opeflag | BIGINT | 0.0% | 1 |  |
| website | VARCHAR | 6.8% | www.capricollege.edu/ |  |
| adminurl | VARCHAR | 21.6% | www.capricollege.edu/ |  |
| faidurl | VARCHAR | 21.5% | https://umobile.edu/financial-aid/ |  |
| applurl | VARCHAR | 25.5% |   |  |
| npricurl | VARCHAR | 20.0% | https://umobile.edu/financial-aid/cost-calculator/ |  |
| veturl | VARCHAR | 43.1% | https://umobile.edu/veterans-affairs/ |  |
| athurl | VARCHAR | 61.8% |   |  |
| disaurl | VARCHAR | 28.3% | umobile.edu/studentsuccesscenter/disability-support-services/ |  |
| sector | BIGINT | 0.0% | 9 | Appears in 3 tables, common join key |
| level | BIGINT | 0.0% | 1 |  |
| control | BIGINT | 0.0% | 2 |  |
| hloffer | BIGINT | 0.0% | 9 |  |
| ugoffer | BIGINT | 0.0% | 1 |  |
| groffer | BIGINT | 0.0% | 2 |  |
| hdegofr1 | BIGINT | 14.2% | 0 |  |
| degree_granting | BIGINT | 0.0% | 1 |  |
| hbcu | BIGINT | 0.0% | 2 |  |
| hospital | BIGINT | 0.0% | 2 |  |
| medical | BIGINT | 0.0% | 2 |  |
| tribal | BIGINT | 0.0% | 2 |  |
| locale_code | BIGINT | 0.0% | 41 |  |
| openpubl | BIGINT | 0.0% | 1 |  |
| act | VARCHAR | 0.0% | A |  |
| newid | DOUBLE | 0.1% | -2.0 |  |
| deathyr | BIGINT | 0.0% | -2 |  |
| close_date | DOUBLE | 19.8% | -2.0 |  |
| currently_active | BIGINT | 0.0% | 1 |  |
| postsec | BIGINT | 0.0% | 1 |  |
| pseflag | BIGINT | 0.0% | 1 |  |
| pset4flg | BIGINT | 0.0% | 2 |  |
| rptmth | BIGINT | 8.4% | 1 |  |
| instcat | BIGINT | 8.4% | 6 |  |
| c00carnegie | BIGINT | 46.6% | -2 |  |
| carnegie_basic | BIGINT | 0.0% | 20 |  |
| carnegieic | BIGINT | 46.6% | 19 |  |
| carnegiesaec | BIGINT | 46.6% | 2 |  |
| carnegiersch | BIGINT | 46.6% | 0 |  |
| carnegiesize | BIGINT | 46.6% | 2 |  |
| carnegiealf | BIGINT | 46.6% | 4 |  |
| carnegieapm | BIGINT | 46.6% | 2 |  |
| carnegiegpm | BIGINT | 46.6% | -2 |  |
| land_grant | BIGINT | 9.5% | 1 |  |
| size_category | BIGINT | 9.5% | 1 |  |
| f1systyp | BIGINT | 13.4% | 1 | Appears in 3 tables, common join key |
| f1sysnam | VARCHAR | 45.4% | -2 | Appears in 3 tables, common join key |
| f1syscod | BIGINT | 19.5% | -2 |  |
| cbsa | BIGINT | 11.9% | 46140 |  |
| cbsatype | BIGINT | 11.9% | 1 |  |
| csa | BIGINT | 11.9% | 408 |  |
| county_fips | BIGINT | 14.2% | 1097 |  |
| county_name | VARCHAR | 15.0% | Mobile County |  |
| cngdstcd | BIGINT | 14.2% | 102 |  |
| longitude | DOUBLE | 15.0% | -73.633008 |  |
| latitude | DOUBLE | 15.0% | 30.793247 |  |
| year | BIGINT | 0.0% | 2025 | Appears in 26 tables, common join key |
| dfrcgid | BIGINT | 64.8% | 18 |  |
| dfrcuscg | BIGINT | 71.3% | 2 |  |
| c21ipug | BIGINT | 95.6% | 13 |  |
| c21ipgrd | BIGINT | 95.6% | -2 |  |
| c21ugprf | BIGINT | 95.6% | 1 |  |
| c21enprf | BIGINT | 95.6% | -2 |  |
| c21szset | BIGINT | 95.6% | 1 |  |
| c18basic | BIGINT | 95.6% | -2 |  |
| c15basic | BIGINT | 87.9% | -2 |  |
| ccbasic | BIGINT | 76.9% | -3 |  |
| carnegie | BIGINT | 62.8% | -3 |  |
| duns | DOUBLE | 85.5% | 78338999.0 |  |
| necta | BIGINT | 68.3% | -2 |  |
| c18ipug | BIGINT | 92.3% | 4 |  |
| c18ipgrd | BIGINT | 92.3% | 8 |  |
| c18ugprf | BIGINT | 92.3% | 5 |  |
| c18enprf | BIGINT | 92.3% | 2 |  |
| c18szset | BIGINT | 92.3% | 6 |  |
| c15ipug | BIGINT | 89.0% | -2 |  |
| c15ipgrd | BIGINT | 89.0% | -2 |  |
| c15ugprf | BIGINT | 89.0% | 4 |  |
| c15enprf | BIGINT | 89.0% | 3 |  |
| c15szset | BIGINT | 89.0% | -2 |  |
| ccipug | BIGINT | 85.9% | -3 |  |
| ccipgrad | BIGINT | 85.9% | -3 |  |
| ccugprof | BIGINT | 85.9% | -3 |  |
| ccenrprf | BIGINT | 85.9% | -3 |  |
| ccsizset | BIGINT | 85.9% | -3 |  |
| faxtele | DOUBLE | 96.4% | 7087955826.0 |  |
| tenursys | BIGINT | 90.2% | -2 | Appears in 3 tables, common join key |
| fpoffer | BIGINT | 85.8% | 2 |  |
| hdegoffr | BIGINT | 85.8% | 0 |  |
| fintele | DOUBLE | 90.7% | 6163639853.0 |  |
| admtele | DOUBLE | 90.0% | 3344606141.0 |  |
| stat_fa | BIGINT | 91.6% | 5 |  |
| stat_ic | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| lock_ic | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_c | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| lock_c | BIGINT | 91.6% | 0 | Appears in 3 tables, common join key |
| prch_c | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_c | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_c | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_wi | BIGINT | 91.6% | 1 |  |
| stat_ef | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| lock_ef | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| prch_ef | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_ef | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_ef | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| pta99_ef | BIGINT | 91.6% | 1 | Appears in 3 tables, common join key |
| ptb_ef | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| ptc_ef | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| ptd_ef | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| pteeffy | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| pteefia | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| fyrpyear | BIGINT | 91.6% | -2 | Appears in 4 tables, common join key |
| stat_sa | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| lock_sa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| prch_sa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_sa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_sa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_s | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| lock_s | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| prch_s | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_s | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_s | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_eap | BIGINT | 91.6% | -9 | Appears in 3 tables, common join key |
| lock_eap | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| prch_eap | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_eap | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_eap | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| ftemp15 | BIGINT | 91.6% | 2 | Appears in 3 tables, common join key |
| sa_excl | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_sp | BIGINT | 91.6% | -9 |  |
| form_f | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_f | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| lock_f | BIGINT | 91.6% | 0 | Appears in 3 tables, common join key |
| prch_f | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_f | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_f | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| fybeg | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| fyend | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| gpfs | BIGINT | 91.6% | -1 | Appears in 3 tables, common join key |
| f1gasbcr | BIGINT | 91.6% | -2 |  |
| f1gasbal | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_sfa | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| lock_sfa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| prch_sfa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_sfa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_sfa | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| stat_gr | BIGINT | 91.6% | 5 | Appears in 3 tables, common join key |
| lock_gr | BIGINT | 91.6% | 0 | Appears in 3 tables, common join key |
| prch_gr | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| idx_gr | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| imp_gr | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| cohrtstu | BIGINT | 91.6% | -1 | Appears in 3 tables, common join key |
| pyaid | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| cohrtaid | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| sport1 | BIGINT | 91.6% | -2 | Appears in 4 tables, common join key |
| sport2 | BIGINT | 91.6% | -1 | Appears in 4 tables, common join key |
| sport3 | BIGINT | 91.6% | -1 | Appears in 4 tables, common join key |
| sport4 | BIGINT | 91.6% | 0 | Appears in 4 tables, common join key |
| sport5 | BIGINT | 91.6% | -1 | Appears in 3 tables, common join key |
| longpgm | BIGINT | 91.6% | -2 | Appears in 3 tables, common join key |
| cohrtmt | BIGINT | 91.6% | -1 |  |
| tpr | BIGINT | 91.6% | 1 |  |
| hpr | BIGINT | 91.6% | -1 |  |
| cufasb | BIGINT | 97.7% | -2 | Appears in 3 tables, common join key |
| cugasb | BIGINT | 97.7% | -2 | Appears in 3 tables, common join key |
| fte | DOUBLE | 99.8% | 452.0 |  |
| ocrmsi | BIGINT | 91.6% | -2 |  |
| ocrhsi | BIGINT | 91.6% | 0 |  |
| twoyrcat | BIGINT | 97.7% | -4 |  |
| rev_c | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| rev_ef | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| rev_sa | BIGINT | 97.7% | -2 | Appears in 3 tables, common join key |
| rev_s | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| rev_eap | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| r_form_f | BIGINT | 97.7% | -2 |  |
| rev_f | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| rev_sfa | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| rev_gr | BIGINT | 97.7% | 0 | Appears in 3 tables, common join key |
| affil | BIGINT | 93.9% | -3 |  |
| pctmin1 | BIGINT | 93.9% | -1 |  |
| pctmin2 | BIGINT | 93.9% | -1 |  |
| pctmin3 | BIGINT | 93.9% | -1 |  |
| pctmin4 | BIGINT | 93.9% | -1 |  |
| ptacipef | BIGINT | 93.9% | -2 | Appears in 3 tables, common join key |
| transver | BIGINT | 93.9% | -2 |  |
| cindon | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinson | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotson | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cindoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinsoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotsoff | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cindfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cinsfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| cotsfam | DOUBLE | 100.0% |  | Appears in 3 tables, common join key |
| rn | BIGINT | 0.0% | 1 |  |

## v_tuition_trends

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unitid | BIGINT | 0.0% | 229799 | Primary institution ID, joins across all IPEDS tables |
| year | BIGINT | 0.0% | 2000 | Appears in 26 tables, common join key |
| institution_name | VARCHAR | 0.1% | University of Mobile | Appears in 4 tables, common join key |
| state | VARCHAR | 0.1% | AL | Appears in 4 tables, common join key |
| sector | BIGINT | 0.1% | 9 | Appears in 3 tables, common join key |
| tuition_in_state | DOUBLE | 0.0% | 3798.0 |  |
| tuition_out_state | DOUBLE | 0.0% | 8160.0 |  |
| tuition_in_district | DOUBLE | 0.0% | 8160.0 |  |
