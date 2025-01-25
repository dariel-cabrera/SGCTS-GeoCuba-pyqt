import PropTypes from 'prop-types';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


export const  ButonCabecera= ({ handleNuevoCalculo }) => {

  return (
    <div className="card-footer text-body-secondary">
      {
        <>
        <button className='btn btn-warning m-2' onClick={handleNuevoCalculo}> Nuevo </button>
        <button className='btn btn-warning m-2'> Salvar </button>
        </>
      }

    </div>

  )
}

ButonCabecera.propTypes = {
  handleNuevoCalculo: PropTypes.func.isRequired,
}



