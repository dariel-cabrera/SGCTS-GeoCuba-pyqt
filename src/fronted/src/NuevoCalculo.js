
import PropTypes from 'prop-types';
import React  from 'react';
import { ButtonGroup } from './components/ButtonGroup';
import { FormularioCalculo } from './components/FormularioCalculo';
import Menu from './components/Menu';
import 'bootstrap/dist/css/bootstrap.min.css';

const NuevoCalculo = (
    {
        calculo,
        setCalculo,
        limpiarDatos,
        getDatos,
        editar, 
        calcularDatos,
        actualizarDatos
    })=> {
  const {id}=calculo;

  

  return (
    <div className="container">
    <div className="card text-center">

    <div className="card-header">
    <h3>Nuevo Cálculo</h3>
    <Menu/> 
    </div>

    <div className="card-body">
      
      <FormularioCalculo  
        calculo={calculo} 
        setCalculo={setCalculo}
      />
    </div> 

    <div className="card-body">
      <ButtonGroup
          editar={editar}
          onCalcular={() => calcularDatos({calculo,getDatos,limpiarDatos})}
          onActualizar={() => actualizarDatos({ id,calculo, getDatos, limpiarDatos})}
          onLimpiar={limpiarDatos}
      />
    </div>

    </div>
</div>
  )
}

NuevoCalculo.propTypes = {}

export default NuevoCalculo
