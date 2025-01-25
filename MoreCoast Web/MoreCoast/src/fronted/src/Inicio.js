import PropTypes from 'prop-types'
import React from 'react'

const Inicio = ((props) => {
  return (
    <div>
      {/* Header */}
      <header>
        <nav>
          <h1>Mi Aplicación</h1>
          <ul>
            <li><a href="#features">Características</a></li>
            <li><a href="#testimonials">Testimonios</a></li>
            <li><a href="#contact">Contacto</a></li>
          </ul>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="hero">
        <h2>Bienvenido a Mi Aplicación</h2>
        <p>La mejor solución para tus necesidades.</p>
        <button>Comenzar ahora</button>
      </section>

      {/* Features Section */}
      <section id="features">
        <h3>Características</h3>
        <div className="feature">
          <h4>Fácil de usar</h4>
          <p>Interfaz intuitiva para todos los usuarios.</p>
        </div>
        <div className="feature">
          <h4>Rápido y eficiente</h4>
          <p>Procesamiento rápido con resultados precisos.</p>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials">
        <h3>Lo que dicen nuestros usuarios</h3>
        <blockquote>"Esta aplicación me ha cambiado la vida"</blockquote>
        <p>- Usuario feliz</p>
      </section>

      {/* Footer */}
      <footer id="contact">
        <p>© 2025 Mi Aplicación. Todos los derechos reservados.</p>
        <a href="/terminos">Términos y Condiciones</a>
      </footer>
    </div>
  );
})

// Inicio.propTypes = {}

export default Inicio