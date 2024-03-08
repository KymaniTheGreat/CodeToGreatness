import React from 'react'
import './About.css'
import about_img from '../../assets/about.png'
import play_icon from '../../assets/play-icon.png'

const About = ({setPlayState}) => {
  return (
    <div className='about'>
      <div className='about-left'>
        <img src={about_img} alt="" className='about-img'/>
        <img src={play_icon} alt="" className='play-icon' onClick={()=>{setPlayState(true)}}/>
      </div>
      <div className='about-right'>
        <h3>ABOUT FGC</h3>
        <h2>Ambassadors For Christ</h2>
        <p>lorem gegug erger gj egjer gegegege geg e rge grergerg eg ergegeg
        geg rgerg egegeregg rge rg rg reg er gerg regr ge rg ge ge rg rg erger greg eg
        ergrg rge grg re afa dedrgrgg eg e f afe the  tj e df the bou 
        </p>
        <p>lorem gegug erger gj egjer gegegege geg e rge grergerg eg ergegeg
        geg rgerg egegeregg rge rg rg reg er gerg regr ge rg ge ge rg rg erger greg eg
        ergrg rge grg re afa dedrgrgg eg e f afe the  tj e df the bou 
        </p>
        <p>lorem gegug erger gj egjer gegegege geg e rge grergerg eg ergegeg
        geg rgerg egegeregg rge rg rg reg er gerg regr ge rg ge ge rg rg erger greg eg
        ergrg rge grg re afa dedrgrgg eg e f afe the  tj e df the bou 
        </p>
      </div>
    </div>
    // {setPlayState}
    //onClick={()=>
                  // {setPlayState(true)}}

  )
}

export default About
