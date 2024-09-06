export const createMessageErrorForm = ({ keyName, mensajeErrors }) => {
    const messageErrorForm = document.createElement('p');
    messageErrorForm.classList.add('text-naranja_claro');
    messageErrorForm.innerHTML = `${mensajeErrors}`;
    document.querySelector(`[name="${keyName}"]`).parentNode.appendChild(messageErrorForm);
    console.log(messageErrorForm);
    return messageErrorForm;
};