import React from "react";
import { useState,useEffect } from 'react';
import { FormularioUsuario } from "./components/FormularioUsuario";
import { ButtonUsuario } from "./components/ButtonUsuarios";
import { TablaUsuario } from "./components/TablaUsuario";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import axios from 'axios';
import { crearUsuarios,actualizarDatosUsuarios,eliminarDatosUsuario } from "./components/AccionesUsuario";


function Usuario () {
    const [id,setId]=useState(0);
    const [nombre,setNombre]= useState("");
    const [apellido,setApellido]=useState("");
    const[segundoApellido,setSegundoApellido]=useState("");
    const[correo, setCorreo]=useState("");
    const[ci,setCi]=useState(0);
    const[usuario,setUsuario]= useState("");
    const[contrasena,setContrasena]=useState("");
    const[confirmarContrasena,setConfirmarContrasena]=useState("");
    const[sexo,setSexo]=useState(true);
    const[tipoTrabajador,setTipoTrabajador]=useState("");
    const[usuariosData,setUsuariosData]=useState([]);
    const[editarUsuario,setEditarUsuario]=useState(false);

    const getDatosUsuario = () => {
      axios.get("http://localhost:3001/mostrarUsuario").then((respuesta) => {
        setUsuariosData(respuesta.data);
      })
    }
    useEffect(() => {
      getDatosUsuario();
    }, []); 


    const limpiarDatos=()=>{
      setId(0);
      setEditarUsuario(false);
      setUsuario("");
      setNombre("");
      setApellido("");
      setSegundoApellido("");
      setCi(0);
      setCorreo("");
      setTipoTrabajador("");
      setContrasena("");
      setConfirmarContrasena("")
      setSexo(true);
    }
  
    const editarUsuarios = (val)=>{
      console.log('Editando Datos');
      setEditarUsuario(true);
      setUsuario(val.usuario);
      setNombre(val.nombre);
      setApellido(val.apellido);
      setSegundoApellido(val.segundoApellido);
      setCi(val.ci);
      setCorreo(val.correo);
      setTipoTrabajador(val.tipoTrabajador);
      
  }

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
            confirmarContrasena={confirmarContrasena} setConfirmarContrasena={setConfirmarContrasena}
        />

      </div>
       

      <ButtonUsuario 
          editar={editarUsuario}
          onLimpiar={limpiarDatos}
          onActualizar={()=>actualizarDatosUsuarios({
            datos:{id,usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena},
            /*getDatosUsuario, */
            limpiarDatos})}
            onRegistrar={()=>crearUsuarios({
            datos:{usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena},
            /*getDatosUsuario,*/
            limpiarDatos})}
      />
      </div>

      <TablaUsuario
         datos={usuariosData}
         onEliminar={(id)=>eliminarDatosUsuario({idValue:id,getDatosUsuario,limpiarDatos})}
         onEditar={(val)=>{
          editarUsuarios(val);
          setEditarUsuario(true);
          setId(val._id);
         }}
      />

      </div>

    );

}

export default Usuario;