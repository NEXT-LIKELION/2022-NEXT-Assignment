const name2 = sessionStorage.getItem("user2Name");
document.querySelector('#user2Name').innerHTML = name2;

const clickedList = new Array();
let result = document.getElementById('result');
result.style.visibility = 'hidden';


//1. 클릭한 버튼 아이디 값
function clickedAns(e) {
    let clickedID = document.getElementById(e.getAttribute('id')).getAttribute('id')
   

    if (clickedList.includes(clickedID)) {
        let index = clickedList.indexOf(clickedID);
        clickedList.splice(index, 1);
        //검정
        e.style.color = 'black';

    } else {
        if (clickedList.length < 5) {
            clickedList.push(clickedID);
            //빨갛게
            e.style.color = 'red';


        }
        else {
            //빠지는 거 검정색
            //인덱스값 0을 가진 버튼의 style 바꾸기
            //인덱스 0인 버튼의 id?
            let delVal = clickedList[0];
            let btn = document.getElementById(delVal);
            btn.style.color = 'black';

            clickedList.shift();
            clickedList.push(clickedID);
            //빨갛게
            e.style.color = 'red';
        }
    }

    console.log(clickedList);


        
        

    let result = document.getElementById('result');
    if (clickedList.length !== 5) {
        result.style.visibility = 'hidden';
    } else if (clickedList.length == 5){
        result.style.visibility = 'visible';
        let clickedValue = new Array();

        for (let k = 0; k < 5; k++){
            clickedValue.push(answerList[clickedList[k]-1])
        }

        let intersec = clickedValue.filter(x => truetags.includes(x));
        console.log(intersec);

        console.log(truetags);
        console.log(intersec.length);
        sessionStorage.setItem('length', intersec.length);
    }
}


//순서 섞기
//배열에 담기
const answerList = new Array();
answerList[0] = tags[0];
answerList[1] = tags[1];
answerList[2] = tags[2];
answerList[3] = tags[3];
answerList[4] = tags[4];
answerList[5] = tags[5];
answerList[6] = tags[6];
answerList[7] = tags[7];
answerList[8] = tags[8];
answerList[9] = tags[9];

//랜덤
function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}

shuffle(answerList);

//ans1~ans10에 담기
document.getElementById('1').innerHTML = answerList[0];
document.getElementById('2').innerHTML = answerList[1];
document.getElementById('3').innerHTML = answerList[2];
document.getElementById('4').innerHTML = answerList[3];
document.getElementById('5').innerHTML = answerList[4];
document.getElementById('6').innerHTML = answerList[5];
document.getElementById('7').innerHTML = answerList[6];
document.getElementById('8').innerHTML = answerList[7];
document.getElementById('9').innerHTML = answerList[8];
document.getElementById('10').innerHTML = answerList[9];



console.log(answerList); //애가 전체 섞은 결과임

// if (clickedList.length == 5) {
//     console.log("heyy");

//     document.getElementById(String(clickedList[0])).setAttribute('name', 'sel1')
//     document.getElementById(String(clickedList[1])).setAttribute('name', 'sel2')
//     document.getElementById(String(clickedList[2])).setAttribute('name', 'sel3')
//     document.getElementById(String(clickedList[3])).setAttribute('name', 'sel4')
//     document.getElementById(String(clickedList[4])).setAttribute('name', 'sel5')
// }












    








// for (let i = 0; i < clickedList.length; i++) {
//     let ans = clickedList[i];

//     console.log(realtruetags);
//     console.log("hellllllo"); 
//     console.log(ans);
    
//     if (ans in realtruetags) {
//         console.log('정답');
//         score += 1;
//     }
// }


// document.querySelector('#score').innerHTML = score;

// localStorage.setItem('score', score);
