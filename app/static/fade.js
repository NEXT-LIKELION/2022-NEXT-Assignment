

const fade = (() => {
  //hyperlink 딜레이주기.
  const delay = 300;
  const step = 10;

  const fade = document.createElement('div');
  let opacity = 1;
  fade.className = 'hi';
  fade.style.width = '100%';
  fade.style.height = '100%';
  fade.style.top = '0px';
  fade.style.left = '0px';
  fade.style.display = 'none';
  fade.style.position = 'fixed';
  fade.style.zIndex = '10';
  fade.style.backgroundColor = `rgb(255,255,255, ${opacity})`;
  document.body.appendChild(fade);

  const fadeOut = () => {
    fade.style.display = 'block';

    const timer = setInterval(() => {
      opacity += 1 / (delay / step);
      fade.style.backgroundColor = `rgb(255, 255, 255, ${opacity}`

      if (opacity >= 1) {
        clearInterval(timer);
      }
    }, step);
  }

  const fadeIn = () => {
    fade.style.display = 'block';

    const timer = setInterval(() => {
      opacity -= 1 / (delay / step);
      fade.style.backgroundColor = `rgb(255, 255, 255, ${opacity}`

      if (opacity <= 0) {
        clearInterval(timer);
        fade.style.display = 'none';
      }
    }, step);
  }



  fadeIn();



  for (const link of document.querySelectorAll('a')) {
    link.onclick = () => {
      setTimeout(() => window.location.href = link.href, delay);
      fadeOut();
      return false;
    };
  }
  for (const btn of document.querySelectorAll('button')) {
    if (btn.type === 'submit') {
      btn.onclick = () => {
        setTimeout(() => document.querySelector(`form[data-form-id="${btn.dataset.formId}"]`).submit(), delay);
        fadeOut();
        return false;
      }
    }
  }

  return {
    fadeIn: fadeIn,
    fadeOut: fadeOut,
    delay: delay,
  };
})();