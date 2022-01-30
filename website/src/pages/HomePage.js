import React from "react";

const HomePage = () => {
  return (
    <>
      <div class="lg:2/6 xl:w-2/4 mt-10 lg:mt-20 lg:ml-16 text-left">
        <div class="text-6xl font-semibold text-gray-900 leading-none">
          Get latest information regarding the disasters near you!
        </div>
        <div class="mt-6 text-xl font-light text-true-gray-500 antialiased">
          Always keep yourself and family safe
        </div>
        <button class="mt-6 px-8 py-4 rounded-full font-normal tracking-wide bg-gradient-to-b from-blue-600 to-blue-700 text-white outline-none focus:outline-none hover:shadow-lg hover:from-blue-700 transition duration-200 ease-in-out">
          Check Tweets
        </button>
      </div>
    </>
  );
};

export default HomePage;
