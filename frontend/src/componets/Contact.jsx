import React from "react";

function Contact() {
  const phone = "1-800-207-777";

  function callNow() {
    window.location.href = `tel:${phone}`;
  }

  return (
    <div>
      <div className="contact-container">
        <div className="contact-box">
          <div className="contact-box-open-days">
            <h3>Hours of operation </h3>
            <div className="Heading-opening-days">
              <div>
                <h4 className="b">ראשון-חמישי</h4>
                <h4 className="s">9:00-17:00</h4>
              </div>
            </div>
          </div>

          <div className="contact-box-mail">
            <h3>Send us email</h3>
            <div className="Heading-mail">
              <a href="mailto:info@sce.ac.il" className="email-link">
                info@sce.ac.il
              </a>
            </div>
          </div>

          <div className="contact-box-phone">
            <h3>call us</h3>
            <div className="Heading-phone">
              <h5>Doctor Aviad Elishr 054-4870000</h5>
            </div>
          </div>

          <div className="contact-box-address">
            <h3>address</h3>
            <h5>
              <span style={{ fontWeight: "bolder" }}>באר שבע -</span> ביאליק 56
            </h5>
          </div>
        </div>

        <div className="contact-image">
          <h1>where are we</h1>
          <div style={{ width: "100%" }}>
            <iframe
              width="520"
              height="400"
              frameBorder="0"
              scrolling="no"
              marginHeight="0"
              marginWidth="0"
              src="https://maps.google.com/maps?width=520&amp;height=400&amp;hl=en&amp;q=%D7%91%D7%99%D7%90%D7%9C%D7%99%D7%A7%2056%20%D7%91%D7%90%D7%A8%20%D7%A9%D7%91%D7%A2+(%D7%9E%D7%9B%D7%9C%D7%9C%D7%AA%20%D7%A1%D7%9E%D7%99%20%D7%A9%D7%9E%D7%A2%D7%95%D7%9F)&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"
            ></iframe>
          </div>
          <h3>or click here</h3>
          <div className="Heading-location">
            <a
              href="https://www.waze.com/ul?ll=32.178485,34.899252&navigate=yes"
              target="_blank"
              rel="noreferrer"
            >
              ביאליק 56, באר שבע, ישראל
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Contact;