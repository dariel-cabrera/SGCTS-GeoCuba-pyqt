import React from "react";
import { InputsGroups } from "./InputsGrups";
import PropTypes from 'prop-types';



export const FormularioUsuario = (
    {
        usuario,setUsuario,
        nombre,setUsuario,
        apellido,setApellido,
        segundoApellido,setSegundoApellido,
        ci,setCi,
        tipoTrabajador,setTipoTrabajador,
        sexo,setSexo,
        correo,setCorreo,
        contrasena,setContrasena

    }

    )=>{
  
    
    return (
        <>
        <InputsGroups  label ="Usuario" value={usuario}
          onChange={(e)=>setUsuario(e.target.value)}
          placeholder="Ingrese el usuario"
        />

        <InputsGroups  label ="Nombre" value={nombre}
          onChange={(e)=>setNombre(e.target.value)}
          placeholder="Ingrese el nombre del usuario"
        />

        <InputsGroups  label ="Primer Apellido" value={apellido}
          onChange={(e)=>setApellido(e.target.value)}
          placeholder="Ingrese el primer apellido del usuario"
        />

        <InputsGroups  label ="Segundo Apellido" value={segundoApellido}
          onChange={(e)=>setSegundoApellido(e.target.value)}
          placeholder="Ingrese el segundo apellido del usuario"
        />

        <InputsGroups  label ="Carnet de Identidad (Id) " value={ci}
          onChange={(e)=>setCi(e.target.value)}
          placeholder="Ingrese el Ci del  usuario"
        />

        <InputsGroups  label ="Tipo de Trabajador" value={tipoTrabajador}
          onChange={(e)=>setTipoTrabajador(e.target.value)}
          placeholder="Ingrese el tipo de Trabajador del usuario"
        />

        <InputsGroups  label ="Correo" value={correo}
          onChange={(e)=>setCorreo(e.target.value)}
          placeholder="Ingrese el correo del usuario"
        />

        <InputsGroups  label ="Contraseña" value={contrasena}
          onChange={(e)=>setContrasena(e.target.value)}
          placeholder="Ingrese la Contraseña usuario"
        /> 

        <InputsGroups  label ="Repita la Contraseña" value={contrasena}
          onChange={(e)=>setContrasena(e.target.value)}
          placeholder="Confirme la Contrasena"
        />     

        </>
    )
} 


FormularioUsuario.PropTypes={
    usuario:PropTypes.string.isRequired,
    setUsuario:PropTypes.func.isRequired,
    nombre:PropTypes.string.isRequired,
    setUsuario:PropTypes.func.isRequired,
    apellido:PropTypes.string.isRequired,
    setApellido:PropTypes.func.isRequired,
    segundoApellido:PropTypes.string.isRequired,
    setSegundoApellido:PropTypes.func.isRequired,
    ci:PropTypes.number.isRequired,
    setCi: PropTypes.func.isRequired,
    tipoTrabajador:PropTypes.string.isRequired,
    setTipoTrabajador: PropTypes.func.isRequired,
    correo:PropTypes.string.isRequired,
    setCorreo: PropTypes.func.isRequired,
    contrasena:PropTypes.string.isRequired,
    setContrasena:PropTypes.func.isRequired
}