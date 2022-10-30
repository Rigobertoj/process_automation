const dotenv = require("dotenv")
const os = require("os")
const fetch = require("f")
const URL_TIIE = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos/oportuno"
const token_tiie = "ec9a753161306d648f740c2d5df1054c2ceed3c196da67704a35000e799e4801"

// let configuracion = dotenv.config(path_file)

const getTiie = async () => {
    const response = await fetch(URL_TIIE, {
        headers:{
            "Bmx-Token": token_tiie
        }
    })

    // const data = await response.json()
    console.log(response)
}

getTiie()