/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*html"],
  theme: {
    extend: {
      backgroundImage: {
        'create_tweet_image': "url('/icon/image.svg')",
      }
    },
  },
  plugins: [],
}
