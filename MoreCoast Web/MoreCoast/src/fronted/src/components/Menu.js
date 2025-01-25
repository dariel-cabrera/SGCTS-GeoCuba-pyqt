
import React, { useState, useEffect, useRef } from "react";


 const Menu = () => {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const handleClickOutside = (event) => {
    if (menuRef.current && !menuRef.current.contains(event.target)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <div ref={menuRef} className={`menu-container ${isOpen ? "open" : ""}`}>
      <button onClick={toggleMenu} className="menu-button">
        ☰ Menú
      </button>
      <div className={`menu-panel ${isOpen ? "open" : ""}`}>
        <ul className="menu-list">
          <li className="menu-item">Opción 1</li>
          <li className="menu-item">Opción 2</li>
          <li className="menu-item">Opción 3</li>
        </ul>
      </div>
      {console.log("Menu sale")}
    </div>
  )
  
}

export default Menu;