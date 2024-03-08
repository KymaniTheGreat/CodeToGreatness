import {useState} from 'react'
import React from 'react'
import Navbar from './Components/Navbar/Navbar'
import Hero from './Components/Hero/Hero'
import Programs from './Components/Programs/Programs'
import Title from './Components/Title/Title'
import About from './Components/About/About'
import Campus from './Components/Campus/Campus'
import Testimonials from './Components/Testimonials/Testimonials'
import Contact from './Components/Contact/Contact'
import Footer from './Components/Footer/Footer'
import VideoPlayer from './Components/VideoPlayer/VideoPlayer'
//import VideoPlayer from './Components/VideoFolder/VideoPlayer'


const App = () => {

  const [playState, setPlayState] = useState(false);

  return (
    <div>
      <Navbar />
      <Hero/>
      <div className='container'>
        <Title subTitle='Our Program' title='What we do'/>
        <Programs/>  
        <About setPlayState={setPlayState}/> 
        <Title subTitle='Gallery' title='FGC Photos'/>
        <Campus/>
        <Title subTitle='TESTIMONIALS' title='What Member Says'/>
        <Testimonials/>
        <Title subTitle='Contact Us' title='Get in Touch'/>
        <Contact/>
        <Footer/>
      </div>
      <VideoPlayer playState={playState} setPlayState={setPlayState}/>
    </div>
    // setPlayState={setPlayState} About....
  )
}

export default App
