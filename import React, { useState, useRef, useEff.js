import React, { useState, useRef, useEffect } from 'react';
import './EyeFollow.css'; // Arquivo de estilos que definiremos abaixo

const EyeFollowLogin = () => {
  // Estado para guardar a rotação (x, y) das pupilas
  const [coords, setCoords] = useState({ x: 0, y: 0 });
  // Estado para o "humor" (neutral, shy)
  const [mood, setMood] = useState('neutral');

  // Referências para os elementos dos olhos
  const eyeLeftRef = useRef(null);
  const eyeRightRef = useRef(null);

  useEffect(() => {
    // Função que roda a cada movimento do mouse
    const handleMouseMove = (event) => {
      // Pegamos a posição do mouse na tela inteira
      const mouseX = event.clientX;
      const mouseY = event.clientY;

      // Calculamos a rotação baseada no olho esquerdo (funciona para os dois)
      if (eyeLeftRef.current) {
        const rect = eyeLeftRef.current.getBoundingClientRect();
        // Encontramos o centro do olho
        const eyeX = rect.left + rect.width / 2;
        const eyeY = rect.top + rect.height / 2;

        // Calculamos o ângulo entre o centro do olho e o mouse
        const angleRad = Math.atan2(mouseY - eyeY, mouseX - eyeX);
        const angleDeg = (angleRad * 180) / Math.PI;

        // Atualizamos o estado com o ângulo de rotação
        setCoords({ x: angleDeg, y: angleDeg });
      }
    };

    // Adicionamos o ouvinte de evento ao mover o mouse
    window.addEventListener('mousemove', handleMouseMove);

    // Limpeza do evento ao desmontar o componente (boa prática)
    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
    };
  }, []); // Roda apenas uma vez no carregamento

  // Estilo dinâmico para aplicar a rotação nas pupilas
  const pupilStyle = {
    transform: `rotate(${coords.x}deg)`,
  };

  return (
    <div className="login-wrapper">
      <div className={`character-box ${mood}`}>
        <div className="character-face">
          <div className="eyes-container">
            {/* Olho Esquerdo */}
            <div className="eye" ref={eyeLeftRef}>
              <div className="pupil" style={pupilStyle}></div>
            </div>
            {/* Olho Direito */}
            <div className="eye" ref={eyeRightRef}>
              <div className="pupil" style={pupilStyle}></div>
            </div>
          </div>
          <div className="mouth"></div>
        </div>
      </div>

      <div className="form-card">
        <h2>Área do Cliente</h2>
        <input 
          type="email" 
          placeholder="E-mail" 
          onFocus={() => setMood('happy')} 
          onBlur={() => setMood('neutral')}
        />
        <input 
          type="password" 
          placeholder="Senha" 
          onFocus={() => setMood('shy')} 
          onBlur={() => setMood('neutral')}
        />
        <button className="login-btn">Entrar no Sistema</button>
      </div>
    </div>
  );
};

export default EyeFollowLogin;

