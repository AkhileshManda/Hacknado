import React, { useEffect, useState } from "react";
import axios from "axios";

const Events = () => {
  const [eventsList, setEventsList] = useState([]);

  useEffect(() => {
    const getData = async () => {
      const events = await axios.get("http://127.0.0.1:5000/list");
      setEventsList(events.data);
      console.log(events.data);
    };
    getData();
  }, []);

  const tweets = ["1487779404969578503", "1487754370301448192"];

  return (
    <>
      {console.log(eventsList)}
      {!eventsList ? (
        <div>Loading...</div>
      ) : (
        <div className="p-8">
          <div className="sm:grid gap-5 md:grid-cols-2 lg:grid-cols-3 2xl:flex flex-wrap justify-center">
            {Object.values(eventsList).map((event, i) => (
              <>
                <div className="m-3">
                  <h2 className="text-lg mb-2">
                    {Object.values(event)[0]}
                    <span className="text-sm text-teal-800 font-mono bg-teal-100 inline rounded-full px-2 align-top float-right animate-pulse">
                      {Object.values(event)[1]}
                    </span>
                  </h2>
                  <blockquote class="twitter-tweet">
                    {console.log(Object.values(event)[4])}
                    <a href={`https://twitter.com/x/status/${tweets[i]}`}></a>
                  </blockquote>
                </div>
              </>
            ))}
          </div>
        </div>
      )}
    </>
  );
};

export default Events;
