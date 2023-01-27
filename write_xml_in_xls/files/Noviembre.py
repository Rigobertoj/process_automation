from class_files import Files
import os
Nov_intereses = {
    "2235",
    "2237",
    "2238",
    "2240",
    "2241",
    "2242",
    "2243",
    "2245",
    "2246",
    "2247",
    "2248",
    "2250",
    "2251",
    "2252",
    "2255",
    "2261",
    "2262",
    "2263",
    "2264",
    "2266",
    "2267",
    "2272",
    "2274",
    "2275",
    "2276",
    "2277",
    "2280",
    "2281",
    "2282",
    "2283",
    "2284",
    "2285",
    "2286",
    "2287",
    "2288",
    "2295",
    "2300",
    "2301",
    "2302",
    "2306",
    "2330",
    "2307",
    "2319",
    "2320",
    "2321",
    "2322",
    "2323",
    "2324",
    "2325",
    "2326",
    "2327",
    "2328",
    "2329",
    "2331",
    "2332",
    "2342", }

Nov_Honorarios = {
    "2236",
    "2239",
    "2249",
    "2253",
    "2254",
    "2257",
    "2258",
    "2259",
    "2260",
    "2265",
    "2268",
    "2269",
    "2270",
    "2271",
    "2273",
    "2278",
    "2289",
    "2290",
    "2294",
    "2296",
    "2297",
    "2299",
    "2303",
    "2304",
    "2305",
    "2309",
    "2310",
    "2311",
    "2312",
    "2313",
    "2314",
    "2315",
    "2316",
    "2317",
    "2318",
}

Nov_Arrendamientos = {
    "2244",
    "2291",
    "2292",
    "2293",
    "2298", }


def generador_to_list(generador): return list((i for i in generador))


# se inicializa una varibale con la ruta de los archivos a filtrar
path = "C:/Users/rigoj/Documents/profile/process_automation/write_xml_in_xls/read_CFDI/2022/11NOVIEMBRE/"

Noviembre_CFDI = Files(path)
list_filter_files = Noviembre_CFDI.filter_files("xml")
Noviembre_CFDI.move_list_file("XML", list_filter_files)

Noviembre_CFDI.set_new_path(f"{path}/XML/")

Intereses = Noviembre_CFDI.searh_files_by_directory(Nov_intereses)
Honorarios_data = Noviembre_CFDI.searh_files_by_directory(Nov_Honorarios)
Arrendamientos_data = Noviembre_CFDI.searh_files_by_directory(Nov_Arrendamientos)

No_identificados = Noviembre_CFDI.filter_files_not_found(Nov_Arrendamientos|Nov_intereses|Nov_Honorarios)



# Noviembre_CFDI.move_list_file("Intereses", Intereses)
# Noviembre_CFDI.move_list_file("Honorarios", Honorarios_data)
# Noviembre_CFDI.move_list_file("Arrendamientos", Arrendamientos_data)

# sum_xml = len(generador_to_list(os.scandir(f"{path}XML")))
# sum_tipo_ingresos = len(generador_to_list(Intereses)) + len(
#     generador_to_list(Honorarios_data)) + len(generador_to_list(Arrendamientos_data))
# print(sum_tipo_ingresos)
