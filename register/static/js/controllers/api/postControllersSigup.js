import { postInformation } from '../../utils/api/postInformation.js';
import { createLoader } from '../../components/loader/loader.js';

const fun = (event) => {
    // event.preventDefault() evita que se envíe el formulario al servidor
    event.preventDefault();
    // form es el formulario que se envia al servidor
    const form = event.target;
    const url = form.action;
    const dataToSend = new FormData(form);
    // loader es el elemento que se muestra mientras se envía el formulario
    let loader;
    const inicialAction = () => {
        loader = createLoader();
    };
    // responseAction es una función que se ejecuta cuando la petición se ha realizado correctamente
    const responseAction = (data) => {
        // Si la petición se ha realizado correctamente, se redirige al usuario a la página de inicio
        if (data.success) {
            window.location.href = data.redirect;
            return;
        }
        // Si ocurre un error, se muestra un mensaje de error en la pantalla
        if (data.error) {
            document.getElementById('error-message').innerHTML = data.error;
            return;
        }
    };
    // errorAction es una función que se ejecuta cuando ocurre un error en la petición
    const errorAction = (error) => {
        document.getElementById('error-message').innerHTML = error;
    };
    // finallyAction es una función que se ejecuta al finalizar la petición
    const finallyAction = () => {
        loader.remove();
    };
    // postInformation es una función que se encarga de enviar información a un servidor
    // y realizar acciones dependiendo de la respuesta del servidor
    postInformation({ url, dataToSend, inicialAction, responseAction, errorAction, finallyAction });
}
// Se agrega un event listener al formulario para que se ejecute la función cuando se envíe el formulario
document.addEventListener('submit', fun);


