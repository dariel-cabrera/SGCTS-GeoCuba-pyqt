import {crearUsuario,actualizarUsuario,eliminarUsuario} from '../db_fronted';
import Swal from 'sweetalert2';

export const crearUsuarios = ({datos={}, getDatos, limpiarDatos}) => {

    const {usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,constrasena} = datos;

    if (!usuario || !nombre || !apellido || !segundoApellido || !ci || !tipoTrabajador || !sexo || !correo || 
        !constrasena) {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Por favor, complete todos los campos antes registrar.'
      });
      return;
    }
    crearUsuario(usuario,nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,constrasena);
    getDatos();
    limpiarDatos();
    Swal.fire({
      position: "top-end",
      icon: "success",
      title: "Datos Registrados con Exitos",
      showConfirmButton: false,
      timer: 1500
    });

}

export const actualizarDatosUsuarios= ({id, datos={}, getDatos, limpiarDatos}) =>{

    const {usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,constrasena} = datos;
    
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
        actualizar(id,usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,constrasena);
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
