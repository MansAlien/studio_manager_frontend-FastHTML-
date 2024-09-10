/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "components/*.py",
    "routes/*.py",
    "templates/*.html",
    "*.py",
    './node_modules/flowbite/**/*.js'

  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
        rubik: ['Rubik', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}
