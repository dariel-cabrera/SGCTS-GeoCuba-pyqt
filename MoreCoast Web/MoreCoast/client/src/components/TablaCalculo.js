import React from 'react';
import PropTypes from 'prop-types';
import { Button } from 'react-bootstrap';

export const TablaCalculo = ({datos, onEliminar, onEditar}) => {

  return ( 
    <table className="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Ubicación</th>
          <th scope="col">Fecha</th>
          <th scope="col">Densidad de Arena</th>
          <th scope="col">Densidad del Mar</th>
          <th scope="col">Coeficiente</th>
          <th scope="col">Indice</th>
          <th scope="col">Altura</th>
          <th scope="col">Angulo</th>
          <th scope="col">Aceleración</th>
          <th scope="col">Q</th>
          <th scope="col">P</th>
          <th scope="col">K</th>
          <th scope="col">Acciones</th>
        </tr>
      </thead>
      <tbody>
        {datos.map((val, index) => (
          <tr key={val._id}>
            <td>{val._id}</td>
            <td></td>
            <td></td>
            <td>{val.densidad_a}</td>
            <td>{val.densidad_m}</td>
            <td>{val.coeficiente}</td>
            <td>{val.indice}</td>
            <td>{val.altura}</td>
            <td>{val.angulo}</td>
            <td>{val.aceleracion}</td>
            <td>{val.Q}</td>
            <td>{val.P}</td>
            <td>{val.K}</td>
            <td>
              <div className='btn-group' role='group' aria-label='Basic example'>
                <button
                  type='button'
                  onClick={() => onEditar(val)}
                  className='btn btn-info'
                >
                  Editar
                </button>
                <button
                  type='button'
                  onClick={() => onEliminar(val._id)}
                  className='btn btn-danger'
                >
                  Eliminar
                </button>
              </div>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

TablaCalculo.propTypes = {
  datos: PropTypes.array.isRequired,
  onEliminar: PropTypes.func.isRequired,
  onEditar: PropTypes.func.isRequired
}