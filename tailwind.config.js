/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './spaces/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"),require("daisyui")],
  daisyui: {
    themes: ["bumblebee"],
  },
}

