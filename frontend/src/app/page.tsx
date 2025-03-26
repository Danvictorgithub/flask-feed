import Link from "next/link";

export default function Home() {
  return (
    <main>
      <section className="w-full min-h-screen bg-white">
        <div className="container relative flex flex-col min-h-screen px-6 py-8 mx-auto">
          <section className="flex items-center flex-1">
            <div className="flex flex-col w-full">
              <h1 className="text-5xl font-extrabold text-center lg:text-7xl 2xl:text-8xl">
                <span className="text-transparent bg-gradient-to-br bg-clip-text from-teal-500 via-indigo-500 to-sky-500">
                  Flask
                </span>
                <span className="text-transparent bg-gradient-to-tr bg-clip-text from-blue-500 via-pink-500 to-red-500">
                  Feed
                </span>
              </h1>
              <p className="max-w-3xl mx-auto mt-6 text-lg text-center text-gray-700 md:text-xl">
                Just a simple socia media feed app
              </p>
              <div className="flex flex-col mt-8 space-y-3 sm:-mx-2 sm:flex-row sm:justify-center sm:space-y-0">
                <Link href="/auth/sign_in">
                  <button className="px-6 py-3 text-sm font-medium tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-500 rounded-md hover:bg-blue-600 focus:bg-blue-600 focus:outline-none sm:mx-2">
                    sign in
                  </button>
                </Link>
                <Link href="/auth/sign_up">
                  <button className="px-6 py-3 text-sm font-medium tracking-wide text-blue-500 capitalize transition-colors duration-300 transform border border-blue-500 rounded-md hover:bg-blue-500 hover:text-white focus:bg-blue-500 focus:text-white focus:outline-none sm:mx-2">
                    sign up
                  </button>
                </Link>
              </div>
            </div>
          </section>
        </div>
      </section>
    </main>
  );
}
