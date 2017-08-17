* Encoding: UTF-8.
SET OLang=English Unicode=Yes Locale=German Small=0 THREADS=AUTO Printback=On BASETEXTDIRECTION=AUTOMATIC DIGITGROUPING=No TLook=None SUMMARY=None MIOUTPUT=[observed imputed pooled diagnostics] TFit=Both LEADZERO=No TABLERENDER=light.

Get File 'C:\...\spss_testdata.sav'.

begin program python3.
import spss, spssdata
from load_spssvars import load_spssvars
import pandas as pd

x = load_spssvars(["test1", "test2", "test3"])
print(x)

end program.