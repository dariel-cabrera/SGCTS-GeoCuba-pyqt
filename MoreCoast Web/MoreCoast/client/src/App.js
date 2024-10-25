import React from 'react';
import { useState } from 'react';
import './App.css';
import { actualizar, eliminar, fetchData } from './db_fronted';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Swal from 'sweetalert2';
import { TablaCalculo } from './components/TablaCalculo';
import { useEffect } from 'react'; // No olvides importar useEffect
import { ButtonGroup } from './components/ButtonGroup';
import { FormularioCalculo } from './components/FormularioCalculo';




function App() {

  const [densidad_a,setDensidadA]=useState(0);
  const [densidad_m,setDensidadM]=useState(0);
  const [coeficiente,setCoeficiente]=useState(0);
  const [indice,setIndice]=useState(0);
  const [altura,setAltura]=useState(0);
  const [angulo,setAngulo]=useState(0);
  const [aceleracion,setAceleracion]=useState(0);
  const [P,setP]=useState(0);
  const [id,setId]=useState(0);
  const[calculos,setCalculos]=useState([]);
  const[editar,setEditar]=useState(false);

  
  
  const getDatos = () => {
    axios.get("http://localhost:3001/mostrar").then((respuesta) => {
      setCalculos(respuesta.data);
    })
  }


  useEffect(() => {
    getDatos();
  }, []);

  const editarCalculos = (val)=>{
      setEditar(true);
      setId(val._id);
      setDensidadA(val.densidad_a);
      setDensidadM(val.densidad_m);
      setIndice(val.indice); 
      setCoeficiente(val.coeficiente);
      setAltura(val.altura);
      setAngulo(val.angulo);
      setAceleracion(val.aceleracion);
      setP(val.P);
      
  } 
  const limpiarDatos=()=>{
    setId("");
    setDensidadA("");
    setDensidadM("");
    setIndice(""); 
    setCoeficiente("");
    setAltura("");
    setAngulo("");
    setAceleracion("");
    setP("");
    setEditar(false);
  }
  
  const calcularDatos = () => {
    if (!densidad_a || !densidad_m || !indice || !coeficiente || !altura || !angulo || !aceleracion || !P) {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Por favor, complete todos los campos antes de calcular.'
      });
      return;
    }
    fetchData(densidad_a,densidad_m,indice,coeficiente,altura,angulo,aceleracion,P);
    getDatos();
    limpiarDatos();
    Swal.fire({
      position: "top-end",
      icon: "success",
      title: "Datos Calculados con Exitos",
      showConfirmButton: false,
      timer: 1500
    });

  }
  const actualizarDatos= () =>{
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: "btn btn-success",
        cancelButton: "btn btn-danger"
      },
      buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
      title: "¿Estas Seguro?",
      text: "Deseas actualizar los datos",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Si,actualizalos!",
      cancelButtonText: "No, cancelar!",
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        actualizar(id,densidad_a,densidad_m,indice,coeficiente,altura,angulo,aceleracion,P);
        getDatos();
        swalWithBootstrapButtons.fire({
          title: "Actualizdos!",
          text: "Sus Datos han sido actualizados.",
          icon: "success"
        });
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire({
          title: "Cancelado",
          text: "Operación Cancelada",
          icon: "error"
        });
      }
    });
    limpiarDatos();

  }
  const eliminarDatos= (idValue) =>{
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: "btn btn-success",
        cancelButton: "btn btn-danger"
      },
      buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
      title: "¿Estas Seguro?",
      text: "Deseas eliminar los datos",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Si,eliminarlos!",
      cancelButtonText: "No, cancelar!",
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        eliminar(idValue);
        swalWithBootstrapButtons.fire({
          title: "Eliminados!",
          text: "Sus Datos han sido Eliminados",
          icon: "success"
        });
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire({
          title: "Cancelado",
          text: "Operación Cancelada",
          icon: "error"
        });
      }
    });
    getDatos();
    limpiarDatos();
    
  }

  return (
    <div className="container">
      <div className="card text-center">

      <div className="card-header">
        <h1>Gestión de Cálculos</h1>
      </div>

      <div className="card-body">
      
      <FormularioCalculo  
        densidad_a={densidad_a} setDensidadA={setDensidadA}
        densidad_m={densidad_m} setDensidadM={setDensidadM}
        coeficiente={coeficiente} setCoeficiente={setCoeficiente}
        indice={indice} setIndice={setIndice}
        altura={altura} setAltura={setAltura}
        angulo={angulo} setAngulo={setAngulo}
        aceleracion={aceleracion} setAceleracion={setAceleracion}
        P={P} setP={setP}
      />

      </div>
     
    {/* ButtonComponets */}
    <ButtonGroup 
        editar={editar} 
        onCalcular={calcularDatos}
        onActualizar={actualizarDatos} 
        onLimpiar={limpiarDatos}
     />
    </div>

    {/*TableComponets */}
    <TablaCalculo 
      datos={calculos} 
      onEliminar={eliminarDatos} 
      onEditar={editarCalculos}
    /> 


</div>

  );
}

export default App;