/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'main.py',
    '*.py',
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
