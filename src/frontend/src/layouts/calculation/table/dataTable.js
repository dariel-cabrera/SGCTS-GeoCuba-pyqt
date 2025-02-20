import React from 'react';
import PropTypes from 'prop-types';
import MDBox from 'components/MDBox';
import MDButton from 'components/MDButton';


export const TablaCalculo = ({ datos, onEliminar, onEditar }) => {
  return (
    <MDBox component="table" className="table table-striped">
      <MDBox component="thead">
        <MDBox component="tr">
          <MDBox component="th" scope="col">#</MDBox>
          <MDBox component="th" scope="col">Ubicación</MDBox>
          <MDBox component="th" scope="col">Fecha</MDBox>
          <MDBox component="th" scope="col">Densidad de Arena</MDBox>
          <MDBox component="th" scope="col">Densidad del Mar</MDBox>
          <MDBox component="th" scope="col">Coeficiente</MDBox>
          <MDBox component="th" scope="col">Indice</MDBox>
          <MDBox component="th" scope="col">Altura</MDBox>
          <MDBox component="th" scope="col">Angulo</MDBox>
          <MDBox component="th" scope="col">Aceleración</MDBox>
          <MDBox component="th" scope="col">Q</MDBox>
          <MDBox component="th" scope="col">P</MDBox>
          <MDBox component="th" scope="col">K</MDBox>
          <MDBox component="th" scope="col">Acciones</MDBox>
        </MDBox>
      </MDBox>
      <MDBox component="tbody">
        {datos.map((val, index) => (
          <MDBox component="tr" key={val._id}>
            <MDBox component="td">{index + 1}</MDBox>
            <MDBox component="td">{/* Deberías rellenar los datos de ubicación aquí */}</MDBox>
            <MDBox component="td">{/* Deberías rellenar los datos de fecha aquí */}</MDBox>
            <MDBox component="td">{val.densidad_a}</MDBox>
            <MDBox component="td">{val.densidad_m}</MDBox>
            <MDBox component="td">{val.coeficiente}</MDBox>
            <MDBox component="td">{val.indice}</MDBox>
            <MDBox component="td">{val.altura}</MDBox>
            <MDBox component="td">{val.angulo}</MDBox>
            <MDBox component="td">{val.aceleracion}</MDBox>
            <MDBox component="td">{val.Q}</MDBox>
            <MDBox component="td">{val.P}</MDBox>
            <MDBox component="td">{val.K}</MDBox>
            <MDBox component="td">
              <MDBox display="flex" justifyContent="space-between"> 
                <MDButton variant="gradient" color="info" size="small" onClick={() => onEditar(val)}>
                  Editar
                </MDButton>
                <MDButton variant="gradient" color="error" size="small" onClick={() => onEliminar(val._id)}>
                  Eliminar
                </MDButton>
                *
              </MDBox>
            </MDBox>
          </MDBox>
        ))}
      </MDBox>
    </MDBox>
  );
}
 
TablaCalculo.propTypes = {
  datos: PropTypes.array.isRequired,
  onEliminar: PropTypes.func.isRequired,
  onEditar: PropTypes.func.isRequired,
};
