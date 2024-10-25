import React from "react";
import { actualizar, eliminar, fetchData } from './db_fronted';
import Swal from 'sweetalert2';

export const calcularDatos = ({datos, getDatos, limpiarDatos}) => {

    const { densidad_a, densidad_m, indice, coeficiente, altura, angulo, aceleracion, P } = datos;

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

  export const actualizarDatos= ({id, datos, getDatos, limpiarDatos}) =>{
    const { densidad_a, densidad_m, indice, coeficiente, altura, angulo, aceleracion, P } = datos;
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
  export const eliminarDatos= ({idValue,getDatos, limpiarDatos}) =>{
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

