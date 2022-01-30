import React from "react";
import { Link } from "react-router-dom";

const NavLinks = () => {
  const navHome =
    "text-white px-3 py-2 text-xl font-medium hover:border-b-2 border-transparent border-b-2 hover:border-current";
  const navClass =
    "text-gray-300 px-3 py-2 text-lg font-medium hover:border-b-2 border-transparent border-b-2 hover:border-current hover:text-white";

  return (
    <>
      <Link to="/" className={navHome}>
        Home
      </Link>
      <Link to="/tweets" className={navClass}>
        Tweets
      </Link>
      <Link to="/events" className={navClass}>
        Events
      </Link>
    </>
  );
};

export default NavLinks;
