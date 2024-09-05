import { getCookie } from '../Cookie/getCookie.js';
export const postInformation = ({ url, dataToSend, responseAction, errorAction }) => {
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': dataToSend.get('csrfmiddlewaretoken')
        },
        body: dataToSend
    })
    .then(response => response.json())
    .then(data => {
        responseAction(data);
    })
    .catch((error) => {
        errorAction(error);
    });
};