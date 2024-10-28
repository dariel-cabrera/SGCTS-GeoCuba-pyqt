import React from "react";
import { useState } from 'react';
import { FormularioUsuario } from "./components/FormularioUsuario";

function Usuario () {
    const [nombre,setNombre]= useState("");
    const [apellido,setApellido]=useState("");
    const[segundoApellido,setSegundoApellido]=useState("");
    const[correo, setCorreo]=useState("");
    const[ci,setCi]=useState("");
    const[usuario,setUsuario]= useState("");
    const[contrasena,setContrasena]=useState("");
    const[sexo,setSexo]=useState("");
    const[tipoTrabajador,setTipoTrabajador]=useState("");

    return (
    <div className="container">
      <div className="card text-center">

      <div className="card-header">
        <h1>Gestión de Usuarios</h1>
      </div>

      <div className="card-body">
        <FormularioUsuario 
            usuario={usuario} setUsuario={setUsuario}
            nombre={nombre} setNombre={setNombre}
            apellido={apellido} setApellido={setApellido}
            segundoApellido={segundoApellido} setSegundoApellido={setSegundoApellido}
            ci={ci} setCi={setCi}
            tipoTrabajador={tipoTrabajador} setTipoTrabajador={setTipoTrabajador}
            sexo={sexo} setSexo={setSexo}
            correo={correo} setCorreo={setCorreo}
            contrasena={contrasena} setContrasena={setContrasena}
        />

      </div>

      </div>

      </div>

    );






}