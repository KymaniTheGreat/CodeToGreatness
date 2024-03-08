import React from 'react'
import './Contact.css'
import msg_icon from '../../assets/msg-icon.png'
import mail_icon from '../../assets/mail-icon.png'
import phone_icon from '../../assets/phone-icon.png'
import location_icon from '../../assets/location-icon.png'
import white_arrow from '../../assets/white-arrow.png'



const Contact = () => {

    const [result, setResult] = React.useState("");

  const onSubmit = async (event) => {
    event.preventDefault();
    setResult("Sending....");
    const formData = new FormData(event.target);

    formData.append("access_key", "0afdaa86-6563-4b58-afbf-62159346151c");

    const response = await fetch("https://api.web3forms.com/submit", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.success) {
      setResult("Form Submitted Successfully");
      event.target.
      event.target.reset();
    } else {
      console.log("Error", data);
      setResult(data.message);
    }
  };


  return (
    <div className='contact'>
      <div className="contact-col">
        <h3>Send us a message <img src={msg_icon} alt=""/></h3>
        <p> Feeling lost or facing challenges? Share your prayer request with our caring church community. 
        No burden is too big for God's love. We believe in the power 
        of prayer, and we're here to support you.g</p>
        <ul>
            <li><img src={mail_icon} alt=''/>kymani.wilson@gmail.com</li>
            <li><img src={phone_icon} alt=''/>+1 876-334-0112</li>
            <li><img src={location_icon} alt=''/>Hendon, Norwood, Montego Bay, St. James</li>
        </ul>
      </div>
      <div className="contact-col">
        <form onSubmit={onSubmit}>
            <label>Your name</label>
            <input type="text" name='name' placeholder='Enter your name'
            required/>
            <label>Phone number</label>
            <input type="tel" name='phone' placeholder='Enter your mobile number' required/>
            <label>Type your message</label>
            <textarea name="message" rows="6" placeholder='enter your message'
            required></textarea>
            <button type='submit' className='btn dark-btn'>Submit now 
            <img src={white_arrow} alt=''/></button>
        </form>
        <span>{result}</span>
      </div>
    </div>
  )
}

export default Contact


{/**
 */}
