//이름
const name1 = sessionStorage.getItem("user1Name");

document.querySelector('#user1Name').innerHTML = name1;

//태그
const testName = sessionStorage.getItem('TestName');

const true1 = sessionStorage.getItem('True1');
const true2 = sessionStorage.getItem('True2');
const true3 = sessionStorage.getItem('True3');
const true4 = sessionStorage.getItem('True4');
const true5 = sessionStorage.getItem('True5');

const false1 = sessionStorage.getItem('False1');
const false2 = sessionStorage.getItem('False2');
const false3 = sessionStorage.getItem('False3');
const false4 = sessionStorage.getItem('False4');
const false5 = sessionStorage.getItem('False5');

document.querySelector('#testName').innerHTML = testName;
// document.querySelector('#true1').innerHTML = true1;
// document.querySelector('#true2').innerHTML = true2;
// document.querySelector('#true3').innerHTML = true3;
// document.querySelector('#true4').innerHTML = true4;
// document.querySelector('#true5').innerHTML = true5;
// document.querySelector('#false1').innerHTML = false1;
// document.querySelector('#false2').innerHTML = false2;
// document.querySelector('#false3').innerHTML = false3;
// document.querySelector('#false4').innerHTML = false4;
// document.querySelector('#false5').innerHTML = false5;


//순서 섞기

//배열에 담기
const answerList = new Array();
answerList[0] = true1;
answerList[1] = true2;
answerList[2] = true3;
answerList[3] = true4;
answerList[4] = true5;
answerList[5] = false1;
answerList[6] = false2;
answerList[7] = false3;
answerList[8] = false4;
answerList[9] = false5;

//랜덤
<<<<<<< HEAD
function shuffle(array){
=======
function shuffle(array) {
>>>>>>> 83288972ace1e9ec0f2878aaa2ee0758faf38ce9
    array.sort(() => Math.random() - 0.5);
}

shuffle(answerList);

//ans1~ans10에 담기
document.querySelector('#ans1').innerHTML = answerList[0];
document.querySelector('#ans2').innerHTML = answerList[1];
document.querySelector('#ans3').innerHTML = answerList[2];
document.querySelector('#ans4').innerHTML = answerList[3];
document.querySelector('#ans5').innerHTML = answerList[4];
document.querySelector('#ans6').innerHTML = answerList[5];
document.querySelector('#ans7').innerHTML = answerList[6];
document.querySelector('#ans8').innerHTML = answerList[7];
document.querySelector('#ans9').innerHTML = answerList[8];
<<<<<<< HEAD
document.querySelector('#ans10').innerHTML = answerList[9];

console.log(answerList[0]);
=======
document.querySelector('#ans10').innerHTML = answerList[9];
>>>>>>> 83288972ace1e9ec0f2878aaa2ee0758faf38ce9
