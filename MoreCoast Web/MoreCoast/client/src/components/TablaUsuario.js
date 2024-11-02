import React from 'react';
import PropTypes from 'prop-types';
import { Button } from 'react-bootstrap';

export const TablaUsuario = ({datos, onEliminar, onEditar}) => {

  return ( 
    <table className="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Usuario</th>
          <th scope="col">Nombre</th>
          <th scope="col">Primer Apellido</th>
          <th scope="col">Segundo Apellido</th>
          <th scope="col">CI</th>
          <th scope="col">Tipo de Trabajador</th>
          <th scope="col">Sexo</th>
          <th scope="col">Correo</th>
        </tr>
      </thead>
      <tbody>
        {datos.map((val, index) => (
          <tr key={val._id}>
            <td>{val._id}</td>
            <td></td>
            <td></td>
            <td>{val.usuario}</td>
            <td>{val.nombre}</td>
            <td>{val.apellido}</td>
            <td>{val.segundoApellido}</td>
            <td>{val.ci}</td>
            <td>{val.tipoTrabajador}</td>
            <td>{val.sexo}</td>
            <td>{val.correo}</td>
            
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

TablaUsuario.propTypes = {
  datos: PropTypes.array.isRequired,
  onEliminar: PropTypes.func.isRequired,
  onEditar: PropTypes.func.isRequired
}