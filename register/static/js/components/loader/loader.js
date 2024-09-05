export const createLoader = () => {
    const loader = document.createElement('div');
    loader.classList.add("loader-div-container");
    loader.setAttribute('style', `position: fixed;
    top: 0px;
    left: 0px;
    display: flex;
    height: 100vh;
    width: 100%;
    align-items: center;
    justify-content: center;
    --tw-backdrop-blur: blur(4px);
    -webkit-backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
    backdrop-filter: var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);`);
    loader.innerHTML = '<div class="loader"></div>';
    document.body.appendChild(loader);
    return loader;
}