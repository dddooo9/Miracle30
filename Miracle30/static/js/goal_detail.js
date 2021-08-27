const participateBtn = document.querySelector(".btn3"),
  cash = document.querySelector("#cash");
  fee = document.querySelector("#fee")

participateBtn.addEventListener("click", (e) => {
  if (participateBtn.textContent.trim() == "참여"){
    if(alertCashBack()) e.preventDefault();

    if (parseInt(cash.textContent) < parseInt(fee.textContent)){
        alert(`그룹에 참여하기 위해서는 ${fee.textContent}만큼의 별이 필요합니다.`);
        e.preventDefault();
    }
  } else{ // 참여 취소
    if(alertCashBack()) e.preventDefault();
  }
  
});

function alertCashBack(){
    return !confirm(`참여 취소시 참가비는 환급되지 않습니다.`);
}