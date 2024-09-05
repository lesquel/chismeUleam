export const postInformation = ({ url, dataToSend, inicialAction, responseAction, errorAction, finallyAction }) => {
    inicialAction();
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
    })
    .finally(() => {
        finallyAction();
    });
};