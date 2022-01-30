import React from "react";
import { Link } from "react-router-dom";

const MobileLinks = () => {
  const navHome =
    "text-white block px-3 py-2 text-base font-medium hover:border-b-2 border-transparent border-l-2 hover:border-current";
  const navClass =
    "text-gray-300 block px-3 py-2 text-base font-medium hover:border-b-2 border-transparent border-l-2 hover:border-current";

  return (
    <>
      <Link to="/" className={navHome}>
        Home
      </Link>
      <Link to="/events" className={navClass}>
        Events
      </Link>
    </>
  );
};

export default MobileLinks;
