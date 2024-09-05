import { postInformation } from '../../utils/api/postInformation.js';


const fun = (event) => {
    event.preventDefault();
    const form = event.target;
    const url = form.action;
    const dataToSend = new FormData(form);
    
    const responseAction = (data) => {
        if (data.success) {
            window.location.href = "{% url 'main:home' %}";
        }
        if (data.error) {
            document.getElementById('error-message').innerHTML = data.error;
        }
    };

    const errorAction = (error) => {
        console.error(error);
    };

    postInformation({ url, dataToSend, responseAction, errorAction });
}

document.addEventListener('submit', fun);
