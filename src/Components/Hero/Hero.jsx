import React from 'react'
import './Hero.css'
import dark_arrow from '../../assets/dark-arrow.png'

const Hero = () => {
  return (
    <div className='hero container'>
      <div className="hero-text">
        <h1>Our mission is to share the Gospel</h1>
        <p>All authority in heaven and on earth has been given to me. Go therefore and make disciples of all nations, 
        baptizing them in the name of the Father and of the Son and of the Holy Spirit, and teaching them to obey everything that 
        I have commanded you.</p>
        <button className='btn'>Explore more <img src={dark_arrow} alt="" /></button>
      </div>
      
    </div>
  )
}

export default Hero
