import React from "react";
import { InputsGroups } from "./InputsGrups";



export const FormularioUsuario = ()=>{
  
    {/*  <InputsGroups label="Densidad de Arena" value={densidad_a} 
        onChange={(e) => setDensidadA(e.target.value)}
        placeholder="Ingrese el valor de la Densidad de Arena" /> */}
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

        <InputsGroups  label ="Apellido" value={apellido}
          onChange={(e)=>setApellido(e.target.value)}
          placeholder="Ingrese el nombre del usuario"
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