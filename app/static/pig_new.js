
const userDataRaw = document.querySelector('.user-data').textContent.replace(/\s+/g, '').split('&').slice(0, -1);
const userData = userDataRaw.map((datum) => {
  const arr = datum.split(':')
  return { pk: arr[0], name: arr[1] };
});

const userAdded = [];

function refreshUserAdded () {
  const div = document.querySelector('.user-added-container');
  div.innerHTML = '';
  for ( const user of userAdded ) {
    const new_div = document.createElement('div');
    new_div.textContent = user.name;
    new_div.className = 'user-found';
    new_div.onclick = () => {
      removeUser(user);
      refreshUserAdded();
    }
    div.appendChild(new_div);
  }
}

function searchUserData (value) {
  const result = [];
  if (value) {
    for (const datum of userData) {
      if (datum.name.includes(value)) {
        result.push(datum);
      }
    }
  }
  return result;
}

function addUser (user) {
  for ( const element of userAdded ) {
    if ( element.pk === user.pk ) {
      return false;
    }
  }
  userAdded.push(user);
  refreshUserAdded();
}

const searchBar = document.querySelector('.search-bar');
searchBar.oninput = (e) => {
  const div = document.querySelector('.user-found-container');
  div.innerHTML = '';
  const searched = searchUserData(e.target.value);
  for (const user of searched) {
    const new_div = document.createElement('div');
    new_div.textContent = user.name;
    new_div.className = 'user-found';
    new_div.onclick = () => {
      addUser(user);
    }
    div.appendChild(new_div);
  }
}


const buttonPlus = document.querySelector('.button-plus');
const buttonMinus = document.querySelector('.button-minus');
const moneyField = document.querySelector('.money-field');
let moneyValue = Number(moneyField.textContent)

buttonPlus.onclick = () => {
  moneyValue += 100;
  moneyField.textContent = String(moneyValue);
}
buttonMinus.onclick = () => {
  moneyValue -= 100;
  moneyField.textContent = String(moneyValue);
}

const form = document.querySelector('form');
const submit = document.querySelector('button.submit');
submit.onclick = () => {
  const moneyInput = document.createElement('input');
  moneyInput.setAttribute('type', 'text');
  moneyInput.setAttribute('name', 'exchange_rate');
  moneyInput.setAttribute('value', String(moneyValue));
  form.appendChild(moneyInput);

  for ( const user of userAdded ) {
    const userInput = document.createElement('input');
    userInput.setAttribute('type', 'text');
    userInput.setAttribute('name', 'user_list');
    userInput.setAttribute('value', String(user.pk));
    form.appendChild(userInput);
  }

  setTimeout( () => {
    form.submit();
  }, fade.delay);
  fade.fadeOut();

  return false;
}