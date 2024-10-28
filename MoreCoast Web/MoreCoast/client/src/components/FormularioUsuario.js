import React from "react";
import { InputsGroups } from "./InputsGrups";



export const FormularioUsuario = (
    {
        usuario,setUsuario,
        nombre,setUsuario,
        apellido,setApellido,
        segundoApellido,setSegundoApellido,
        ci,setCi,
        tipoTrabajador,setTipoTrabajador,
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