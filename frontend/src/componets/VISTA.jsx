import React from "react";
import Insta from "./InstagramLoginButton";

function VISTA() {
    return (
        <div className="vista-container">
            <div className="hero-section">
                <h1 className="hero-title">Welcome to <span>VISTA</span></h1>
                <p className="hero-description">
                    Automated photo filtering for tourism using <span>deep</span> and <span>active learning</span>.
                </p>
                <Insta />
            </div>
        </div>
    );
}

export default VISTA;