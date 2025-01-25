import React from 'react';
import { InputsGroups } from './InputsGrups';

export const FormularioCalculo = ({ calculo, setCalculo }) => {
  // Manejar el cambio de valores
  const handleInputChange = (field, value) => {
    setCalculo((prev) => ({
      ...prev,
      [field]: isNaN(value) ? value : parseFloat(value),
    }));
  };

  // Configuración de los campos del formulario
  const campos = [
    {
      label: "Densidad de Arena",
      key: "densidad_a",
      placeholder: "Ingrese el valor de la Densidad de Arena",
    },
    {
      label: "Densidad del Mar",
      key: "densidad_m",
      placeholder: "Ingrese el valor de la Densidad del Mar",
    },
    {
      label: "Coeficiente de Porosidad",
      key: "coeficiente",
      placeholder: "Ingrese el valor del Coeficiente de Porosidad",
    },
    {
      label: "Índice de Rompiente",
      key: "indice",
      placeholder: "Ingrese el valor del Índice de Rompiente",
    },
    {
      label: "Altura",
      key: "altura",
      placeholder: "Ingrese el valor de la Altura",
    },
    {
      label: "Ángulo",
      key: "angulo",
      placeholder: "Ingrese el valor del Ángulo",
    },
    {
      label: "Aceleración de la Gravedad",
      key: "aceleracion",
      placeholder: "Ingrese el valor de la Aceleración de la Gravedad",
    },
    {
      label: "P",
      key: "P",
      placeholder: "Ingrese el valor de P",
    },
  ];

  return (
    <>
      {campos.map((campo) => (
        <InputsGroups
          key={campo.key}
          label={campo.label}
          value={calculo[campo.key] || ""}
          type="number"
          onChange={(e) => handleInputChange(campo.key, e.target.value)}
          placeholder={campo.placeholder}
        />
      ))}
    </>
  );
};