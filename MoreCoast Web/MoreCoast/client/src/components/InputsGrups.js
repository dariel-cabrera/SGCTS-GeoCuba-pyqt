import React from 'react'

export const InputsGroups = ({ label, value, onChange, placeholder }) => {
  return (
    <div className="input-group mb-3">
      <span className="input-group-text" id="basic-addon1">{label}</span>
      <input
        type="number"
        value={value}
        onChange={onChange}
        className="form-control"
        placeholder={placeholder}
        aria-label={label}
        aria-describedby="basic-addon1"
      />
    </div>
  );
};



