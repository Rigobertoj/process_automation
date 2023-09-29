gastos_Febrero = {
    "Arreendamiento",
    "Comision mercantil",
    "Equipo de oficina",
    "Equipo de transporte",
    "Gastos de papeleria",
    "Gastos de telefonia e internet",
    "Gasto por servicio financiero",
    "Gastos de ferreteria",
    "Honorarios pagados",
    "Impuestos diversos",
    "Otros gastos",
    "Soporte tecnico",
    "Sofware de terceros",
    "Nomina",
}

gastos_Enero = {
    "Aportaciones.",
    "Arrendamientos.",
    "Comisiones mercantiles.",
    "Gastos por servicios financieros.",
    "Gastos por telefonia e internet.",
    "Gastos software de terceros.",
    "Honorarios pagados",
    "Impuestospagados",
    "Otros gastos ",
    "Papeleria y utiles",
    "Servicios de mantenimeinto",
    "Nomina",
}

Gastos_Marzo = {
    "Arrendamiento",
    "Comisiones mercantiles",
    "Equipo",
    "Nomina",
    "Telefono e internet",
    "Honorarios pagados",
    "Impuestos diversos",
    "Papeleria y utiles",
    "Seguros y fianzas",
    "Servicios de mantenimineto",
    "Servicios de transporte y carga",
    "Servicios financieros",
    "Sofware de terceros",
    "Soporte tecnico",
}

Gastos_Abril = {
    "Arrendamiento",
    "Gasto por servicio financiero",
    "Gasto por software a terceros",
    "Gastos por soporte tecnico",
    "Gastos de personal",
    "Gastos por comisión",
    "Honorarios pagados",
    "Impuestos diversos",
    "Mobiliario y equipo de oficina",
    "Otros gastos",
    "Papeleria y utiles",
    "Servicios de internet y telefonia",
    "Vehiculos y equipos de transporte",
}

Gastos_Mayo = {
    "Mobiliario y equipo",
    "Arrendamiento",
    "Gastos de personal",
    "Comisiones mercantiles",
    "Servicios financieros",
    "Sofware de terceros",
    "Honorarios",
    "Impuestos diversos",
    "Otros gastos",
    "Papelería y útiles",
    "Seguros y fianzas",
    "Servicios de telefonía",
    "Soporte técnico",
    "Vehículos y medios de transporte",
}

Gasto_junio = {
    "Arrendamiento de local",
    "Gasto de rentas",
    "Gasto por comisión mercantil",
    "Gastos de papelería y útiles",
    "Gastos por servicios financieros",
    "Gastos por combustibles",
    "Gastos por soporte técnico",
    "Gastos de software de terceros",
    "Honorarios pagados",
    "Impuestos diversos",
    "Otros gastos",
    "Peaje",
    "Nómina",
}

Gasto_julio = {
    "Arrendamiento",
    "Gasto por servicio financiero",
    "equipo de oficina",
    "Gasto por ferreterias",
    "Gasto en combustible",
    "Gasto por comicion mercantil",
    "Gasto por servicio de telefonia e internet",
    "Gastos por soporte tecnico",
    "Gasto por sofware de terceros",
    "Gasto sistema electrico,accesorios y componentes",
    "Honorarios pagados",
    "Impuestos diversos",
    "Invercion maquinaria y eq",
    "Nomina",
    "Otros gastos",
    "Papeleria y utiles",
    "Rentas",
    "Vehiculos de transporte",
    "Mobiliario y equipo de oficina",
}

gastos_agosto = {
    "Gasto de ejecucion",
    "Gasto por comicion mercantil",
    "Gasto por mobiliario y equipo",
    "Gastos de ferreteria",
    "Nomina",
    "Gastos equipo de oficina y computo",
    "Gastos por servicio de telefonia e internet",
    "Gastos por soporte tecnico",
    "Gastos prima de seguro",
    "Honorarios pagados",
    "Impuestos diversos",
    "otros gastos",
    "Renta",
    "Maq y equipo",
    "Papeleria y utiles",
    "Vehiculos y accesorios",
    "Fletes",
}

Gastos_septiembre = {
    "Gastos papeleria y utiles",
    "Nomina",
    "Gasto de personal",
    "Honorarios",
    "Impuestos diversos",
    "Otros gastos",
    "Arrendamiento",
    "Servicios de admin",
    "Servicios administrativos",
    "Servicios gastos financieros",
    "Moniliario y equipo",
    "Comisión mercantil",
    "Sofware de terceros",
    "Servicios de internet y telefonia",
    "Seguros y fianzas",
    "Soporte tecnico",
    "Vehiculos y equipo de transporte",
}

Gastos_octubre = {
    "Seguros y fianzas",
    "Arrendamiento",
    "Gasto por devolución",
    "Anticipos",
    "Gastos de personal (Nominas)",
    "Gastos sofware de terceros",
    "Gastos por telefonia e internet",
    "Gastos por comisiones",
    "Gastos por servicios financieros",
    "Honorarios pagados",
    "Impuestos diversos",
    "otros gastos",
    "Papeleria y utiles",
    "Fletes",
    "Servicios de mantenimiento",
    "Maq y equipo",
}

Gastos_noviembre = {
    "Gasto de rentas",
    "Honorarios",
    "Gasto por comisión",
    "Impuestos diversos",
    "Papeleria y utiles",
    "Gasto financieros",
    "Nomina",
    "Gasto de promoción y administracion",
    "Peaje",
    "Sofware de terceros",
    "Telefonia e internet",
    "Otros gastos",
    "Soporte tecnico",
    "Combustibles",
    "Productos domesticos",
    "Servicios de mantenimiento",
}

Gastos_Diciembre = {
    "Comisón mercantil",
    "equipo de oficina",
    "Nomina",
    "Ferreteria",
    "Honorarios",
    "Impuestos diveros",
    "Maq y equipo",
    "Otros gastos",
    "Papeleria y utiles",
    "Publicidad y marketing",
    "Renta",
    "Seguros y fianzas",
    "Servicios de mantenimiento",
    "Soporte tecnico",
    "Servicios financieros",
    "Sofware de terceros",
}

conjunto_de_tipos_2022 = gastos_Febrero | gastos_Enero 


for i in conjunto_de_tipos_2022:
    # print(i)
    pass
    
print(len(conjunto_de_tipos_2022))

a = {1,2,3}
b = {1,2,3}

print(a | b )