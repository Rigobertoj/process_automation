from class_files import Files
import os

Sep_Intereses = {
"2071",
"2072",
"2073",
"2075",
"2077",
"2080",
"2081",
"2082",
"2086",
"2087",
"2088",
"2092",
"2093",
"2094",
"2095",
"2099",
"2100",
"2102",
"2103",
"2104",
"2105",
"2106",
"2107",
"2108",
"2122",
"2123",
"2124",
"2125",
"2126",
"2127",
"2131",
"2133",
"2134",
"2135",
"2139",
"2141",
"2142",
"2143",
"2144",
"2145",
"2146",
"2147",
"2148",
}


Sep_Honorarios = {
"2070",
"2074",
"2078",
"2079",
"2083",
"2084",
"2089",
"2090",
"2091",
"2096",
"2097",
"2098",
"2101",
"2110",
"2111",
"2112",
"2113",
"2115",
"2116",
"2117",
"2118",
"2119",
"2120",
"2121",
"2137",
"2138",
"2140",
}

Sep_Arrendamientos = {
"2085",
"2109",
"2129",
"2130",
"2132",
"2136",
}


path = "C:/Users/rigoj/Documents/profile/process_automation/write_xml_in_xls/read_CFDI/2022/09SEPTIEMBRE/"

SEPTIEMBRE = Files(path)
SET_OCT_XML = SEPTIEMBRE.filter_files("xml")
SEPTIEMBRE.move_list_file("XML", SET_OCT_XML)

SEPTIEMBRE.set_new_path(f"{path}XML/")

SEP_INTERESES = SEPTIEMBRE.searh_files_by_directory(Sep_Intereses)
SEP_ARRENDAMIENT = SEPTIEMBRE.searh_files_by_directory(Sep_Arrendamientos)
SEP_HONORARIOS = SEPTIEMBRE.searh_files_by_directory(Sep_Honorarios)

SEP_FILES_NOT_FUND = SEPTIEMBRE.filter_files_not_found(Sep_Intereses|Sep_Arrendamientos|Sep_Honorarios)


SEPTIEMBRE.move_list_file("Honorarios", SEP_HONORARIOS )
SEPTIEMBRE.move_list_file("Arrendamientos", SEP_ARRENDAMIENT)
SEPTIEMBRE.move_list_file("Intereses", SEP_INTERESES)

SEPTIEMBRE.move_list_file("No_identifiacos", SEP_FILES_NOT_FUND)