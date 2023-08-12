function chooseSpace(){
    let filterForm = document.getElementById("filterForm");
    if(filterForm[0].value == "all"){
        let allCards = document.getElementsByClassName("spaceCard")
        for(let i=0; i<allCards.length; i++){
            allCards[i].style.display = ''
        }
    } else {
        let spaceTypes = ["coworking","cafe","hostel"]
        let filteredSpaces= spaceTypes.filter(function(ele){
            return ele != filterForm[0].value
        })
        console.log(filteredSpaces)
        let spaceToBeRemoved = document.querySelectorAll(`.${filteredSpaces[0]},.${filteredSpaces[1]}`)
        for(let i=0;i<spaceToBeRemoved.length;i++){
            spaceToBeRemoved[i].style.display = 'none'
        }
    }
    
}

function hasInternet(){
    let hasNoInternet = document.getElementsByClassName("internet-False");
    let filterForm = document.getElementById('filterForm')
    if(filterForm[1].checked == true){
        for(let i=0; i<hasNoInternet.length;i++){
            hasNoInternet[i].style.display = 'none'
        }
    } else {
        for(let i=0; i<hasNoInternet.length;i++){
            hasNoInternet[i].style.display = ''
        }
    }

}

function isMeetingFriendly(){
    let notMeetingFriendly = document.getElementsByClassName("meeting-False")
    let filterForm = document.getElementById('filterForm')
    if(filterForm[2].checked == true){
        for(let i=0; i<notMeetingFriendly.length;i++){
            notMeetingFriendly[i].style.display = 'none'
        }
    } else {
        for(let i=0; i<notMeetingFriendly.length;i++){
            notMeetingFriendly[i].style.display = ''
        }
    }

}

function resetFilter(){
    let allCards = document.getElementsByClassName("spaceCard")
    for(let i=0; i<allCards.length; i++){
        allCards[i].style.display = ''
    }

}