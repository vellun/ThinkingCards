import React from "react";
import cl from "./Navbar.module.css";
import justhink_logo from "../../../assets/images/justhink_logo.png";
import { Link } from "react-router-dom";
import MyButton from "../button/MyButton";

const Navbar = () => {
  return (
    <header className={cl.Header}>
      <a className={cl.HeaderLogo} href="/">
        <img
          src={justhink_logo}
          width={125}
          height={32}
          alt="JustThink"
          className={cl.HeaderLogoImage}
        ></img>
      </a>
      <nav className={cl.HeaderMenu}>
        <ul className={cl.HeaderMenuList}>
          <li className={cl.HeaderMenuItem}>
            <Link className={cl.HeaderMenuLink} to="/">
              Главная
            </Link>
          </li>
          <li className={cl.HeaderMenuItem}>
            <Link className={cl.HeaderMenuLink} to="/">
              Друзья
            </Link>
          </li>
          <li className={cl.HeaderMenuItem}>
            <Link className={cl.HeaderMenuLink} to="/">
              Правила
            </Link>
          </li>
        </ul>
      </nav>
      <a href="/login">
        <MyButton>Вход</MyButton>
      </a>
    </header>
  );
};

export default Navbar;
