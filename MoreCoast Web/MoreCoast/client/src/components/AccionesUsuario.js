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
