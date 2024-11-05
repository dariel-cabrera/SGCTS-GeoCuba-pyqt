import {crearUsuario,actualizarUsuario,eliminarUsuario} from '../db_fronted';
import Swal from 'sweetalert2';

export const crearUsuarios = ({datos={}, limpiarDatos}) => {

    const {usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena} = datos;
  
    if (!usuario || !nombre || !apellido || !segundoApellido || !ci || !tipoTrabajador || !sexo || !correo || !contrasena) {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Por favor, complete todos los campos antes registrar.'
      });
      return;
    }
    crearUsuario(usuario,nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena);
    /*getDatosUsuarios(); */
    limpiarDatos();
    Swal.fire({
      position: "top-end",
      icon: "success",
      title: "Datos Registrados con Exitos",
      showConfirmButton: false,
      timer: 1500
    });

}

export const actualizarDatosUsuarios= ({id, datos={}, getDatosUsuario, limpiarDatos}) =>{

    const {usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena} = datos;
    

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
        actualizarUsuario(id,usuario, nombre,apellido,segundoApellido,ci,tipoTrabajador,sexo,correo,contrasena);
        getDatosUsuario()
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

  export const eliminarDatosUsuario= ({idValue,getDatosUsuario, limpiarDatos}) =>{
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
        eliminarUsuario(idValue);
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
    getDatosUsuario();
    limpiarDatos();
    
  }
