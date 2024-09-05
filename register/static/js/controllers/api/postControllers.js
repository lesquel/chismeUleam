import { postInformation } from '../../utils/api/postInformation.js';


document.addEventListener('submit', (event) => {
    event.preventDefault();
    const form = event.target;
    const url = form.action;
    const dataToSend = new FormData(form);

    console.log('Datos a enviar:', ...dataToSend.entries()); 

    const responseAction = (data) => {
        console.log(data);
    };

    const errorAction = (error) => {
        console.error(error);
    };

    postInformation({ url, dataToSend, responseAction, errorAction });
});
