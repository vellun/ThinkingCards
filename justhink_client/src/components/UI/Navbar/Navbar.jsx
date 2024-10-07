import React from "react";
import cl from "./Navbar.module.css";

const Navbar = () => {
  return <header className={cl.Header}>
    <a className={cl.HeaderLogo} href="/"></a>
  </header>;
};

export default Navbar;
