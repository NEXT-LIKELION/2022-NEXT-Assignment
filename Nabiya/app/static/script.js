const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];

  document.querySelector(".date p").innerHTML = new Date().toDateString();

  let days = "";

  for (let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
  }


  let diarys_info = {'pk': [], 'date': []}
  for (i = 0; i < diarys.length ; i++){
    diarys_info['pk'].push(diarys[i]['pk']);
    diarys_info['date'].push(diarys[i]['fields']['uploaded']);
  }

  let year_month = date.getFullYear();

  if(date.getMonth() + 1 < 10){
    year_month += "-0" + (date.getMonth() + 1);
  } else {
    year_month += date.getMonth() + 1;
  }
  
  let date_str = year_month;
  console.log(diarys_info['date'])

  for (let i = 1; i <= lastDay; i++) {
    
    if (i < 10 ){
      date_str = year_month + "-0" + i;
    } else {
      date_str = year_month + "-" + i
    }

    console.log(date_str);

    let diary_idx = diarys_info['date'].indexOf(date_str);
    
    if (diary_idx != -1) {
      console.log(diarys_info['pk'][diary_idx]);
      days += `<div><a href='day_detail/${date_str}'>${i}</a></div>`
    } else {
      days += `<div><a href='day_detail/${date_str}'>${i}</a></div>`;
    }

  }

  for (let j = 1; j <= nextDays; j++) {
    days += `<div class="next-date">${j}</div>`;
    monthDays.innerHTML = days;
  }
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
