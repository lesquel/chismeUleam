import { postInformation } from '../../utils/api/postInformation.js';
import { createLoader } from '../../components/loader/loader.js';

const fun = (event) => {
    event.preventDefault();
    const form = event.target;
    const url = form.action;
    const dataToSend = new FormData(form);

    let loader;
    const inicialAction = () => {
        loader = createLoader();
    };
    
    const responseAction = (data) => {
        if (data.success) {
            window.location.href = data.redirect;
            return;
        }
        if (data.error) {
            let messageData = JSON.parse(data.error);
            console.log(messageData.__all__);
                // let message = '';
                // for (let key in messageData.__all__) {
                //     message += `${key}: ${messageData[key]}`;
                // }
            document.getElementById('error-message').innerHTML = message;
            return;
        }
    };

    const errorAction = (error) => {
        document.getElementById('error-message').innerHTML = error;
    };

    const finallyAction = () => {
        loader.remove();
    };

    postInformation({ url, dataToSend, inicialAction, responseAction, errorAction, finallyAction });
}

document.addEventListener('submit', fun);


{error: '{"__all__": [{"message": "Por favor, introduzca un…s a may\\u00fasculas.", "code": "invalid_login"}]}'}