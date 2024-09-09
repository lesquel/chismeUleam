/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            fontFamily: {
                matemasie: ["Matemasie", "sans-serif"],
                popins: ["Poppins", "sans-serif"],
                Courier_New: ["Courier New", "sans-serif"],
            },
            colors: {
                naranja_claro: {
                    light: "#F39B7F",
                    DEFAULT: "#F39B7F",
                    dark: "#F39B7F",
                },
                verder_claro: {
                    light: "#4A7766",
                    DEFAULT: "#4A7766",
                    dark: "#4A7766",
                },
                negro: {
                    light: "#001219",
                    DEFAULT: "#001219",
                    dark: "#001219",
                },
                ese_color: {
                    light: "#E3E3E3",
                    DEFAULT: "#E3E3E3",
                    dark: "#E3E3E3",
                },
                blanco: {
                    light: "#ECE7E2",
                    DEFAULT: "#ECE7E2",
                    dark: "#ECE7E2",
                },
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
