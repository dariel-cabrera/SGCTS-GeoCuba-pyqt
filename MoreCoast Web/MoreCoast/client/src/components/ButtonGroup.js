import React from 'react';
import PropTypes from 'prop-types';
import 'bootstrap/dist/css/bootstrap.min.css';


export  const ButtonGroup = ({ editar, onCalcular, onActualizar, onLimpiar }) => {
  return (

    <div className="card-footer text-body-secondary">
            {
            editar? (
            <>
            <button className='btn btn-warning m-2' onClick={onActualizar}>Actualizar</button> 
            <button className='btn btn-info m-2' onClick={onLimpiar}>Cancelar</button> 
            <button className='btn btn-success' onClick={onCalcular}> Nuevo </button>
            </>
            ):(<button className='btn btn-success m-2' onClick={onCalcular}>Calcular</button>
            
            )}
    </div>
  )
}

ButtonGroup.propTypes = {
    onCalcular: PropTypes.func.isRequired,
    onActualizar: PropTypes.func.isRequired,
    onLimpiar: PropTypes.func.isRequired
}