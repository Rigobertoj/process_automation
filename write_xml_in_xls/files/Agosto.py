from class_files import Files
import os
Agos_Intereses =  {
"1967",
"1968",
"1969",
"1974",
"1979",
"1980",
"1981",
"1982",
"1991",
"1997",
"1998",
"1999",
"2016",
"2017",
"2018",
"2019",
"2020",
"2021",
"2022",
"2024",
"2028",
"2029",
"2037",
"2038",
"2039",
"2045",
"2051",
"2052",
"2053",
"2054",
"2055",
"2056",
"2057",
"2058",
"2059",
"2062",
"2063",
"2064",
"2065",
"2066",
"2068",
"2069",
}

Agos_Honorarios = {
"1965",
"1966",
"1970",
"1971",
"1973",
"1975",
"1976",
"1977",
"1978",
"1983",
"1984",
"1985",
"1987",
"1988",
"2000",
"2003",
"2004",
"2005",
"2006",
"2008",
"2013",
"2014",
"2015",
"2023",
"2025",
"2026",
"2027",
"2030",
"2031",
"2032",
"2033",
"2034",
"2035",
"2036",
"2040",
"2041",
"2042",
"2043",
"2044",
"2046",
"2047",
"2048",
"2049",
"2050",
}

Agos_Arrendamientos = {
"1986",
"1990",
"1992",
"1993",
"1994",
"1995",
"2010",
"2011",
"2012",
"2060",
"2061",
}



path = "C:/Users/rigoj/Documents/profile/process_automation/write_xml_in_xls/read_CFDI/2022/08AGOSTO/"

AGOSTO = Files(path)
SET_OCT_XML = AGOSTO.filter_files("xml")
# print(SET_OCT_XML)
AGOSTO.move_list_file("XML", SET_OCT_XML)

AGOSTO.set_new_path(f"{path}XML/")

AGO_INTERESES = AGOSTO.searh_files_by_directory(Agos_Intereses)
AGO_ARRENDAMIENT = AGOSTO.searh_files_by_directory(Agos_Arrendamientos)
AGO_HONORARIOS = AGOSTO.searh_files_by_directory(Agos_Honorarios)

SEP_FILES_NOT_FUND = AGOSTO.filter_files_not_found(Agos_Intereses|Agos_Arrendamientos|Agos_Honorarios)


AGOSTO.move_list_file("Honorarios", AGO_HONORARIOS)
AGOSTO.move_list_file("Arrendamientos", AGO_ARRENDAMIENT)
AGOSTO.move_list_file("Intereses", AGO_INTERESES)

AGOSTO.move_list_file("No_identifiacos", SEP_FILES_NOT_FUND)