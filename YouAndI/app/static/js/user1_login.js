const createForm = document.querySelector('#create-form')
const user1Input = document.querySelector('#user1NickName');

const HIDDEN_CLASSNAME='hidden';

function createFn(event){
	event.preventDefault();
	createForm.classList.add(HIDDEN_CLASSNAME);
	const user1Name = user1Input.value;
	sessionStorage.setItem("user1Name", user1Name);

	console.log(user1Name);
}

createForm.addEventListener('submit', createFn);