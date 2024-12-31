import { NavLink , Link  } from "react-router-dom";
import logo from "../images/logo.png";

export default function NavBar() {
  return (
    <>
      <nav>
        <ul className="navbar">
          <li>
            <Link to="/">
              <img src={logo} alt="Vista Logo" className="navbar-logo" />
            </Link>
          </li>
          <li>
            <NavLink end to="/home">Home</NavLink>
          </li>
          <li>
            <NavLink to="/about">About</NavLink>
          </li>
          <li>
            <NavLink to="/gallery">Gallery</NavLink>
          </li>
          <li>
            <NavLink to="/contact">Contact</NavLink>
          </li>
          <li>
            <NavLink to="/model_test">Model Test</NavLink>
          </li>
          <li className="button">
            <button>Log In</button>
            <button>Sign Up</button>
          </li>
        </ul>
      </nav>
    </>
  );
}