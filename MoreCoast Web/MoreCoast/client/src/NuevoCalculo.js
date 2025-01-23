
import PropTypes from 'prop-types';
import React  from 'react';
import { ButtonGroup } from './components/ButtonGroup';
import { FormularioCalculo } from './components/FormularioCalculo';
import Menu from './components/Menu';
import 'bootstrap/dist/css/bootstrap.min.css';

const NuevoCalculo = (
    {
        densidad_a, setDensidadA,
        densidad_m,setDensidadM,
        coeficiente, setCoeficiente,
        indice, setIndice,
        altura, setAltura,
        angulo,setAngulo,
        aceleracion, setAceleracion,
        P, setP,
        limpiarDatos,getDatos,
        editar, calcularDatos,
        id, actualizarDatos,
        
      
    })=> {
  return (
    <div className="container">
    <div className="card text-center">

    <div className="card-header">
    <h3>Nuevo Cálculo</h3>
    <Menu/> 
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

    <div className="card-body">
      <ButtonGroup
          editar={editar}
          onCalcular={() => calcularDatos({datos:{ densidad_a, densidad_m, indice, coeficiente, altura, angulo, aceleracion, P }, getDatos, limpiarDatos})}
          onActualizar={() => actualizarDatos({id, datos: {densidad_a, densidad_m, indice, coeficiente, altura, angulo, aceleracion, P }, getDatos, limpiarDatos})}
          onLimpiar={limpiarDatos}
      />
    </div>

    </div>
</div>
  )
}

NuevoCalculo.propTypes = {}

export default NuevoCalculo
