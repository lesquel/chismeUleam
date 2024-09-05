import { getCookie } from '../Cookie/getCookie.js';
export const postInformation = ({ url, dataToSend, responseAction, errorAction }) => {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': dataToSend.get('csrfmiddlewaretoken')
        },
        body: dataToSend
    })
    .then(response => response.text())
    .then(data => {
        responseAction(data);
    })
    .catch((error) => {
        errorAction(error);
    });
};