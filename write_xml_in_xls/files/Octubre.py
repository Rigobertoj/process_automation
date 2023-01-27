from class_files import Files
import os

generador_to_list = lambda generador : list((i for i in generador))
Oct_Intereses = {
"2150",
"2151",
"2152",
"2153",
"2154",
"2159",
"2162",
"2163",
"2164",
"2165",
"2169",
"2170",
"2173",
"2174",
"2175",
"2176",
"2177",
"2178",
"2182",
"2183",
"2184",
"2187",
"2189",
"2190",
"2193",
"2194",
"2197",
"2198",
"2199",
"2200",
"2201",
"2203",
"2204",
"2205",
"2207",
"2211",
"2212",
"2213",
"2214",
"2215",
"2216",
"2217",
"2218",
"2219",
"2227",
"2228",
"2229",
"2230",
"2232",
"2233",
}


Oct_Honorarios = {
"2149",
"2155",
"2156",
"2157",
"2158",
"2160",
"2166",
"2167",
"2171",
"2172",
"2179",
"2180",
"2181",
"2185",
"2186",
"2188",
"2192",
"2195",
"2196",
"2202",
"2206",
"2208",
"2209",
"2210",
"2223",
"2224",
}

Oct_arrendamiento = {
"2168",
"2191",
"2220",
"2222",
"2225",
"2226",
}

oct_abono_capital = {
    "2232",
    "2178"
}


conjunto_de_ingresos = Oct_Intereses | Oct_Honorarios | Oct_arrendamiento 
lista_de_ingresos = list(Oct_Intereses) + list(Oct_Honorarios) + list(Oct_arrendamiento) 
print(len(lista_de_ingresos))

path = "C:/Users/rigoj/Documents/profile/process_automation/write_xml_in_xls/read_CFDI/2022/10OCTUBRE/"
OCTUBRE = Files(path)
SET_OCT_XML = OCTUBRE.filter_files("xml")
OCTUBRE.move_list_file("XML", SET_OCT_XML)

OCTUBRE.set_new_path(f"{path}XML/")

OCT_INTERESES = OCTUBRE.searh_files_by_directory(Oct_Intereses)
OCT_ARRENDAMIENT = OCTUBRE.searh_files_by_directory(Oct_arrendamiento)
OCT_HONORARIOS = OCTUBRE.searh_files_by_directory(Oct_Honorarios)

suma_file = len(generador_to_list(OCT_INTERESES)) + len(list(i for i in OCT_ARRENDAMIENT)) + len(list(i for i in OCT_HONORARIOS))

I = len(Oct_Intereses) 
print(I)

sum_xml =  len(generador_to_list(os.scandir(f"{path}XMl")))
print(f"""
suma todos los cfdi clasificados por tipos :  {sum_xml}  
suma de todo el conjunto de CFDI           : -{suma_file}
                                            --------------
                                              {sum_xml - suma_file}
""")


# OCTUBRE.move_list_file("Honorarios", OCT_HONORARIOS )
# OCTUBRE.move_list_file("Arrendamientos", OCT_ARRENDAMIENT)
# OCTUBRE.move_list_file("Intereses", OCT_INTERESES)


# OCT_ABONO_CAPITAL = OCTUBRE.searh_files_by_directory(oct_abono_capital)
# OCTUBRE.move_list_file("Abono capital",OCT_ABONO_CAPITAL )

print(len(conjunto_de_ingresos))
files_not_fund = OCTUBRE.filter_files_not_found(conjunto_de_ingresos)
OCTUBRE.move_list_file("No_identificados", files_not_fund)
